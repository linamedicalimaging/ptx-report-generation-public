"""Verify patient-level PTX candidate counts for local dataset files."""

from __future__ import annotations

import argparse

from common import column_values, key_for_dataset, read_table


def count_patients(table_path: str, column: str, dataset: str) -> int:
    table = read_table(table_path)
    return len({key_for_dataset(value, dataset, "patient") for value in column_values(table, column)})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mimic-ptx-table")
    parser.add_argument("--mimic-column", default="0")
    parser.add_argument("--chexpert-ptx-table")
    parser.add_argument("--chexpert-column", default="0")
    parser.add_argument("--iu-ptx-table")
    parser.add_argument("--iu-column", default="0")
    args = parser.parse_args()

    if args.mimic_ptx_table:
        print(f"mimic_ptx_patients={count_patients(args.mimic_ptx_table, args.mimic_column, 'mimic')}")
    if args.chexpert_ptx_table:
        print(f"chexpert_ptx_patients={count_patients(args.chexpert_ptx_table, args.chexpert_column, 'chexpert')}")
    if args.iu_ptx_table:
        print(f"iu_ptx_patients={count_patients(args.iu_ptx_table, args.iu_column, 'iu')}")


if __name__ == "__main__":
    main()
