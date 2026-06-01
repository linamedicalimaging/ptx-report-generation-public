# Data Scripts

These scripts are public-safe helpers for reconstructing the pneumothorax
(PTX) data preparation workflow in a local environment where the user already
has authorized access to the source datasets.

## What These Scripts Do

- identify PTX-positive reports using transparent keyword rules;
- compare report-derived labels with structured labels when available;
- count overlap between author test splits and PTX/non-PTX candidate pools;
- build balanced patient-level train/validation/test splits from local inputs.

## What These Scripts Do Not Include

- no MIMIC-CXR-JPG, CheXpert Plus, or IU X-ray images;
- no reports, report snippets, or generated report text;
- no annotation JSON files produced from restricted datasets;
- no Excel workbooks containing case-level reports or model outputs;
- no checkpoints or LoRA weights.

Generated outputs may contain restricted identifiers, report snippets, or
report text depending on the input files. Keep generated outputs outside the
repository or in paths ignored by `.gitignore`.

## Typical Workflow

1. Run `extract_ptx_reports.py` on locally available reports to create
   PTX-positive candidate tables.
2. Run `report_label_compare.py` if structured labels are available and need
   to be compared with report-derived labels.
3. Run `count_author_test_ptx.py` to estimate overlap with an author test
   split.
4. Run `count_ptx_patients_by_dataset.py` to verify patient-level PTX counts.
5. Run `build_balanced_splits.py` to reconstruct balanced mixed-source splits.

All paths are supplied as command-line arguments. Do not add private absolute
paths to these public scripts.
