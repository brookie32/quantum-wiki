---
title: "Quantum code parameters, checkable by a certificate of provable size"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03214"
summary: "arXiv:2610.03214v1 Announce Type: new Abstract: A code is described by three numbers: its physical qubits, its logical qubits, and the smallest error it cannot detect, counted in qubits. The first two"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03214v1 Announce Type: new Abstract: A code is described by three numbers: its physical qubits, its logical qubits, and the smallest error it cannot detect, counted in qubits. The first two are linear algebra. The third, the distance, is an optimum over an exponentially large set, read off a solver whose answer carries no certificate. Whether a code's parameters can be checked uniformly across codes, with a certificate of proved size, is open. Here we show that they can, by moving the unit of work from the code to a certificate, a short object, either a list, a pairing or a symbolic instance, whose correctness the kernel of the Lean proof assistant decides by computation. The kernel is the small core that checks each step. The certificate's size is itself a theorem: its enumeration form lists the vectors of weight below the distance d, sum_{j<d}inom{n}{j} of them, a polynomial in the code's length n at fixed distance d. No bound uniform over codes in both n and d is smaller. For product families the certificate is smaller still, the bound being proved once, symbolically. Deciding that a vector lies outside the row space of the check matrix, the set of sums of its rows, becomes one matrix-vector product and one inner product. On an eighteen-qubit toric code, a surface code closed into a torus, the whole-file check of that decision falls from 42,s to 9,s. Eleven code families and thirty-nine parameter sets follow, the widest at 1872 qubits. Nothing beyond the three standard axioms of Lean's logic is trusted, though the generator that writes a code's checks stops at twenty qubits, and the lower bound for the 144-qubit code is imported rather than proved here. A distance becomes checkable rather than believed, and the same move applies wherever else a computation ends in a solver.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03214) | 2026-10-05
