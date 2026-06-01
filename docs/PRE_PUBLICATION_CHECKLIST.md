# Pre-Publication Checklist

Use this checklist before pushing the repository to GitHub.

## Contribution Boundary

- [ ] README states that this is not the original CXPMRG-Bench repository.
- [ ] README links to the original authors' public codebase:
      https://github.com/Event-AHU/Medical_Image_Analysis
- [ ] Original CXPMRG-Bench/MambaXray-VL paper is cited as prior work.
- [ ] Our contribution is described as PTX-focused adaptation and evaluation.
- [ ] No wording implies that we created the original CXPMRG-Bench framework.

## Data Boundary

- [ ] No MIMIC-CXR-JPG images are included.
- [ ] No MIMIC-CXR-JPG reports are included.
- [ ] No CheXpert Plus images are included.
- [ ] No CheXpert Plus reports are included.
- [ ] No IU X-ray images or reports are included.
- [ ] No full Excel workbook with GT or generated report text is included.
- [ ] No generated report files containing restricted report text are included.
- [ ] No patient-identifying information is included.

## Model Boundary

- [ ] No author-provided checkpoints are included.
- [ ] No LoRA checkpoints are included unless redistribution is explicitly license-compatible.
- [ ] No downloaded foundation model weights are included.
- [ ] Instructions require users to obtain allowed model resources themselves.

## File Safety

- [ ] Run a file extension scan for `.xlsx`, `.xls`, `.csv`, `.jsonl`, `.jpg`, `.png`, `.dcm`, `.pth`, `.pt`, `.ckpt`, and `.safetensors`.
- [ ] Check for private absolute paths such as local OneDrive paths.
- [ ] Check for hard-coded usernames, server IP addresses, or private credentials.
- [ ] Check that `.gitignore` excludes data, results, images, weights, and checkpoints.

## License and Citation

- [ ] Decide repository license before public release.
- [ ] Ensure license does not conflict with original code or dataset terms.
- [ ] Add citation information for the original framework.
- [ ] Add citation information for MIMIC-CXR-JPG and CheXpert Plus.
- [ ] Add citation information for our manuscript once available.

