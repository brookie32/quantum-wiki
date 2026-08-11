---
title: "A Design Space Study of Density Matrix Parameterizations for Diffusion-Based Quantum State Tomography"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.09625"
summary: "arXiv:2608.09625v1 Announce Type: new Abstract: Diffusion-based quantum state tomography (QST) has shown promising results, but all existing methods implicitly adopt a single parameterization---typica"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.09625v1 Announce Type: new Abstract: Diffusion-based quantum state tomography (QST) has shown promising results, but all existing methods implicitly adopt a single parameterization---typically Cholesky---without systematic evaluation. We present a design space study of density matrix parameterizations for diffusion QST, introducing a geometric framework based on the Jacobian Gram matrix mathbf{J}^opmathbf{J} that quantifies two competing criteria: isometric conditioning and physical constraint satisfaction. Our calibration of seven parameterizations at 2- and 3-qubit scales reveals three key findings. First, isometry and constraints are orthogonal criteria---no single parameterization optimizes both. Second, theoretical elegance does not predict geometric quality: the exponential map exhibits a spectral range of 149imes at 2 qubits and 75,658imes at 3 qubits, while simpler parameterizations remain well-conditioned. Third, geometric conditioning alone does not fully predict end-to-end performance: without classifier-free guidance (CFG), Hermitian direct outperforms Bloch despite worse local isometry; under CFG, the ranking reverses due to amplified boundary effects. End-to-end training confirms that better-conditioned parameterizations converge faster and achieve higher fidelity in the absence of CFG. We provide actionable selection guidelines to guide future QST method design.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.09625) | 2026-08-11
