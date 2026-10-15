---
title: "Solving the traveling salesman problem on lceil log_2 (N-1)! rceil qubits with a variational quantum Kolmogorov--Arnold network: exact-gradient CVaR training and generalization over time-dependent graphs"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.22752"
summary: "arXiv:2509.22752v2 Announce Type: replace Abstract: The one-hot encoding of the traveling salesman problem (TSP) on quantum hardware needs (N-1)^2 qubits for N sites and penalty terms that dominate th"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2509.22752v2 Announce Type: replace Abstract: The one-hot encoding of the traveling salesman problem (TSP) on quantum hardware needs (N-1)^2 qubits for N sites and penalty terms that dominate the cost landscape. Permutation encodings that label every tour by its Lehmer code need only lceil log_2 (N-1)! rceil qubits and no penalty term, but variational solvers on them have reached the optimum reliably only up to six sites. Here we show how to train such a solver so that it scales to ten sites and transfers across graphs. A variational quantum Kolmogorov--Arnold network (VQKAN) generates the angles of a shallow circuit from the time and from features of the distance matrix; the circuit is trained on the conditional value at risk (CVaR) of the tour length with an exact adjoint gradient, a risk-level schedule, multi-start, small-angle initialization, and basin-hopping restarts, and the qubits are read as a Gray code so that neighbouring states are neighbouring tours. The method returns the optimal tour on every instance tested for N = 4 to 10 (symmetric polygons and asymmetric random graphs), and in 112 of 120 cases of a thirty-run repetition at N = 10 with the remaining gaps at 1% of the optimum, using 3 to 19 qubits where one-hot encoding needs 9 to 81, with as few as 10^2 measurement shots. With the distance features as inputs, one parameter set generalizes to unseen times on time-dependent graphs. An ablation identifies basin hopping as the ingredient that removes the residual local minima at N = 10, while deeper circuits do not help; controls against 2-opt, the one-hot encoding, and an N-qubit one-hot walk separate the circuit's contribution from classical post-processing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.22752) | 2026-10-15
