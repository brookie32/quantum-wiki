---
title: "The ZZ feature map induces a signless Laplacian metric: a closed-form classical surrogate for quantum kernel regression"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.29422"
summary: "arXiv:2608.29422v1 Announce Type: new Abstract: Quantum kernel methods lose their advantage over classical kernels once the encoding bandwidth is tuned, and bandwidth-tuned quantum kernels have been s"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.29422v1 Announce Type: new Abstract: Quantum kernel methods lose their advantage over classical kernels once the encoding bandwidth is tuned, and bandwidth-tuned quantum kernels have been shown to resemble radial basis function kernels closely. The analytical support for that observation rests on separable encoding circuits and captures entangling circuits only qualitatively. We close this gap for the ZZ feature map. We prove that in the small-bandwidth regime the induced kernel is, to leading order, an anisotropic Gaussian kernel with metric M = I + pi^2 Q, where Q is the signless Laplacian of the entanglement graph, and that the quadratic structure persists at every circuit depth as a pullback of the Fubini-Study metric. The anisotropy depends entirely on a phase convention: under the unshifted convention the metric is the identity irrespective of entanglement, which explains the isotropic resemblance previously reported. The derivation is verified against direct simulation for path, cycle and complete entanglement graphs, with relative error below 10^-3. The corresponding classical kernel requires no fitted parameters and no quantum simulation. Compared with the quantum kernel across two near-infrared spectroscopic benchmarks, four targets, five preprocessing pipelines and 100 resampled splits per cell, the paired 95% bootstrap interval contains zero in 18 of 20 cells, the typical relative difference in test error is 2.7%, and the two families select the same preprocessing pipeline in 96% of splits. The regime in which the reduction fails begins at the same bandwidth on both datasets and adds no robust predictive value: restricting the grid to the classical regime improves mean test error by 3.8%, a gain that an equally large random restriction does not reproduce. The quantum circuit can thus be removed without detectable predictive loss, and we can state precisely which classical kernel it was computing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.29422) | 2026-09-01
