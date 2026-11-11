---
title: "Pool-free, residual-triggered ansatz growth for variational imaginary-time evolution: when a fixed operator order beats adaptive screening"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13998"
summary: "arXiv:2611.13998v1 Announce Type: new Abstract: Adaptive variational algorithms such as ADAPT-VQE and AVQITE screen an operator pool at every growth step, and ADAPT-VQE also re-optimizes all parameter"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13998v1 Announce Type: new Abstract: Adaptive variational algorithms such as ADAPT-VQE and AVQITE screen an operator pool at every growth step, and ADAPT-VQE also re-optimizes all parameters. We study a pool-free alternative for variational imaginary-time evolution (VITE). The layers are fixed in advance by nested commutators of the Hamiltonian, grouped by symmetry and particle number, and the next layer is appended when the relative McLachlan residual exceeds a threshold. On five non-integrable systems (the mixed-field Ising chain and tori, and stretched H_4), this dynamic VITE reaches a relative error of 10^{-4} with 1.6-5.4 times fewer circuits than the cheapest of six to eight adaptive variants, including single-Pauli-string and qubit-excitation pools and batched ADAPT-VQE. On the chain the advantage persists from 8 to 16 sites. Screening and re-optimization account for most of the adaptive methods' cost. On the spin models, a longitudinal-field scan shows that the advantage requires broken integrability, which makes adaptive screening expensive. The advantage is lost on transverse-field Ising models, at tight targets (relative error 10^{-6}) and where the schedule front-loads weak layers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13998) | 2026-11-11
