---
title: "On the Multi-User Security of CSI-FiSh with Tight Reductions"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2216"
summary: "The security of isogeny-based signatures is almost exclusively studied in the single-user setting, leaving a gap for realistic multi-user deployments. This gap is especially crucial for CSI-FiSh, wher"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

The security of isogeny-based signatures is almost exclusively studied in the single-user setting, leaving a gap for realistic multi-user deployments. This gap is especially crucial for CSI-FiSh, where the small challenge space and parameter sensitivity directly impacts security estimates. We address the multi-user security of CSI-FiSh and obtain tight concrete classical multi-user bounds in the random-oracle model (ROM) plus generic group-action model (GGAM). Crucially, our analysis only incurs an additive degradation in the number of users rather than a multiplicative one. As a byproduct, we show that CSI-FiSh attains 125 bits of provable classical security even with 2^{46} users. We extend this analysis to preprocessing attacks, where an adversary with nation-state resources can perform offline precomputations. We capture this by extending the preprocessing security framework of Coretti et al. to ROM+GGAM and obtain concrete multi-user bounds for CSI-FiSh with preprocessing. Finally, we address the multi-user security of CSI-FiSh in the quantum random-oracle model and obtain results in the algebraic group action model which also avoids this multiplicative loss. This gives a unified concrete security treatment of plain CSI-FiSh in the deployment regimes where multi-user and preprocessing effects are unavoidable.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2216) | 2026-09-25
