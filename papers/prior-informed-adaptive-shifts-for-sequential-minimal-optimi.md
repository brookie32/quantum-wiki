---
title: "Prior-Informed Adaptive Shifts for Sequential Minimal Optimization in Variational Quantum Eigensolvers"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.21616"
summary: "arXiv:2608.21616v1 Announce Type: new Abstract: Sequential minimal optimization methods, such as the Rotosolve and the Nakanishi-Fujii-Todo algorithm (NFT), are widely used for Variational Quantum Eig"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.21616v1 Announce Type: new Abstract: Sequential minimal optimization methods, such as the Rotosolve and the Nakanishi-Fujii-Todo algorithm (NFT), are widely used for Variational Quantum Eigensolvers (VQEs). These methods optimize one parameter direction at a time, requiring measurements at only a few locations along that direction. In the presence of measurement shot noise, however, their performance depends critically on the choice of measurement locations, and recent studies suggest that equidistant measurements are optimal. However, we often observe that equidistant measurements are not always optimal in practice. We argue that this discrepancy between theory and practice arises from the fact that two assumptions underlying previous analyses do not generally hold: (1) the absence of prior knowledge about the energy minimizer, and (2) the use of the uncertainty of the estimated energy as a proxy for optimization performance. In this paper, we develop a new theory for determining optimal measurement locations. First, we show that incorporating prior information about the minimizer is beneficial. Early in optimization, when little is known about the pivot, i.e., the current minimizer, equidistant measurements are indeed near-optimal, but as the prior belief sharpens the optimal locations move away from equidistant. Second, rather than analyzing the uncertainty of the estimated minimum energy, we study the uncertainty of the estimator of the minimizer itself, which leads to substantially different strategies. Based on this analysis, we propose Prior-informed Adaptive Shifts (PAS), a method that automatically adjusts measurement locations during optimization. Numerical experiments across different shot counts and problems validate our theoretical findings and demonstrate that PAS adaptively recovers whichever fixed shift is best in each regime without it being specified in advance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.21616) | 2026-08-25
