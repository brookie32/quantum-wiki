---
title: "Hamiltonian Eigenvalue Transformation by Tridiagonal Gadgets"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03295"
summary: "arXiv:2610.03295v1 Announce Type: new Abstract: An analog device implements a local Hamiltonian H, but a polynomial P (H) is in general not local, so the device cannot implement it. We carry P (H), to"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03295v1 Announce Type: new Abstract: An analog device implements a local Hamiltonian H, but a polynomial P (H) is in general not local, so the device cannot implement it. We carry P (H), to any prescribed accuracy, as the action of a single time-independent local Hamiltonian on an explicitly described invariant subspace. Short chains of ancilla qubits are attached to H. A chain of 2m sites has a unique isolated eigenvalue that is an analytic function of the input vanishing to order exactly 2m, because the input must cross the chain and come back before it can shift the energy at the far end. Chains of different lengths therefore form a triangular family, and a weighted sum of them reproduces a prescribed polynomial term by term. Even chains give the even part and odd chains the odd part, so any polynomial is reached. We prove uniqueness, analyticity and coefficient bounds uniform in the chain length for inputs H of norm below any r < 1. Where the circuit model pays degree 2l in 2l sequential oracle calls, the result here is one Hamiltonian of locality two more than that of H, which pays the degree in O(l^2 + log2^(1/eps)) ancillas and in energy scale. As an application we filter a marked eigenstate of a local Hamiltonian. Composing a synthesised square along the Chebyshev doubling identity works, but its energy scale grows quasi-polynomially with the degree. Iterating instead the exact eigenvalue branch of the two-site chain k times gives a filter on k + 1 ancilla qubits whose error decays geometrically in k, at an energy scale polynomial in the inverse passband width and independent of k, the locality growing by one per stage. In adiabatic optimisation with a rank-one driver, the construction replaces that non-local driver, by a Hamiltonian with O(log n) ancillas and O(log n)- body terms, at an energy scale polynomial in n. Simulations including every ancilla reproduce the spectrum of the ideal algorithm.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03295) | 2026-10-05
