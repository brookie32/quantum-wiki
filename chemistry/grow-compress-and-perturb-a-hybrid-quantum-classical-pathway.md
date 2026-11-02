---
title: "Grow, Compress, and Perturb: A Hybrid Quantum-Classical Pathway to Scalable Quantum Chemistry on Quantum Computers"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.40561"
summary: "arXiv:2610.40561v2 Announce Type: replace Abstract: While Variational Quantum Eigensolver (VQE) variants are among the leading candidates for electronic structure calculations on quantum computers, gr"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.40561v2 Announce Type: replace Abstract: While Variational Quantum Eigensolver (VQE) variants are among the leading candidates for electronic structure calculations on quantum computers, gradient-based operator selection limits their scalability. To solve this, we introduce the Hamiltonian-gradient-free VULCAN (Variational Upbuilding, Layered Compression, Adaptive N-body perturbation) layered VQE framework. Our method dynamically generates ansatz operators using Variational Double Bracket Flow (VDBF) equations. Combined with a linearly scaling minimal complete pool, it creates a pool 4-12 times smaller than QEB (Qubit-Excitation-Based) pools. By appending entire layers simultaneously, Hamiltonian gradient measurements are completely eliminated. Circuit depth is managed via a grow-then-compress scheme using efficient state-overlap measurements, and qubit requirements are reduced by projecting the Hamiltonian onto a dominant-determinant subspace. Using high-performance emulation up to 32 logical qubits, we achieve chemical accuracy at just 5-20% of the measurement cost of batched ADAPT-VQE for hydrogen chains, BeH2 and H2O. For the 32-qubit C3H6, where batched ADAPT-VQE does not reach chemical accuracy, a single VULCAN layer combined with a GPU-accelerated stochastic Epstein-Nesbet (ENPT2) correction does. This stochastic ENPT2 post-processing step enables early termination at chemical accuracy.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.40561) | 2026-11-02
