---
title: "Balanced Routing for Symmetric Quantum Circuits"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.06072"
summary: "arXiv:2608.06072v1 Announce Type: new Abstract: Mapping quantum programs to restricted physical chips requires SWAP operations, incurring depth and error penalties. In symmetric programs, this routing"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.06072v1 Announce Type: new Abstract: Mapping quantum programs to restricted physical chips requires SWAP operations, incurring depth and error penalties. In symmetric programs, this routing overhead breaks theoretical symmetry because identical logical roles experience unequal shuffling. While often attributed to hardware topology alone, we show this is a two-level phenomenon. A qubit patch's shape dictates if it can host a balanced assignment. When balance is possible, the actual imbalance is set by the logical-to-physical assignment, meaning a balanced assignment can distribute routing costs perfectly evenly at no extra depth. Through exhaustive search on a 57-qubit "heavy-hex" lattice, we prove these topological constraints. For a four-part ring, 108 of 124 connected patches admit a cost-free balanced assignment, with the 16 exceptions being star-shaped. For a six-part ring, cost-free balance is impossible on compact patches. For a fully connected four-part symmetry, balance is structurally impossible at any depth. Simulations using realistic error rates show that, relative to the worst-case concentrated assignment, balanced assignments reduce symmetry-breaking by 92.7% (95% CI [+89.8%, +95.3%]) for the raw metric and 87.0% (95% CI [+79.6%, +94.1%]) for the decoherence-corrected measure (p = 2.45 x 10^-32). Substrate error heterogeneity accounts for at most 10.8% of this effect. Notably, switching to the compiler's highest generic optimization level did not yield a statistically significant change in routing imbalance, highlighting the need for targeted symmetry-aware passes. When patch geometry permits, routing imbalance is a compiler choice rather than a hardware limitation. Thus, symmetry-aware assignment should be a primary objective for compiler optimization and chip design.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.06072) | 2026-08-07
