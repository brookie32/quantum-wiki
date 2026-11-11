---
title: "Divide-and-Conquer Neural Network Surrogates for Quantum Sampling: Accelerating Markov Chain Monte Carlo in Large-Scale Constrained Optimization Problems"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.20701"
summary: "arXiv:2604.20701v2 Announce Type: replace Abstract: Quantum-enhanced Markov chain Monte Carlo (MCMC) [D.~Layden mbox{extit{et al.}},href{https://www.nature.com/articles/s41586-023-06095-4} {Nature 619"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2604.20701v2 Announce Type: replace Abstract: Quantum-enhanced Markov chain Monte Carlo (MCMC) [D.~Layden mbox{extit{et al.}},href{https://www.nature.com/articles/s41586-023-06095-4} {Nature 619, 282--287 (2023)}] is a promising way to use quantum-circuit samples as MCMC proposals to improve sampling efficiency. On the other hand, many practical problems are large-scale and constrained, making it difficult to construct efficient proposal distributions in classical methods and slowing down MCMC mixing. In this work, we propose a divide-and-conquer neural network surrogate framework for quantum sampling to accelerate MCMC under fixed Hamming weight constraints. Our method divides the interaction graph for an Ising problem into subgraphs, generates samples using QAOA for those subproblems with an XY mixer, and trains neural network surrogates conditioned on the Hamming weight to provide proposal distributions for each subset while preserving the constraint. In numerical experiments of Boltzmann sampling on 3-regular graphs, our method consistently accelerated mixing as the system size N increased, with average improvements in the autocorrelation decay rate constant by speedup factors of about mbox{14.0} and mbox{7.7} over local and global Kawasaki dynamics, respectively. We also applied the method to an MNIST feature mask optimization problem with N=784, obtaining faster energy convergence and a classification accuracy 2.03 percentage points higher than that of global Kawasaki dynamics after 50 MCMC steps. These numerical results support the usefulness of surrogate proposals with a divide-and-conquer strategy for large-scale constrained sampling and finite-step optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.20701) | 2026-11-11
