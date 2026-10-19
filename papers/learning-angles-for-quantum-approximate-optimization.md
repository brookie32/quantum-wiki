---
title: "Learning angles for quantum approximate optimization"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.23296"
summary: "arXiv:2610.23296v1 Announce Type: new Abstract: The Quantum Approximate Optimization Algorithm (QAOA) and its variants are leading algorithms to help solve challenging combinatorial optimization probl"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.23296v1 Announce Type: new Abstract: The Quantum Approximate Optimization Algorithm (QAOA) and its variants are leading algorithms to help solve challenging combinatorial optimization problems. QAOA maps these problems to Ising Hamiltonians such that their ground state is the desired solution. Candidate solutions are then drawn from a variational quantum circuit. The performance of QAOA hinges on a set of variational angles. However, finding good angles is an instance-specific and computationally expensive non-convex classical optimization task. Here, we learn the mapping from the problem instance to high-quality QAOA angles. Our learned models replace the per-instance optimization, that we call the solver, with a single forward pass that is several orders of magnitude faster than the solver with a near identical quality. Our models further generalize to unseen topologies such as Barabasi-Albert and 2D grid graphs. Experiments on quantum hardware confirm that QAOA samples with angles produced by our open-source models are indistinguishable from solver angles. Crucially, models sensitive to the topology of the problem instance increase the quality of the QAOA angles. Our work amortizes a major bottleneck in QAOA by an up-front data generation and training cost. Importantly, this cost can be amortized over time in settings where many similar problems are optimized on a regular basis, as is often the case in applications for industry.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.23296) | 2026-10-19
