---
title: "Beyond Ground States: Physics-Inspired Optimization of Excited States of Classical Hamiltonians"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2507.12394"
summary: "arXiv:2507.12394v2 Announce Type: replace Abstract: We introduce excited local quantum annealing (ExcLQA), a classical, physics-inspired algorithm that extends local quantum annealing (LQA) to identif"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2507.12394v2 Announce Type: replace Abstract: We introduce excited local quantum annealing (ExcLQA), a classical, physics-inspired algorithm that extends local quantum annealing (LQA) to identify excited states of classical Ising Hamiltonians. LQA simulates quantum annealing while constraining the quantum state to remain in a product state and uses a gradient-based approach to find approximate solutions to large-scale quadratic unconstrained binary optimization problems. ExcLQA extends this framework by adding a penalty term in the cost function to target excited states, with a single hyperparameter that can be tuned via binary search to set the desired penalization level. We benchmark ExcLQA on fully connected Ising models with random interactions and on the shortest vector problem (SVP). The latter is a fundamental lattice problem underlying the security of many post-quantum cryptographic schemes, and its solution can be mapped to the first excited state of an Ising Hamiltonian. For the fully connected Ising models, we show that, on the tested instances, ExcLQA outperforms both a matrix-product-state-based method and simulated annealing. Notably, even when only a lower bound on the ground-state energy is provided, rather than the exact ground-state information required by these competing methods, ExcLQA still achieves superior performance. For the SVP, ExcLQA finds exact solutions for instances up to rank 46, and outperforms the Metropolis-Hastings algorithm in terms of solved ratio, number of shots, and approximation factor on the tested instances.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2507.12394) | 2026-08-03
