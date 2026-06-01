# Evaluation Protocol

This document summarizes the public, case-independent evaluation rules used for
the pneumothorax-focused report generation study. It does not contain patient
data, reports, model outputs, or case-level scores.

## Core Rule

Evaluation follows a strict GT-only rule:

- GT report text and GT labels are the reference standard.
- Findings explicitly supported by GT can receive true-finding credit.
- Findings not supported by GT are counted as false findings according to their
  clinical category.
- Chest radiographs are not reinterpreted during AI scoring.

The aim is to make AI scoring repeatable and auditable, while keeping the
criteria aligned with radiologist review.

## Models Evaluated

GT is used only as the reference. Model comparison is performed across the
generated reports from:

- CheXpert_author
- Mimic_author
- CheXpert_text_only
- CheXpert_vision_only
- CheXpert_both
- Mimic_text_only
- Mimic_vision_only
- Mimic_both

## PTX Primary Evaluation

PTX scoring evaluates pneumothorax diagnosis using:

- Present
- Side
- Location
- Extent

The scoring order is hierarchical:

1. Score Present.
2. If Present is incorrect, stop PTX scoring for that model.
3. If Present is correct, score Side.
4. If Side is incorrect, stop downstream PTX attribute scoring.
5. If Side is correct, score Location when GT specifies location.
6. If Location is specified by GT and incorrect, stop downstream Extent scoring
   for that PTX component.
7. If Location is correct or skipped because GT does not specify location, score
   Extent when GT specifies extent.

If GT has no PTX, only Present is scored.

If GT has PTX but does not specify Location and/or Extent, the unspecified
attribute is not included in the maximum score. For example:

- GT says right PTX without location or extent: max = Present + Side.
- GT says right small PTX without location: max = Present + Side + Extent.
- GT says right apical PTX without extent: max = Present + Side + Location.
- GT says right apical small PTX: max = Present + Side + Location + Extent.

## Component-Weighted PTX

For bilateral or multifocal PTX with distinct GT-supported components, scoring
is component-weighted. Each GT-supported PTX component contributes equally to
the available Present, Side, Location, and Extent points when those attributes
are specified.

Example:

GT: right apical small PTX and left large PTX.

Model: right small PTX only.

Available points:

- Present: right component + left component
- Side: right component + left component
- Location: right apical component only, because left location is not specified
- Extent: right small component + left large component

The model receives credit only for the right-sided component it clinically
covers. It receives no left-sided component credit.

## Uncertain PTX

When GT describes uncertain PTX, record GT Present as uncertain. For evaluation,
uncertain PTX is treated as a GT-supported PTX finding for detection purposes,
but over-definite model wording should be recorded in notes and may be used as a
tie-break penalty if models otherwise remain tied.

## Global Secondary Evaluation

Global evaluation measures clinically relevant report quality beyond PTX.

Major true findings are GT-supported clinically important findings correctly
reported by the model. Examples include:

- pneumothorax
- pleural effusion
- atelectasis
- consolidation or pneumonia
- pulmonary edema, vascular congestion, or interstitial edema
- cardiomegaly or enlarged cardiomediastinal silhouette
- lung opacity, infiltrate, nodule, lesion, or mass
- acute fracture
- subcutaneous emphysema
- mediastinal shift
- hyperinflation, COPD, or emphysema
- fibrosis or scarring when reported as a positive finding
- lobar or lung collapse

Minor true findings are GT-supported lower-acuity or background findings
correctly reported by the model. Examples include:

- PICC, central venous catheter, chest tube, pleural drain
- endotracheal or enteric tube
- pacemaker or ICD
- postoperative or postsurgical changes
- surgical clips
- sternotomy wires or CABG changes
- aortic calcification or tortuosity
- degenerative osseous changes, spondylosis, or osteoarthritis
- old, healed, or chronic fracture deformity
- low lung volume or hypoinflation
- elevated hemidiaphragm
- calcified granuloma

Unsupported model findings are counted as false findings according to the same
major/minor clinical category. Findings that are clinically plausible or visible
on the image still count as false if not supported by GT.

## Template and Trailing Text

Irrelevant trailing text, template artifacts, and recommendation-like phrases
are not automatically counted as major or minor false findings. They are counted
as false findings only when they explicitly state an unsupported clinical or
radiological positive finding.

Otherwise, they should be recorded in notes and used only as a tie-break
penalty.

Unsupported claims about comparison timing, such as a specific prior date or a
generic comparison statement not present in GT, should usually be recorded in
notes rather than counted as a false clinical finding, unless the statement
introduces a concrete unsupported clinical change.

## Best-Model Selection

Best-model selection is performed separately for PTX_best and Global_best.

1. Exclude invalid outputs.
2. Rank by primary score:
   - PTX_best: PTX_total_norm.
   - Global_best: Global_total.
3. If tied, prefer better coverage of GT-supported major findings.
4. If tied, prefer better coverage of GT-supported minor findings.
5. If tied, prefer fewer clinically relevant major false findings.
6. If tied, prefer fewer clinically relevant minor false findings.
7. If tied, prefer complete and coherent reports over truncated, repetitive, or
   irrelevant-template reports.
8. If still tied, allow multiple best models.
