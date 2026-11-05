---
title: "Hardware Demonstration of Neural-Surrogated Quantum-Enhanced MCMC for Large-Scale Constrained Boltzmann Sampling"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.05883"
summary: "arXiv:2611.05883v1 Announce Type: new Abstract: Neural-surrogated quantum-enhanced Markov chain Monte Carlo (QeMCMC) uses neural networks trained on samples from the quantum approximate optimization a"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.05883v1 Announce Type: new Abstract: Neural-surrogated quantum-enhanced Markov chain Monte Carlo (QeMCMC) uses neural networks trained on samples from the quantum approximate optimization algorithm (QAOA) to accelerate Boltzmann sampling. A divide-and-conquer strategy extends this approach to larger systems, but independently optimizing QAOA parameters for each subproblem is costly. In this paper, we develop a hardware-efficient implementation of neural-surrogated QeMCMC and demonstrate it using an IBM Quantum Heron r2 processor. Experiments with N=144 binary variables reveal faster autocorrelation decay for appropriate subproblem sizes while exposing challenges in neural-surrogate learning for larger blocks. We then extend the demonstration to a system with N=1064, where the autocorrelation decay rate per MCMC step is approximately 5.2 and 12.3 times those of global and local Kawasaki dynamics, respectively. These results demonstrate faster autocorrelation decay in a system exceeding one thousand variables using samples generated on quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.05883) | 2026-11-05
