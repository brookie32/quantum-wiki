---
title: "Quantum Folding in Chebyshev-Based Quantum Subspace Diagonalization"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.19922"
summary: "arXiv:2610.19922v1 Announce Type: new Abstract: Quantum subspace diagonalization (QSD) with a Krylov space spanned by Chebyshev polynomials of the Hamiltonian is a natural ground-state method for faul"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2610.19922v1 Announce Type: new Abstract: Quantum subspace diagonalization (QSD) with a Krylov space spanned by Chebyshev polynomials of the Hamiltonian is a natural ground-state method for fault-tolerant quantum computers, but every guarantee it offers---convergence rate, noise floor, and the cost of turning its classical output back into a physical state---is controlled by the overlap of the reference state with the true ground state, which decays exponentially with system size for any product state and non-trivial Hamiltonian. We propose quantum folding: for a system governed by a local Hamiltonian, seed the QSD with the product of the ground states of its subsystems, which differs from the target only through the interface terms. We prove a nonasymptotic error bound for the Chebyshev QSD that is linear in the measurement noise, by transplanting Kirby's effective-Hamiltonian analysis to the Chebyshev--Krylov basis, and identify the block-encoding rescaling of the Hamiltonian as a parameter of the guarantee. Exact simulations of antiferromagnetic Heisenberg chains show that the folded reference state reduces the Krylov dimension for a given accuracy severalfold and lowers the error under noise by two to five orders of magnitude relative to the Neel state. We show how the Ritz vector is prepared as a physical state and that the ground-state generation probability obeys a tight ceiling set by the overlap, so that recursive folding prepares ground states at polynomial cost. Taken together, these results allow for a scalable QSD framework that avoids the exponentially small ground-state overlaps associated with conventional product-state initialization. Finally we compute the fold fidelity itself: a slow power law for the gapless spin-1/2 chain, a size-independent constant for the gapped spin-1 chain, and an exact closed form converging to 1/4 for the AKLT chain.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.19922) | 2026-10-15
