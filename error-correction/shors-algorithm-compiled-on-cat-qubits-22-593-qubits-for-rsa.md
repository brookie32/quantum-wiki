---
title: "Shor's algorithm compiled on cat qubits: 22 593 qubits for RSA-2048 in 3.14 days"
date: "2026-10-28"
updated: "2026-10-29"
source: "agent"
category: "error-correction"
tags: [error-correction, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2665"
summary: "We present an end-to-end resource estimation of Shor's algorithm on superconducting cat qubits, from its mathematical description to the allocation and scheduling of physical qubits on a chip layout. "
last_verified: "2026-10-29"
review_by: "2027-01-27"
stale: false
---

We present an end-to-end resource estimation of Shor's algorithm on superconducting cat qubits, from its mathematical description to the allocation and scheduling of physical qubits on a chip layout. After proposing a comprehensive view of the modern versions of Shor's algorithm for RSA, ECDLP and FFDLP, we make explicit their logical circuits and the trade-offs they enable. We compile the dominant subroutines down to physical-qubit operations on two architectures: one based on repetition cat codes and one based on LDPC cat codes. We design a parity-Cnot gate for cat qubits, extend a multi-target Cnot gate to the LDPC-cat architecture, and adapt an active injection procedure to cat-qubit architectures. Building on these primitives, we adapt to cat-qubit architectures the adder from Gidney’s 2025 resource estimate for factoring RSA-2048. We combine our adder compilation and a coarser resource estimate for the phaseup with the factory designs and lookup compilation from the FeMoco resource estimation of Kroell et al. Together, these compilations lead to chip layouts and schedules for factoring RSA-2048. Assuming a 1mus error-correction cycle time, a 10mus reaction time, circuit-level phase-flip noise with probability p_Z = 5 imes 10^{-4} and no bit-flips, factoring RSA-2048, the configuration we compile in full, requires about 23 000 cat qubits and 3.14 days. Reusing the operations compiled for RSA-2048, solving ECDLP on secp256k1 requires at most 30 000 cat qubits and 1 hour, and FFDLP-512, which we propose as an intermediate benchmark, about 6,700 cat qubits and 21~minutes. Trading space for time, RSA-2048 runs in 1.25 hours on about 611 000 cat qubits. The requirement on no bit-flips (which corresponds to a bit-flip time of about 100 years) can be relaxed to a bit-flip time of about one hour by using an additional concatenation layer into a distance-3 bit-flip error-correcting code. In that case, we estimate that the cost of RSA-2048 increases to about 45 000 cat qubits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2665) | 2026-10-28
