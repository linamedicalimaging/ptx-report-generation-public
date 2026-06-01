"""Build balanced patient-level PTX/non-PTX splits from local annotations.

The produced annotation files can contain restricted report text and image
paths. Keep outputs outside the repository or in ignored directories.
"""

from __future__ import annotations

import argparse
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

from common import column_values, entry_paths, key_for_dataset, load_annotation, read_table


def load_key_set(table_path: str, column: str, dataset: str) -> set[str]:
    table = read_table(table_path)
    return {key_for_dataset(value, dataset, "patient") for value in column_values(table, column)}


def collect_entries(annotation_path: str, dataset: str) -> list[dict[str, Any]]:
    annotation = load_annotation(annotation_path)
    rows: list[dict[str, Any]] = []
    for split_entries in annotation.values():
        for entry in split_entries:
            paths = entry_paths(entry)
            if not paths:
                continue
            patient = key_for_dataset(paths[0], dataset, "patient")
            if patient:
                copied = dict(entry)
                copied["_dataset"] = dataset
                copied["_patient_key"] = patient
                rows.append(copied)
    return rows


def one_per_patient(entries: list[dict[str, Any]], allowed_patients: set[str], rng: random.Random) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        if entry["_patient_key"] in allowed_patients:
            grouped[entry["_patient_key"]].append(entry)
    selected = []
    for patient_entries in grouped.values():
        selected.append(rng.choice(patient_entries))
    return selected


def split_rows(rows: list[dict[str, Any]], val_ratio: float, test_ratio: float, rng: random.Random):
    shuffled = list(rows)
    rng.shuffle(shuffled)
    n = len(shuffled)
    n_test = round(n * test_ratio)
    n_val = round(n * val_ratio)
    test = shuffled[:n_test]
    val = shuffled[n_test : n_test + n_val]
    train = shuffled[n_test + n_val :]
    return train, val, test


def strip_internal_keys(entry: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in entry.items() if not k.startswith("_")}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mimic-annotation", required=True)
    parser.add_argument("--chexpert-annotation", required=True)
    parser.add_argument("--mimic-ptx-table", required=True)
    parser.add_argument("--mimic-non-ptx-table", required=True)
    parser.add_argument("--chexpert-ptx-table", required=True)
    parser.add_argument("--chexpert-non-ptx-table", required=True)
    parser.add_argument("--mimic-column", default="0")
    parser.add_argument("--chexpert-column", default="0")
    parser.add_argument("--samples-per-class", type=int, default=None)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--test-ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out-json", required=True)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    mimic_entries = collect_entries(args.mimic_annotation, "mimic")
    chex_entries = collect_entries(args.chexpert_annotation, "chexpert")

    pools = {
        ("mimic", "ptx"): one_per_patient(
            mimic_entries, load_key_set(args.mimic_ptx_table, args.mimic_column, "mimic"), rng
        ),
        ("mimic", "non_ptx"): one_per_patient(
            mimic_entries, load_key_set(args.mimic_non_ptx_table, args.mimic_column, "mimic"), rng
        ),
        ("chexpert", "ptx"): one_per_patient(
            chex_entries, load_key_set(args.chexpert_ptx_table, args.chexpert_column, "chexpert"), rng
        ),
        ("chexpert", "non_ptx"): one_per_patient(
            chex_entries, load_key_set(args.chexpert_non_ptx_table, args.chexpert_column, "chexpert"), rng
        ),
    }

    target = args.samples_per_class or min(len(rows) for rows in pools.values())
    balanced: list[dict[str, Any]] = []
    for key, rows in pools.items():
        if len(rows) < target:
            raise ValueError(f"Not enough rows for {key}: have {len(rows)}, need {target}")
        sampled = rng.sample(rows, target)
        for row in sampled:
            row["_label_group"] = key[1]
        balanced.extend(sampled)

    train, val, test = split_rows(balanced, args.val_ratio, args.test_ratio, rng)
    output = {
        "train": [strip_internal_keys(x) for x in train],
        "val": [strip_internal_keys(x) for x in val],
        "test": [strip_internal_keys(x) for x in test],
    }

    out_path = Path(args.out_json)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2)

    print(f"wrote {out_path}")
    print(f"train={len(train)} val={len(val)} test={len(test)} target_per_dataset_label={target}")


if __name__ == "__main__":
    main()
