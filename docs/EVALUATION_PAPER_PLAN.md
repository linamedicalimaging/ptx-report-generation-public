# AI-vs-Human Evaluation Paper Plan

## Proposed Positioning

We propose and validate a transparent, radiologist-aligned, disease-aware evaluation framework for chest X-ray report generation, using pneumothorax as a clinically important case study.

The claim should be careful:

- The framework is more clinically interpretable than generic lexical metrics.
- The framework is more fine-grained for PTX-focused evaluation than coarse clinical efficacy labels.
- The framework is not claimed to be universally superior for every ARRG setting.

## Main Question

Can a strict ground-truth-only, disease-aware AI evaluation protocol produce scores that align closely with radiologist scoring for pneumothorax-focused chest X-ray report generation?

## Evaluation Framework

- Strict GT-only rule.
- PTX primary score:
  - present;
  - side;
  - location;
  - extent;
  - sequential scoring;
  - uncertain PTX handling;
  - bilateral/multifocal component weighting.
- Global secondary score:
  - major true findings;
  - minor true findings;
  - major false findings;
  - minor false findings.
- Best-model selection:
  - PTX-best;
  - Global-best;
  - explicit tie-break rules.

## Recommended Validation Design

Separate the evaluation into two phases:

1. Calibration phase:
   - early cases used to develop and refine Legend/Prompt;
   - disagreements between AI and radiologist are discussed;
   - rules are updated and documented.

2. Frozen-rule validation phase:
   - later held-out cases are scored after the Legend/Prompt are fixed;
   - AI and human scoring are compared quantitatively;
   - this phase supports the main validation claim.

Recommended validation size:

- minimum: 50 cases;
- better: 100 cases;
- stronger: 150 cases.

Each case includes eight model reports, so 100 cases provide 800 model-report evaluations.

## Main Agreement Metrics

- Exact agreement for PTX Present.
- Exact agreement for PTX Side.
- Exact agreement for PTX Location.
- Exact agreement for PTX Extent.
- Agreement on PTX-best.
- Agreement on Global-best.
- Mean absolute difference in PTX_total_norm.
- Mean absolute difference in Global_total.
- Spearman correlation for PTX_total_norm.
- Spearman correlation for Global_total.
- Cohen's kappa for categorical labels where appropriate.
- ICC for continuous scores if appropriate.

## Comparison With Conventional Metrics

Compare the proposed clinical scores against common ARRG metrics:

- BLEU;
- ROUGE;
- METEOR;
- CIDEr;
- clinical efficacy labels if available.

Important examples:

- high lexical score but clinically wrong PTX;
- low lexical overlap but clinically correct PTX;
- correct PTX but major non-PTX omission;
- PTX false positive in a non-PTX GT case.

## Draft Structure

1. Introduction
2. Related Work
3. Materials
4. Evaluation Framework
5. AI-Human Agreement Study
6. Results
7. Discussion
8. Limitations
9. Conclusion

