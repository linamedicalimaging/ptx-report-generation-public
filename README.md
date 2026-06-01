# Pneumothorax-Focused Adaptation and Evaluation of Chest X-ray Report Generation Models

This repository contains code, configuration examples, and evaluation protocols for a pneumothorax-focused study of chest X-ray automated radiology report generation.

The project builds on the publicly released CXPMRG-Bench/MambaXray-VL implementation and author-provided checkpoints, and studies pneumothorax-specific LoRA adaptation and clinically oriented evaluation.

## Important Boundary

This repository is **not** the original CXPMRG-Bench repository.

The original CXPMRG-Bench/MambaXray-VL work and code belong to the original authors. Their public codebase is available at:

https://github.com/Event-AHU/Medical_Image_Analysis

Our work uses the original framework and author-provided checkpoints as reproduced baselines and base models. The contribution of this repository is limited to:

- pneumothorax-focused data construction scripts;
- LoRA fine-tuning and inference scripts for the reproduced framework;
- clinically oriented pneumothorax and global report evaluation protocols;
- analysis scripts for comparing author models and PTX-focused LoRA-adapted models;
- documentation for reproducing the study with authorized access to the required datasets.

## What Is Included

This public repository is intended to include:

- scripts for PTX report screening and dataset split construction;
- configuration examples for LoRA text-only, vision-only, and joint adaptation;
- inference and result-combination utilities;
- final evaluation rules, including Legend, Prompt, and PTX terminology mapping;
- AI-vs-human evaluation analysis scripts;
- table and figure generation scripts for manuscript preparation.

## What Is Not Included

This repository does **not** redistribute:

- MIMIC-CXR-JPG images or reports;
- CheXpert Plus images or reports;
- IU X-ray images or reports;
- raw report text from restricted datasets;
- chest radiograph image files;
- author-provided model checkpoints;
- LoRA checkpoints, unless redistribution is later confirmed to be license-compatible;
- full Excel workbooks containing ground-truth reports or generated reports from restricted datasets.

Users must obtain access to the original datasets from their official providers and reconstruct the experiment locally.

## Datasets

The study uses MIMIC-CXR-JPG and CheXpert Plus. IU X-ray/Open-i was considered but excluded from the PTX-focused split construction because too few PTX-positive patients remained after patient-level processing and author-test exclusion.

Dataset access is controlled by the original dataset providers. This repository provides code and documentation only.

Dataset links, recommended citations, and redistribution boundaries are listed in:

- [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md)

## Evaluation Framework

The evaluation is based on a strict ground-truth-only rule:

- findings explicitly supported by the GT report/labels can receive true-positive credit;
- unsupported positive model findings are treated as false findings;
- chest images are not reinterpreted during AI scoring.

The evaluation separates:

- PTX primary scoring: present, side, location, extent;
- Global secondary scoring: major/minor true findings and major/minor false findings;
- best-model selection: PTX-best and Global-best with explicit tie-break rules.

## Planned Papers

This repository supports two related studies:

1. PTX-focused LoRA adaptation of chest X-ray report generation models.
2. Radiologist-aligned AI evaluation for chest X-ray report generation using pneumothorax as a clinically important case study.

## Citation

Please cite the original CXPMRG-Bench/MambaXray-VL paper and repository when using the reproduced framework or author-provided checkpoints.

Citation details for our PTX-focused study will be added after manuscript preparation.
