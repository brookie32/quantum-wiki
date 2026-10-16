---
title: "Representation-split Carleman lattice Boltzmann with near-unit step success probability on quantum computers"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.20620"
summary: "arXiv:2610.20620v1 Announce Type: cross Abstract: The Carleman lattice Boltzmann method replaces the quadratic collision of the lattice Boltzmann equation by a linear map on a lifted state. Existing b"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.20620v1 Announce Type: cross Abstract: The Carleman lattice Boltzmann method replaces the quadratic collision of the lattice Boltzmann equation by a linear map on a lifted state. Existing block encodings of this map succeed with probability 10^{-5} to 10^{-2} per step, so that the probability of a multi-step evolution decays exponentially with the number of steps. This study develops multi-relaxation-time Carleman lattice Boltzmann, a representation split in which the Carleman-lifted collision is performed in a moment basis on the amplitude-encoded state, while streaming remains a permutation in population space. The level-2 hierarchy closes under collision but not under streaming, which generates the work of pressure, advection and stress on the momentum flux. The state therefore remains the full pair array, and the moment representation is an orthogonal change of basis of the population one, with identical dynamics and truncation error. The operator to be block encoded changes with the basis, and with it the success probability of a quantum step. In the weighted Hermite basis with the amplitude encoding f_i/sqrt{w_i}, the relaxation is a diagonal operator of norm one, and the level-2 collision stage becomes this diagonal plus a sparse coupling from products of conserved moments. A structured block encoding of this form raises the single-step success probability on the D2Q9 lattice from 10^{-2} for the best population encoding to 0.98. With the pair sector in relative coordinates and scaled, one step requires O(log^2 N) Toffoli gates and is verified by statevector simulation. The encoding and readout overhead of a T-step run is then polynomial in T and N rather than accumulating a factor p^T. For resolved flows, the remaining exponential loss in coherent multi-step Carleman lattice Boltzmann evolution is set by the non-equilibrium norm relaxed by dissipation rather than by the block encoding.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.20620) | 2026-10-16
