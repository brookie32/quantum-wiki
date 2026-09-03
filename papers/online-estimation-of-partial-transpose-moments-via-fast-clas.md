---
title: "Online Estimation of Partial Transpose Moments via Fast Classical Updates"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.01433"
summary: "arXiv:2605.01433v2 Announce Type: replace Abstract: Partial-transpose (PT) moments are among the most practically relevant nonlinear quantities accessible from local Pauli classical shadows, because t"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2605.01433v2 Announce Type: replace Abstract: Partial-transpose (PT) moments are among the most practically relevant nonlinear quantities accessible from local Pauli classical shadows, because they directly underpin mixed-state entanglement certification and recent PT-moment-based phase diagnostics. The online framework of Marso et al. rewrote the exact PT-moment statistic into a fixed-memory recurrence that updates a small collection of accumulated matrices after each new shadow snapshot. Its update cost is independent of the shot number, but each step treats the incoming partially transposed snapshot as a generic dense matrix. Therefore, the arithmetic cost scales cubically with the dimension of the Hilbert space. We show that the same estimator can be updated exactly in subcubic time per shot while retaining the same memory. The key point is that the accumulated matrices become dense, but the fresh partially transposed snapshot still factorizes into local factors. Right-multiplication by that factorized snapshot can therefore be executed by exact column-pair sweeps. For the second PT moment, we further optimize the process by utilizing a Pauli basis update.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.01433) | 2026-09-03
