---
title: "Beyond Quantum Advantage: Improved Classical Algorithms for the Binary Paint Shop Problem"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.00607"
summary: "arXiv:2604.00607v3 Announce Type: replace Abstract: The binary paint shop problem (BPSP) is an APX-hard optimization problem in which, given n car models that occur twice in a sequence of length 2n, t"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2604.00607v3 Announce Type: replace Abstract: The binary paint shop problem (BPSP) is an APX-hard optimization problem in which, given n car models that occur twice in a sequence of length 2n, the objective is to find a colouring sequence such that each car model pair is painted differently while minimizing the number of times the paint is swapped along the sequence. A recent classical heuristic, known as the recursive star greedy (RSG) algorithm, is conjectured to achieve an expected paint swap ratio of 0.361, thereby outperforming the Quantum Approximate Optimization Algorithm (QAOA) with circuit depth p=7. Since the performance of the QAOA with logarithmic circuit depth is instance independent, the average paint swap-ratio is upper-bounded by the QAOA. We provide an improved upper-bound of the BPSP by extending the QAOA to depth p=17, outputting an expected paint swap ratio of 0.334 via an exact computation while numerical extrapolation suggests a further reduction to a value of 0.295. To provide hardware-relevant comparisons, we additionally implement the BPSP on a D-Wave Quantum Annealer Advantage 2, obtaining a minimum paint swap ratio of 0.329. Given that the QAOA with logarithmic circuit depth does not exhibit a quantum advantage for sparse optimization problems such as the BPSP, this implies the existence of a classical algorithm that outperforms both the RSG algorithm and logarithmic depth QAOA. We provide numerical evidence that the Mean-Field Approximate Optimization Algorithm (MF-AOA) is one such algorithm, yielding a paint swap ratio of approximately 0.280 beating all known classical and quantum algorithms for the BPSP.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.00607) | 2026-08-20
