---
title: "Diagonalizing large-scale quantum many-body Hamiltonians using variational quantum circuit and tensor network"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2508.06159"
summary: "arXiv:2508.06159v3 Announce Type: replace Abstract: Exact diagonalization (ED) provides complete access to many-body eigenenergies and eigenstates, yet its exponential cost confines it to small system"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2508.06159v3 Announce Type: replace Abstract: Exact diagonalization (ED) provides complete access to many-body eigenenergies and eigenstates, yet its exponential cost confines it to small systems. We propose tensor network variational diagonalization (TNVD), which encodes the full eigenenergy spectrum in a matrix product state (MPS) while representing the corresponding eigenstates via a finite depth variational quantum circuit (VQC) acting on product states. TNVD thereby reduces diagonalization complexity from exponential to polynomial in system size N. For the quantum Ising chain, TNVD accurately reproduces eigenenergies for Nleq 16 and, at sizes inaccessible to ED such as N=100, directly samples them from a single MPS encoding all 2^N levels. A random label control shows that this compact N-site representation depends on how the eigenenergies are organized in label space. TNVD further reveals that, at their integrable limits, the random field Ising and XXZ chains show comparable level spacing ratios and mean eigenstate entanglement entropies but markedly different Schmidt spectrum decay. This difference exposes distinct eigenstate entanglement structures that govern their classical simulability and the difficulty of finite depth quantum circuit preparation. Our work establishes TNVD as a scalable full spectrum diagonalization framework and its VQC as a quantum route to volume-law-entangled eigenstates that challenge efficient classical simulation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2508.06159) | 2026-09-01
