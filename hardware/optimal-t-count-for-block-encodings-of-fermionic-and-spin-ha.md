---
title: "Optimal T-Count for Block Encodings of Fermionic and Spin Hamiltonians"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.11153"
summary: "arXiv:2609.11153v1 Announce Type: new Abstract: We determine the non-Clifford T-gate cost of constructing block encodings of structured fermionic and spin Hamiltonians in a unitary Clifford+T model, w"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.11153v1 Announce Type: new Abstract: We determine the non-Clifford T-gate cost of constructing block encodings of structured fermionic and spin Hamiltonians in a unitary Clifford+T model, when arbitrarily many clean ancillas and unrestricted block-encoding subnormalization are allowed, but without mid-circuit measurements or classical feed-forward. Our main technical tool is an ancilla-compression theorem: any block encoding of an n-qubit operator with a clean ancillas and at most s T gates can be compressed to use at most min{a,n+2s} ancillas, without increasing the absolute error or T-count. For general second-quantized Hamiltonians with bounded one- and two-body coefficients, at operator-norm block-encoding error epsilon, a volume-covering argument combined with circuit counting gives the worst-case lower bound Omega(n^2sqrt{log(n^4/epsilon)}), matching the existing upper bound at fixed precision. For the bond-dependent Kitaev honeycomb family on n spins, we obtain independent lower bounds Omega(n) from stabilizer nullity and Omega(log(1/epsilon)) from one-qubit state preparation, established using different Hamiltonian instances. Together with an explicit LCU construction, they give the tight worst-case scaling Theta(n+log(1/epsilon)). As an application, we evaluate the T-count of a Hamiltonian simulation circuit based on quantum singular value transformation, with each block-encoding query compiled separately. When phase synthesis and controlled queries add at most constant-factor overhead, the simulation T-count scales as the query count times the optimal T-count per query.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.11153) | 2026-09-11
