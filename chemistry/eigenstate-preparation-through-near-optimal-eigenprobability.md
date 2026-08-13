---
title: "Eigenstate Preparation Through Near-Optimal Eigenprobability Filtering"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.12297"
summary: "arXiv:2608.12297v1 Announce Type: new Abstract: Quantum simulation is expected to be a main application of quantum computers with realistic utility in quantum chemistry, materials science and beyond. "
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.12297v1 Announce Type: new Abstract: Quantum simulation is expected to be a main application of quantum computers with realistic utility in quantum chemistry, materials science and beyond. However, preparing excited or general eigenstates is a central challenge, particularly when the desired eigenvalue is not known in advance, or when the overlap with the initial state is insufficient. We introduce the Dominant Eigenstate Filtering via Eigenprobability Amplification and Thresholding (DEFEAT) algorithm that identifies and filters the eigenstate with the largest overlap with the supplied initial state. Our key observation is that we do not need prior knowledge of the target eigenvalue, as we construct efficient twirling superoperators that map initial states to eigenprobability density operators rho, diagonal in the Hamiltonian eigenbasis and encoding its spectral weights, alongside its block-encoding implementation. Our crucial innovation is the quadratic amplification of probabilities via the factorisation rho=rho_{rm sqrt}^aggerrho_{rm sqrt}, analogous to the recently introduced sum-of-squares spectral amplification (SOSSA), which we use here to amplify the separation between dominant and subdominant components. Thresholding then yields the dominant-eigenstate projector. Compared with conventional phase estimation, DEFEAT improves the dependence on the overlap with the initial state while requiring substantially fewer ancillary qubits. We prove that the query complexity of the filtering step is optimal up to logarithmic factors and establish a complementary lower bound for eigenstate preparation under purified query access to rho. We validate in numerical simulations that the convergence rate of DEFEAT matches our theoretical results. Our results provide a general eigenvalue-agnostic primitive for dominant eigenstate filtering and preparation, and for estimating properties of dominant eigenstates.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.12297) | 2026-08-13
