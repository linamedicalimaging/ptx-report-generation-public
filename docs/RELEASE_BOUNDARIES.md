# Release Boundaries

This document defines what can and cannot be included in the public repository.

## Publicly Shareable

- Project-specific code written for this PTX-focused experiment.
- Scripts that reconstruct splits from locally available authorized datasets.
- Configuration examples without private paths or credentials.
- Final Legend, Prompt, and PTX terminology rules.
- Analysis code for AI-vs-human agreement and model comparison.
- Empty or synthetic templates that do not contain restricted reports.
- Documentation describing methods and reproduction steps.

## Not Publicly Shareable

- MIMIC-CXR-JPG images or reports.
- CheXpert Plus images or reports.
- IU X-ray images or reports.
- Any copied dataset files.
- Full generated report files if they reproduce report text derived from restricted data.
- Excel files containing raw GT reports, generated reports, or case-level text from restricted datasets.
- Author-provided checkpoints unless the original license explicitly permits redistribution.
- LoRA checkpoints unless base-model and dataset licenses permit redistribution.
- Private local paths that reveal unnecessary personal or institutional information.

## Original Work Boundary

The CXPMRG-Bench/MambaXray-VL paper and original implementation are not our work. The public codebase is:

https://github.com/Event-AHU/Medical_Image_Analysis

Our repository should describe that work as the original framework, reproduced baseline, and source of author-provided checkpoints. Our contribution is the PTX-focused adaptation and evaluation layer built on top of it.

## Recommended Wording

Use:

> This study builds upon the publicly released CXPMRG-Bench/MambaXray-VL implementation and author-provided checkpoints.

Avoid:

> We propose CXPMRG-Bench.

Avoid:

> Our model is CXPMRG-Bench.

Use:

> We adapt the author-provided checkpoints for pneumothorax-focused report generation using LoRA.

