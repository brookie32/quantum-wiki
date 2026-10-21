---
title: "Bidirectional Path Integral Monte Carlo Simulation of Quantum Circuits"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.27768"
summary: "arXiv:2610.27768v1 Announce Type: new Abstract: We propose an approximate classical algorithm for estimating quantum circuits' transition amplitudes, langle Psi_f | hat{U} | Psi_0 rangle, based on Mon"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.27768v1 Announce Type: new Abstract: We propose an approximate classical algorithm for estimating quantum circuits' transition amplitudes, langle Psi_f | hat{U} | Psi_0 rangle, based on Monte Carlo sums over bidirectionally sampled Feynman paths. The algorithm generates Feynman paths, i.e., sequences of intermediate computational basis states, by combining information from random walks initiated at both the input and output states, Psi_0 and Psi_f, respectively. It further combines this bidirectional approach with Multiple Importance Sampling, a powerful variance reduction technique that avoids variance peaks caused by divisions by the very low sampling probabilities associated with hard to reach paths. Empirical data demonstrate the superior convergence rate exhibited by the bidirectional algorithm over a unidirectional, forward-only sampling approach. This superiority is due to the effectiveness of the proposed algorithm in finding and weighting paths with non-zero amplitude in an extremely sparse path space. Sum of paths algorithms exhibit very favourable space complexity. Monte Carlo replaces exhaustive enumeration of the exponentially large path space by stochastic sampling, the computational cost being determined by the variance of the estimator. This work demonstrates these two features by presenting results on very large quantum circuits, with up to 4096 qubits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.27768) | 2026-10-21
