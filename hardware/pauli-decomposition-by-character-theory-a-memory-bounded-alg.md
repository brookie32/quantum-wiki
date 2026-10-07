---
title: "Pauli Decomposition by Character Theory: A Memory-Bounded Algorithm for Qubits and Qudits"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.08299"
summary: "arXiv:2610.08299v1 Announce Type: new Abstract: Pauli decomposition underpins Trotterization, phase estimation, sparse-Hamiltonian simulation, and variational observables, at exponential naive cost. F"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.08299v1 Announce Type: new Abstract: Pauli decomposition underpins Trotterization, phase estimation, sparse-Hamiltonian simulation, and variational observables, at exponential naive cost. From the character theory of (Z_2)^n, characters hi_z(v)=(-1)^{langle v,zrangle} are the diagonal Pauli strings, so any diagonal operator is already Pauli-decomposed. A general operator still needs the shifts: each X^{otimes x} couples to a character hi_z=Z^{otimes z}, and the products X^{otimes x}Z^{otimes z} -- up to phases in {pm 1,pm i} -- form the Pauli group, the central extension of (Z_2)^nimes(Z_2)^n by that phase group fixed by the symplectic pairing. A section of that extension remains a choice: the bare products X^{otimes x}Z^{otimes z}, or the genuine operators that insert Y=iXZ at every qubit where x and z overlap. As Fourier analysis on an abelian shift-character lattice (a natural DFT), this formulation is not qubit-bound: (Z_p)^n recovers Heisenberg-Weyl qudits. The fast algorithm is the FFT for the group at hand; on (Z_2)^n that FFT is Walsh-Hadamard, at cost O(ndot 4^n). paulikit is a memory-bounded realization of that qubit transform: peak usage need not materialize the dense 2^nimes 2^n operator, unlike prior codes whose O(1) extra sits on that buffer, checked beyond a billion oscillator terms against Work-Span and bandwidth ceilings.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.08299) | 2026-10-07
