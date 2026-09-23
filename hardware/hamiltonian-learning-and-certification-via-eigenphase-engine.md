---
title: "Hamiltonian Learning and Certification via Eigenphase Engineering"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.26596"
summary: "arXiv:2609.26596v1 Announce Type: new Abstract: We study Hamiltonian learning for k-local Hamiltonians at large step size, using only forward time evolution at integer multiples of a fixed time interv"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.26596v1 Announce Type: new Abstract: We study Hamiltonian learning for k-local Hamiltonians at large step size, using only forward time evolution at integer multiples of a fixed time interval. For this task, our new technique, which we call eigenphase engineering, achieves Heisenberg-limited learning with a step size that is optimal up to logarithmic factors. For an unknown s-sparse Hamiltonian with fixed locality k and |H|_{op}leqLambda, our algorithm recovers its Pauli coefficients to ell_2 error arepsilon in total evolution time widetilde{O}(s/arepsilon), matching the best known scaling while allowing a near-maximal step size widetilde{Theta}(1/Lambda). As an independent contribution, we strengthen the evolution-time lower bound to Omega_k(s^{1-1/(2k)}/arepsilon), placing our algorithm within a factor widetilde{O}(s^{1/(2k)}) of being optimal. Eigenphase engineering departs from approaches based on dynamical approximation or iteratively canceling the unknown Hamiltonian. It encodes energy expectation differences in the perturbative response of eigenphases of the actual controlled evolution, then extracts them through phase estimation and high-order extrapolation. This avoids the need for polynomially shorter evolution steps as the target precision improves. A version using only single-qubit operations retains the same step size with a sqrt n overhead in ell_2 learning time for n qubits. The method also enables tolerant Hamiltonian certification and estimation of a specified Pauli coefficient, the latter without locality or sparsity assumptions. These results establish eigenphase engineering as a versatile approach to extracting Hamiltonian information with infrequent control.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.26596) | 2026-09-23
