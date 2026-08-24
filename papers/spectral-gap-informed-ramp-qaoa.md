---
title: "Spectral Gap Informed Ramp QAOA"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24580"
summary: "arXiv:2604.24580v3 Announce Type: replace Abstract: A challenge with the Quantum Approximate Optimisation Algorithm (QAOA), and variational algorithms in general, is finding good variational parameter"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2604.24580v3 Announce Type: replace Abstract: A challenge with the Quantum Approximate Optimisation Algorithm (QAOA), and variational algorithms in general, is finding good variational parameters, a task which in itself can be NP-hard. Recent work has sought to de-variationalise QAOA by picking well-informed guesses for the variational parameters. The Linear Ramp QAOA (LR-QAOA) achieves this by using parameter schedules inspired by the quantum adiabatic algorithm. In this work, we propose Spectral Gap Informed Ramp QAOA (SGIR-QAOA), a new QAOA variant that incorporates spectral gap information from an adiabatic Hamiltonian, with the QAOA mixer Hamiltonian as the initial Hamiltonian, to construct smooth parameter schedules. SGIR-QAOA performs slow evolution where the spectral gap of the adiabatic Hamiltonian is small. We show that SGIR-QAOA has performance improvements over the LR-QAOA on Grover's problem at constant depth and that SGIR-QAOA requires shorter depths to achieve the same optimal solution probability. We then show that these performance benefits extend to a problem with potential practical applications - the Maximum Independent Set (MIS) problem. Finally, we demonstrate the scalability of the SGIR-QAOA method using extrapolated spectral gap information for scales that the spectral gap cannot be exactly evaluated, and show that the advantage appears to persist under mild depolarising noise.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24580) | 2026-08-24
