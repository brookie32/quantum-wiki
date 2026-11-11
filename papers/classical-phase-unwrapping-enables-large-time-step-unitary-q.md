---
title: "Classical phase unwrapping enables large-time-step unitary quantum Krylov subspace diagonalization"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.14214"
summary: "arXiv:2611.14214v1 Announce Type: new Abstract: For computing molecular energies on early fault-tolerant hardware, unitary quantum Krylov subspace diagonalization (UQKSD) avoids both the deep circuits"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.14214v1 Announce Type: new Abstract: For computing molecular energies on early fault-tolerant hardware, unitary quantum Krylov subspace diagonalization (UQKSD) avoids both the deep circuits of quantum phase estimation and the Pauli-term sampling of variational methods by extracting the energies from a projected real-time propagator. At a small time step au, nearly linearly dependent Krylov vectors make the overlap matrix ill-conditioned. Our tests at fixed total evolution time show that additional Krylov vectors then add no accuracy, while the thresholded energy becomes increasingly sensitive to the choice of cutoff. A larger time step improves the conditioning and reduces the Krylov dimension M needed for a target accuracy, but the energies are then known only modulo 2pi/au. We present Classical Unwrapping for Resolving Eigenvalues (CURE-QKSD), a classical post-processing method that leaves the UQKSD circuits and generalized eigenvalue problem unchanged and recovers the missing multiples of 2pi/au from phase-consistency landscapes of one or, when needed, two UQKSD runs. In noiseless tests on six molecules with 12--20 qubits, all 28 targeted energies are recovered in their aliased regimes with final errors of at most 1.1imes10^{-7}~Ha. Under Gaussian noise with sigma=10^{-4}, the median error of the ground or first excited state reaches chemical accuracy at large aliased time steps with M=20--65, whereas uncorrected principal-branch energies are off by 0.7--115~Ha. CURE-QKSD therefore makes aliased time steps usable for UQKSD calculations with smaller, better-conditioned Krylov bases.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.14214) | 2026-11-11
