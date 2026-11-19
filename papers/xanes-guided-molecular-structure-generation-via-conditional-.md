---
title: "XANES-Guided Molecular Structure Generation via Conditional Diffusion and Forward Spectral Prediction"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.23725"
summary: "arXiv:2611.23725v1 Announce Type: new Abstract: Reconstructing complete molecular structures from X-ray absorption near-edge structure (XANES) spectra remains challenging because the spectra primarily"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23725v1 Announce Type: new Abstract: Reconstructing complete molecular structures from X-ray absorption near-edge structure (XANES) spectra remains challenging because the spectra primarily encode local chemical environments, with overlapping contributions from multiple absorbing sites. Here, we develop an inverse-forward framework combining XANES-conditioned diffusion-based molecular structure generation with forward spectral prediction for candidate selection. The inverse model generates atomic species, bond connectivity, and three-dimensional coordinates from C, N, and O K-edge XANES, given only the total atom count without molecular formulas or element-specific atom counts. Combining all three absorption edges substantially improves structural recovery, achieving a best-of-10 exact-match rate of 56.6% across 2,888 test molecules. The generated candidates also reproduce functional groups and structural motifs, achieving a macro-averaged F1 score of 0.951 across 21 categories. Ranking candidates by agreement between input and forward-predicted spectra increases the exact-match rate from 24.3% for unranked top-1 selection to 43.9%. This spectral-consistency criterion also enables atom count estimation, identifying the correct count for 65.6% of molecules among seven tested values. Application to experimental spectra yields an exact structural match for imidazole and recovers characteristic functional groups in two additional molecules, while revealing limitations due to simulation-experiment spectral discrepancies. These findings establish an inverse-forward approach for reconstructing whole-molecule structures from complementary element-specific XANES information.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.23725) | 2026-11-19
