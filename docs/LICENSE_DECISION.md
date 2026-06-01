# License Decision Notes

The final public license should be chosen carefully because this repository builds on external code, datasets, and author-provided checkpoints.

## Current Recommendation

Do not finalize the public license until the following have been checked:

- the license of the original CXPMRG-Bench/MambaXray-VL codebase;
- the redistribution terms for author-provided checkpoints;
- MIMIC-CXR-JPG data-use restrictions;
- CheXpert Plus data-use restrictions;
- whether any copied scripts from the original repository remain in the public version.

## Conservative Option

If this repository contains only newly written wrapper scripts, evaluation rules, and analysis scripts, a standard open-source license may be possible.

If any original-author code is copied or modified, the public repository should preserve the original license and attribution requirements.

## Practical Rule

Before public release:

1. identify every file copied from another repository;
2. keep original copyright/license notices;
3. state modifications clearly;
4. avoid redistributing data or weights unless explicitly permitted.

