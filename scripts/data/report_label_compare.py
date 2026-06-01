"""Compare report-derived PTX labels with structured labels.

This is a minimal public-safe comparison utility. It does not include source
labels or reports. Outputs can contain identifiers and should not be committed.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from common import column_values, read_table
from extract_ptx_reports import classify_ptx


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-table", required=True, help="CSV/TSV/XLSX with local reports and optional labels.")
    parser.add_argument("--id-column", default="0")
    parser.add_argument("--report-column", required=True)
    parser.add_argument("--structured-ptx-column", default=None)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--include-uncertain", action="store_true")
    args = parser.parse_args()

    table = read_table(args.input_table)
    ids = column_values(table, args.id_column)
    reports = column_values(table, args.report_column)
    structured = column_values(table, args.structured_ptx_column) if args.structured_ptx_column is not None else []

    rows = []
    for index, report in enumerate(reports):
        label, evidence = classify_ptx(report)
        report_positive = int(label == "positive" or (args.include_uncertain and label == "uncertain"))
        structured_value = structured[index] if index < len(structured) else ""
        rows.append(
            {
                "id": ids[index] if index < len(ids) else index,
                "report_ptx_label": label,
                "report_ptx_positive": report_positive,
                "structured_ptx_label": structured_value,
                "evidence": evidence,
            }
        )

    out_path = Path(args.out_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else ["id"])
        writer.writeheader()
        writer.writerows(rows)

    if structured:
        agree = sum(str(row["report_ptx_positive"]) == str(row["structured_ptx_label"]) for row in rows)
        print(f"agreement_raw={agree}/{len(rows)}")
    print(f"wrote {len(rows)} rows to {out_path}")


if __name__ == "__main__":
    main()
