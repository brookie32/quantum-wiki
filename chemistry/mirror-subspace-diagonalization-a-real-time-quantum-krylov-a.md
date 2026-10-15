---
title: "Mirror subspace diagonalization: A real-time quantum Krylov algorithm with near-optimal sampling cost"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.20998"
summary: "arXiv:2511.20998v3 Announce Type: replace Abstract: Quantum Krylov algorithms are a promising approach for ground-state energy estimation on near-term quantum computers. However, their sampling cost i"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2511.20998v3 Announce Type: replace Abstract: Quantum Krylov algorithms are a promising approach for ground-state energy estimation on near-term quantum computers. However, their sampling cost is inherently high because each Hamiltonian term is measured individually. Despite various mitigation techniques, this overhead remains a bottleneck for large-scale electronic structure problems. We introduce mirror subspace diagonalization (MSD), which approaches the theoretical lower bound on the sampling cost for quantum Krylov algorithms built upon real-time evolution. MSD uses a finite-difference formula to express the Hamiltonian as a linear combination of time-evolution unitaries with symmetrically shifted timesteps, enabling efficient estimation of the Hamiltonian matrix within the Krylov subspace. By optimizing the timestep and shifting the energy spectrum, finite-difference and statistical errors are minimized simultaneously, allowing MSD to attain the sampling-cost lower bound up to a logarithmic factor. We further apply classical post-processing to infer Hamiltonian moments, which mitigate the ground-state energy error via the Lanczos scheme. Our analysis shows MSD is particularly effective when the Hamiltonian's spectral norm is much smaller than its 1-norm, as in high-accuracy molecular simulations with large basis sets and strong electronic correlations. Numerical results for various molecular models show sampling-cost reductions of roughly 10 to 10,000 times over the conventional quantum Krylov algorithm.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.20998) | 2026-10-15
