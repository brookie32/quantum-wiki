---
title: "Meta-learning of Gibbs states for many-body Hamiltonians with applications to Quantum Boltzmann Machines"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2507.16373"
summary: "arXiv:2507.16373v3 Announce Type: replace Abstract: The preparation of quantum Gibbs states is a fundamental challenge in quantum computing, essential for applications ranging from modeling open quant"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2507.16373v3 Announce Type: replace Abstract: The preparation of quantum Gibbs states is a fundamental challenge in quantum computing, essential for applications ranging from modeling open quantum systems to quantum machine learning. Building on the Meta-Variational Quantum Eigensolver framework proposed by Cervera-Lierta et al. and a problem-driven ansatz design, we introduce two meta-learning algorithms: Meta-Variational Quantum Thermalizer (Meta-VQT) and Neural Network Meta-VQT (NN-Meta VQT) for efficient thermal state preparation of parametrized Hamiltonians on Noisy Intermediate-Scale Quantum (NISQ) devices. Meta-VQT utilizes a fully quantum ansatz, while NN Meta-VQT integrates a quantum--classical hybrid architecture. Both use collective optimization over a finite set of training parameter values to prepare approximate Gibbs states at held-out parameter values within the sampled parameter domain. We validate our methods on Transverse Field Ising Models (TFIM) with up to eight qubits and on a two-qubit Heisenberg model with all field terms. Within these finite-size benchmarks, the trained models accurately prepare thermal states at test points inside the training interval. For the six and eight qubit cases of TFIM, meta-learned parameters when combined with appropriately designed ansatz serve as warm-start initializations, significantly outperforming random initializations in the optimization tasks. Furthermore, a 3 qubit Kitaev ring example showcases our algorithm's effectiveness across finite-temperature crossover regimes. Finally, we apply our algorithms to train a Quantum Boltzmann Machine (QBM) on a 2-qubit Heisenberg model with all field terms, achieving enhanced training efficiency, improved Gibbs state accuracy, and a 30-fold runtime speedup over existing techniques such as variational quantum imaginary time (VarQITE)-based QBM highlighting the practicality of meta-algorithm-based QBMs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2507.16373) | 2026-10-23
