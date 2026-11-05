---
title: "Subtle Energy Corrections Reshape Condensed-Phase Property Predictions from a Machine-Learning Interatomic Potential"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.06109"
summary: "arXiv:2611.06109v1 Announce Type: new Abstract: Accurate reproduction of electronic-structure labels by machine-learning interatomic potentials does not necessarily ensure reliable condensed-phase pro"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06109v1 Announce Type: new Abstract: Accurate reproduction of electronic-structure labels by machine-learning interatomic potentials does not necessarily ensure reliable condensed-phase properties. We investigate the effects of basis-set superposition error (BSSE) and an explicit Axilrod-Teller-Muto (ATM) three-body dispersion contribution on molecular-liquid predictions. Starting from MACELES-OFF, we fine-tune a baseline potential at the omegaB97M-V/def2-TZVPD level. A separate branch learns counterpoise (CP) energy and force corrections with the baseline frozen, while a D4-parametrized ATM term is added during molecular-dynamics inference. Mean atom-normalized CP and ATM contributions are 0.222 and 0.205 meV/atom, respectively, for the analyzed SPICE2 configurations from OMol25. We compare baseline, CP-only, ATM-only, and CP + ATM variants for 39 organic liquids. Relative to baseline, the mean system-wise density changes are -1.17%, -10.38%, and -11.93% for CP-only, ATM-only, and CP + ATM, respectively; the corresponding enthalpy-of-vaporization changes are -2.79%, -14.74%, and -18.32%. For the 11 liquids with experimental self-diffusion data, the mean self-diffusion changes are +17.66%, +203.02%, and +230.36%. Both corrections thus lower density and enthalpy of vaporization while increasing molecular mobility on average. ATM dominates these changes, while CP provides a smaller contribution; their combination yields the largest average shifts. These results show that corrections with sub-meV/atom mean values on the analyzed configurations can substantially reshape the predicted structural, thermodynamic, and transport properties of molecular liquids.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.06109) | 2026-11-05
