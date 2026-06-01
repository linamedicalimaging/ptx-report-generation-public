"""Extract PTX-positive candidate reports from local authorized datasets.

This script contains only rule logic. It does not include reports or images.
Outputs may contain report snippets or identifiers and must not be committed.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

PTX_TERMS = [
    r"pneumothorax",
    r"ptx",
    r"hydropneumothorax",
    r"apical pleural air",
]

NEGATION_PATTERNS = [
    r"no (?:evidence of |definite |new |residual )?(?:right |left |bilateral )?pneumothorax",
    r"without (?:evidence of )?(?:right |left |bilateral )?pneumothorax",
    r"negative for (?:right |left |bilateral )?pneumothorax",
    r"pneumothorax (?:is )?(?:not seen|absent|resolved)",
]

UNCERTAIN_PATTERNS = [
    r"(?:possible|probable|questionable|suspected|tiny|trace) (?:right |left |bilateral )?pneumothorax",
    r"cannot exclude (?:right |left |bilateral )?pneumothorax",
    r"may represent (?:right |left |bilateral )?pneumothorax",
]


def classify_ptx(text: str) -> tuple[str, str]:
    """Return (label, evidence): positive, uncertain, negative, or absent."""

    compact = re.sub(r"\s+", " ", text.lower()).strip()
    if not compact:
        return "absent", ""

    for pattern in UNCERTAIN_PATTERNS:
        match = re.search(pattern, compact)
        if match:
            return "uncertain", match.group(0)

    for pattern in NEGATION_PATTERNS:
        match = re.search(pattern, compact)
        if match:
            return "negative", match.group(0)

    for pattern in PTX_TERMS:
        match = re.search(pattern, compact)
        if match:
            start = max(0, match.start() - 80)
            end = min(len(compact), match.end() + 80)
            return "positive", compact[start:end]

    return "absent", ""


def iter_json_reports(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    entries = []
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, list):
                entries.extend(value)
    elif isinstance(data, list):
        entries = data
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        text = " ".join(
            str(entry.get(key, "")).strip()
            for key in ("report", "text", "findings", "impression")
            if entry.get(key)
        )
        yield {
            "id": entry.get("id") or entry.get("study_id") or entry.get("image_path") or "",
            "path": entry.get("image_path") or entry.get("path") or "",
            "text": text,
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", required=True, help="Local annotation/report JSON.")
    parser.add_argument("--out-csv", required=True, help="Output CSV path. Do not commit it.")
    parser.add_argument(
        "--include-uncertain",
        action="store_true",
        help="Treat uncertain PTX as PTX-positive in the ptx_positive column.",
    )
    args = parser.parse_args()

    rows = []
    for item in iter_json_reports(Path(args.input_json)):
        label, evidence = classify_ptx(item["text"])
        rows.append(
            {
                "id": item["id"],
                "path": item["path"],
                "ptx_label": label,
                "ptx_positive": int(label == "positive" or (args.include_uncertain and label == "uncertain")),
                "evidence": evidence,
            }
        )

    out_path = Path(args.out_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "path", "ptx_label", "ptx_positive", "evidence"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows to {out_path}")


if __name__ == "__main__":
    main()
