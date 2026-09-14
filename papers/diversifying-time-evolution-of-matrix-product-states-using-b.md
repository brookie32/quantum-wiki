---
title: "Diversifying time evolution of matrix product states using BUGs"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.12848"
summary: "arXiv:2609.12848v1 Announce Type: cross Abstract: Time evolution of tensor-network states is a central tool for studying nonequilibrium dynamics in strongly correlated quantum systems. In the past dec"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.12848v1 Announce Type: cross Abstract: Time evolution of tensor-network states is a central tool for studying nonequilibrium dynamics in strongly correlated quantum systems. In the past decade, using the time-dependent variational principle (TDVP) discretized by projector-splitting has become the gold standard for evolving matrix product states (MPS) with long-range Hamiltonians. More recently, a conceptually different class of discretizations of the TDVP, the class of Basis Update and Galerkin (BUG) integrators, has been developed within the framework of dynamical low-rank approximation, offering an alternative, more flexible approach. In this work, we formulate two BUG integrators explicitly for MPS. The BUG integrators result in "single-site" MPS integrators that are robust with respect to small singular values, avoid backward-in-time substeps, and naturally allow for the adaptive choice of bond dimensions. We consider the augmented BUG integrator of first order and the midpoint BUG integrator of second order and clarify their relation to the projector-splitting discretization of the TDVP. Using representative models of strongly correlated quantum systems, like the XY spin model with long-range interaction and two-dimensional lattice models of fermions and spins of various lengths, we perform a systematic numerical comparison between BUG and projector-splitting time discretizations of the continuous-time TDVP, focusing on scalability, numerical complexity, and accuracy. We find that BUG integrators, due to their reduced numerical cost and the flexibility of the concept, provide a competitive and, in certain regimes, advantageous alternative to the well-established time-stepping by projector-splitting in TDVP, especially in models with large local dimensions, and in cases where observables are extracted with high temporal resolution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.12848) | 2026-09-14
