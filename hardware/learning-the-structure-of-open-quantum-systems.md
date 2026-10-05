---
title: "Learning the structure of open quantum systems"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.30358"
summary: "arXiv:2606.30358v2 Announce Type: replace Abstract: We design an algorithm for learning the coefficients of an n-qubit constant-local Lindbladian to arepsilon error with O(g d^2 log(n) / arepsilon^2) "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2606.30358v2 Announce Type: replace Abstract: We design an algorithm for learning the coefficients of an n-qubit constant-local Lindbladian to arepsilon error with O(g d^2 log(n) / arepsilon^2) total evolution time, where g is the single-site energy and d is the (approximate) degree of the interaction graph. Though Lindbladians present new challenges not present in the special case of Hamiltonians, our algorithm achieves the suite of desiderata attained by state-of-the-art Hamiltonian learning algorithms: (1) it uses non-adaptive, ancilla-free randomized Pauli measurement circuits with a time resolution of only Theta(1/g); (2) it works without knowledge of the structure of the unknown Lindbladian; (3) it depends on a smooth form of degree, thereby supporting the learning of quasi-local and power-law Lindbladians. Moreover, we prove a lower bound showing that our algorithm is optimal in each parameter up to logarithmic factors. Our algorithm is a simple iterative method, where the objective function consists of Fourier coefficients of the Lindbladian restricted to few-site regions. Its analysis identifies the difficulty unique to open systems, which we call "confusing" terms. For settings where the "confusion" is limited, the performance of the algorithm improves. We demonstrate this for the case of structure learning of Hamiltonians from access to real-time evolution, where we obtain a new algorithm that is significantly simpler than previous work. In addition, using the same iterative method, we design the first efficient algorithm for structure learning Hamiltonians from high-temperature Gibbs states.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.30358) | 2026-10-05
