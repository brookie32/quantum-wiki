---
title: "Quantum amplitude estimation beyond power-of-two schedules"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.02715"
summary: "arXiv:2609.02715v1 Announce Type: new Abstract: Non-adaptive quantum amplitude estimation (QAE) fixes its Grover depths in advance, so every circuit can run in parallel, but it has so far needed more "
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02715v1 Announce Type: new Abstract: Non-adaptive quantum amplitude estimation (QAE) fixes its Grover depths in advance, so every circuit can run in parallel, but it has so far needed more queries than the best adaptive methods. We show that most of this gap comes from two conventional choices: subspace-based post-processing and power-of-two depth ladders. We replace the first by the exact maximum-likelihood estimate, one matrix multiplication per batch of estimates, and the second by a geometric ladder with ratio r approx 1.45. The result is a fully parallel, deterministic-schedule estimator with total query complexity 2.8-3.1/arepsilon at 95% confidence for target errors from 3.5imes 10^{-3} to 10^{-6}. This matches the average-case complexity of chebAE, the best benchmarked adaptive method, within statistical uncertainty (with the lower point estimate at every scale tested), beats its maximum-observed complexity by 1.6imes, and needs a maximum sequential depth of only 0.21/arepsilon against chebAE's 2.9/arepsilon. Relative to csAE, the best non-adaptive benchmark, the constants improve by 30-35% at 95% and 1.5-1.7imes at 99% confidence. The optimal ratio has a simple origin. Doubling is the fastest depth growth at which the data can still tell neighboring candidate values apart, so power-of-two ladders sit at the edge of confusion and must buy reliability with extra shots; a slightly denser ladder checks every scale redundantly. An error-probability analysis reproduces the measured failure rates and locates the optimum. The likelihood formulation extends directly to noise-aware estimation, and uniformly scaling the capped ladder covers the depth-limited regime, realizing the optimal trade-off M N_{tot} approx (0.4-0.6)/arepsilon^2 within sim 1.1imes of the schedule's Cramer-Rao limit.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.02715) | 2026-09-03
