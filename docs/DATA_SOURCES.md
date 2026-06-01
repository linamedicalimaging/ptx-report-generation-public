# Data Sources

This project uses code and documentation to support reproducibility, but it does not redistribute any dataset files, chest radiographs, or radiology reports.

Users must obtain access to each dataset from its original provider and comply with the corresponding data-use terms.

## MIMIC-CXR-JPG

Role in this project:

- Used as one of the two source datasets for the PTX-focused train/validation/test construction.
- Used together with CheXpert Plus to form balanced PTX-positive and non-PTX splits.

Official data source:

- MIMIC-CXR-JPG Database, PhysioNet:
  https://physionet.org/content/mimic-cxr-jpg/2.0.0/

Related original database:

- MIMIC-CXR Database, PhysioNet:
  https://physionet.org/content/mimic-cxr/

Access notes:

- Requires credentialed access through PhysioNet.
- The data-use agreement does not permit redistribution of images or reports.
- This repository therefore provides reconstruction scripts only.

Recommended citations:

- Johnson AEW, Pollard TJ, Berkowitz SJ, et al. MIMIC-CXR, a de-identified publicly available database of chest radiographs with free-text reports. Scientific Data. 2019.
- Johnson AEW, Pollard TJ, Greenbaum NR, et al. MIMIC-CXR-JPG, a large publicly available database of labeled chest radiographs. arXiv:1901.07042.

## CheXpert Plus

Role in this project:

- Used as one of the two source datasets for the PTX-focused train/validation/test construction.
- Used together with MIMIC-CXR-JPG to form balanced PTX-positive and non-PTX splits.

Official data source:

- CheXpert Plus, Stanford AIMI:
  https://aimi.stanford.edu/datasets/chexpert-plus

Related code/model information:

- Stanford-AIMI CheXpert Plus repository:
  https://github.com/Stanford-AIMI/chexpert-plus

Access notes:

- Users must obtain the dataset from Stanford AIMI and comply with its terms.
- This repository does not redistribute CheXpert Plus images, reports, metadata files, or derived report text.

Recommended citation:

- Chambon P, Delbrouck JB, Sounack T, et al. CheXpert Plus: Augmenting a Large Chest X-ray Dataset with Text Radiology Reports, Patient Demographics and Additional Image Formats. arXiv:2405.19538.

## IU X-ray / Open-i Indiana University Chest X-ray Collection

Role in this project:

- Considered during dataset construction.
- Excluded from the final PTX-focused split because too few PTX-positive patients remained after patient-level processing and author-test exclusion.

Official data source:

- Open-i, National Library of Medicine:
  https://openi.nlm.nih.gov/

Access notes:

- The dataset is publicly available through Open-i and related mirrors.
- This repository does not redistribute IU X-ray images or reports.

Recommended citation:

- Demner-Fushman D, Kohli MD, Rosenman MB, et al. Preparing a collection of radiology examinations for distribution and retrieval. Journal of the American Medical Informatics Association. 2016;23(2):304-310.

## Summary of Redistribution Policy

This repository does not include:

- MIMIC-CXR-JPG images or reports;
- CheXpert Plus images or reports;
- IU X-ray/Open-i images or reports;
- raw report text copied from any of the above datasets;
- Excel files or generated-output files containing restricted ground-truth or generated report text.

The repository provides only code, documentation, configuration examples, and evaluation rules.

