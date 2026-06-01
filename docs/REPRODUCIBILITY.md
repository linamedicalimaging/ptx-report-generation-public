# Reproducibility Notes

This repository is designed to support reproducibility without redistributing restricted data.

## Required External Resources

Users need authorized local access to:

- MIMIC-CXR-JPG;
- CheXpert Plus;
- the original CXPMRG-Bench/MambaXray-VL code and checkpoints, subject to the original authors' license and distribution terms.

Original codebase:

https://github.com/Event-AHU/Medical_Image_Analysis

## Reproduction Workflow

1. Obtain access to the required datasets from the official providers.
2. Download or clone the original CXPMRG-Bench/MambaXray-VL implementation.
3. Configure local dataset paths.
4. Run PTX screening and author-test exclusion scripts.
5. Construct the PTX-focused train/validation/test splits.
6. Run LoRA fine-tuning scripts.
7. Run inference for the author and LoRA-adapted models.
8. Combine generated reports.
9. Apply the clinical evaluation protocol.
10. Run statistical analysis scripts.

## Notes on Dataset Splits

The PTX-focused primary analysis uses a balanced 592-case test set constructed from MIMIC-CXR-JPG and CheXpert Plus.

The public repository should provide reconstruction logic, not the restricted reports or images themselves.

