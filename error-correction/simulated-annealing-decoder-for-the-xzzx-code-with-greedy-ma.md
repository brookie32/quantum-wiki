---
title: "Simulated-annealing decoder for the XZZX code with greedy-matching initialization"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.17837"
summary: "arXiv:2509.17837v3 Announce Type: replace Abstract: The XZZX code is a variant of the surface code tailored to address biased noise in realistic quantum devices. We propose a simulated annealing (SA) "
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2509.17837v3 Announce Type: replace Abstract: The XZZX code is a variant of the surface code tailored to address biased noise in realistic quantum devices. We propose a simulated annealing (SA) decoder for the XZZX code. Our SA decoder is amenable to parallelization because its Markov chain Monte Carlo updates are simple and local. To initialize SA, we use a recovery configuration produced by our greedy-matching decoder. Although Z-biased noise is commonly assumed in realistic quantum devices, we instead focus on Y-biased noise. Under Y-biased noise, the minimum-weight perfect matching (MWPM) decoder becomes suboptimal because it cannot take into account the fact that a Y error contains both X and Z components on the same qubit. Our numerical simulations for the code capacity noise model, where only data qubits suffer errors, show that our SA decoder achieves higher accuracy than the MWPM decoder. They also show that, under moderately Y-biased noise, our SA decoder achieves accuracy comparable to that of a decoder based on IBM ILOG CPLEX Optimizer (CPLEX), which uses integer programming to find a minimum-energy error configuration consistent with the measured syndrome. In our greedy-matching decoder, we randomize the tie breaking among equal-weight pairs. This randomness generates a variety of initial configurations for SA, which improves the convergence of our SA decoder. These results suggest that combining SA with our greedy-matching initializer is a promising approach to decoding the XZZX code under Y-biased noise in the code capacity noise model.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.17837) | 2026-08-17
