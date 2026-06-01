"""Shared helpers for public-safe data preparation scripts.

The helpers intentionally avoid project-specific absolute paths. Generated
outputs may still contain restricted dataset identifiers or report text, so
outputs should not be committed.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable


def read_table(path: str | Path, sheet_name: str | int | None = 0):
    """Read CSV/TSV/XLSX files with pandas.

    Pandas is used because the original local workflow used Excel workbooks.
    The dependency is optional until these scripts are executed.
    """

    import pandas as pd

    path = Path(path)
    suffix = path.suffix.lower()
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path, sheet_name=sheet_name)
    if suffix == ".tsv":
        return pd.read_csv(path, sep="\t")
    return pd.read_csv(path)


def column_values(frame: Any, column: str | int) -> list[str]:
    """Return non-empty values from a table column.

    The column can be a zero-based integer index or a column name.
    """

    if isinstance(column, str) and column.isdigit():
        column = int(column)
    series = frame.iloc[:, column] if isinstance(column, int) else frame[column]
    return [str(x).strip() for x in series.dropna().tolist() if str(x).strip()]


def normalize_path(value: str) -> str:
    return re.sub(r"/+", "/", value.replace("\\", "/").strip()).lower()


def basename_key(value: str) -> str:
    return Path(normalize_path(value)).stem


def mimic_study_key(value: str) -> str:
    """Return a MIMIC-style study key from a file path or study id."""

    text = basename_key(value)
    match = re.search(r"(s?\d+)", text)
    return match.group(1).lstrip("s") if match else text


def mimic_patient_key(value: str) -> str:
    text = normalize_path(value)
    match = re.search(r"(p\d{2,})", text)
    return match.group(1)


def chexpert_patient_key(value: str) -> str:
    text = normalize_path(value)
    match = re.search(r"(patient\d+)", text)
    return match.group(1)


def iu_patient_key(value: str) -> str:
    text = basename_key(value)
    match = re.search(r"(\d+)", text)
    return match.group(1) if match else text


def key_for_dataset(value: str, dataset: str, level: str = "patient") -> str:
    dataset = dataset.lower()
    level = level.lower()
    if dataset == "mimic":
        return mimic_patient_key(value) if level == "patient" else mimic_study_key(value)
    if dataset == "chexpert":
        return chexpert_patient_key(value) if level == "patient" else normalize_path(value)
    if dataset == "iu":
        return iu_patient_key(value)
    return normalize_path(value)


def load_annotation(path: str | Path) -> dict[str, list[dict[str, Any]]]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, dict):
        return {k: list(v) for k, v in data.items() if isinstance(v, list)}
    if isinstance(data, list):
        return {"all": data}
    raise TypeError(f"Unsupported annotation format: {type(data)!r}")


def entry_paths(entry: dict[str, Any]) -> list[str]:
    """Extract image/report path-like fields from an annotation entry."""

    paths: list[str] = []
    for key in ("image_path", "image_paths", "images", "path", "paths", "id", "study_id"):
        value = entry.get(key)
        if isinstance(value, str):
            paths.append(value)
        elif isinstance(value, Iterable):
            paths.extend(str(x) for x in value if x is not None)
    return paths


def entry_text(entry: dict[str, Any]) -> str:
    fields = ("report", "text", "findings", "impression")
    parts = [str(entry.get(k, "")).strip() for k in fields if entry.get(k)]
    return " ".join(parts).strip()
