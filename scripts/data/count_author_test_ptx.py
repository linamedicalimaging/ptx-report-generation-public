"""Count PTX/non-PTX candidates overlapping an author test split.

Inputs must be local files available under the relevant dataset licenses.
Do not commit generated outputs or case-level tables.
"""

from __future__ import annotations

import argparse

from common import column_values, entry_paths, key_for_dataset, load_annotation, read_table


def candidate_keys(path: str, column: str, dataset: str, level: str) -> set[str]:
    table = read_table(path)
    return {key_for_dataset(value, dataset, level) for value in column_values(table, column)}


def annotation_keys(path: str, split: str, dataset: str, level: str) -> set[str]:
    annotation = load_annotation(path)
    entries = annotation.get(split, [])
    keys: set[str] = set()
    for entry in entries:
        for value in entry_paths(entry):
            key = key_for_dataset(value, dataset, level)
            if key:
                keys.add(key)
    return keys


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True, choices=["mimic", "chexpert", "iu"])
    parser.add_argument("--annotation-json", required=True)
    parser.add_argument("--split", default="test")
    parser.add_argument("--ptx-table", required=True)
    parser.add_argument("--non-ptx-table", required=True)
    parser.add_argument("--ptx-column", default="0", help="Column name or zero-based index.")
    parser.add_argument("--non-ptx-column", default="0", help="Column name or zero-based index.")
    parser.add_argument("--level", default="patient", choices=["patient", "study"])
    args = parser.parse_args()

    author = annotation_keys(args.annotation_json, args.split, args.dataset, args.level)
    ptx = candidate_keys(args.ptx_table, args.ptx_column, args.dataset, args.level)
    non_ptx = candidate_keys(args.non_ptx_table, args.non_ptx_column, args.dataset, args.level)

    print(f"dataset={args.dataset}")
    print(f"split={args.split}")
    print(f"author_{args.level}_count={len(author)}")
    print(f"ptx_overlap={len(author & ptx)}")
    print(f"non_ptx_overlap={len(author & non_ptx)}")
    print(f"unmatched_author={len(author - ptx - non_ptx)}")


if __name__ == "__main__":
    main()
