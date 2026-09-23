---
title: "Machine-learned, finite temperature Fermi-operator expansions suitable for GPUs and AI-hardware"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.08523"
summary: "arXiv:2605.08523v3 Announce Type: replace Abstract: We present several finite-temperature recursive Fermi-operator expansion schemes based on the second-order spectral projection (SP2) method. Our app"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2605.08523v3 Announce Type: replace Abstract: We present several finite-temperature recursive Fermi-operator expansion schemes based on the second-order spectral projection (SP2) method. Our approach builds on a previous observation that the electronic structure problem, as formulated through a recursive SP2 expansion, can be mapped onto the architecture of a deep neural network. Using this perspective, we generalize SP2 to finite electronic temperatures by constructing machine learning models that determine optimized recursive expansion coefficients. The same approach is also applied to the prediction of the electronic entropy for fractional occupation numbers. The coefficients are trained for a specified chemical potential and electronic temperature and are not available in closed analytical form. However, by employing an appropriate affine rescaling strategy to the Hamiltonian matrix, we eliminate the need to retrain the model for different temperatures and chemical potentials. Our approach avoids explicit diagonalization and relies solely on highly optimized matrix-matrix multiplication kernels. Compared to state-of-the-art diagonalization, we achieve an order-of-magnitude speedup in the single-particle finite-temperature density matrix calculation for small and moderately sized matrices on modern GPUs and dense matrix multiply units.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.08523) | 2026-09-23
