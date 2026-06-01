# PTX Terminology Mapping

This document describes terminology equivalence rules used during PTX-focused
evaluation. It is a public, case-independent summary and does not include
patient reports.

## Principle

Different wording can receive credit when it is clinically equivalent to the GT
label. Equivalence is judged only against GT-supported PTX findings and does not
allow the evaluator to infer new findings from the image.

## Side

Equivalent wording examples:

- right: right, right-sided, right hemithorax
- left: left, left-sided, left hemithorax
- bilateral: bilateral, both sides, both hemithoraces

If GT is unilateral and the model reports only the opposite side, Side is
incorrect and downstream PTX attribute scoring stops for that component.

If GT is unilateral and the model reports bilateral PTX, the GT-supported side
can receive partial credit while the unsupported side should be considered in
false-finding and tie-break review.

## Location

Equivalent wording examples:

- apical: apex, apical, lung apex, upper apical pleural space
- basilar: base, basal, lung base, costophrenic region
- lateral: lateral pleural space, lateral hemithorax
- anterior: anterior pleural space
- apicolateral: apical and lateral, upper lateral pleural space

Location is scored only when GT specifies a PTX location. If GT does not specify
location, do not penalize the model for omitting location.

## Extent

Equivalent wording examples:

- trace: tiny, minimal, very small
- small: small, slight, mild
- moderate: moderate, moderately sized
- large: large, sizable, extensive

Extent is scored only when GT specifies PTX extent. If GT does not specify
extent, do not penalize the model for omitting extent.

## Uncertain Wording

Uncertain wording examples include:

- possible pneumothorax
- questionable pneumothorax
- suspected pneumothorax
- cannot exclude pneumothorax

When GT is uncertain, record Present as uncertain. Model wording that is more
definitive than GT may still detect the GT-supported PTX concept, but the
certainty mismatch should be noted and can be used as a tie-break penalty.

## Non-Equivalent Cases

The following are not equivalent:

- right PTX vs left PTX
- apical PTX vs basilar PTX when GT specifies location
- trace PTX vs large PTX when GT specifies extent
- no PTX vs definite PTX

Unsupported additional PTX components should not receive true credit, even if
they are clinically plausible.
