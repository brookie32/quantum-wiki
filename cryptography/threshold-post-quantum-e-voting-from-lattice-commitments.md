---
title: "Threshold Post-Quantum E-Voting from Lattice Commitments"
date: "2026-10-15"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2500"
summary: "Lattice-based homomorphic e-voting protocols built on commitments, such as EVOLVE, keep ballots private against all but one authority and the tally verifiable even if all authorities collude, but need"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

Lattice-based homomorphic e-voting protocols built on commitments, such as EVOLVE, keep ballots private against all but one authority and the tally verifiable even if all authorities collude, but need every authority for tallying. We present T-EVOLVE, in which votes are Shamir-shared over the commitment message space: any t of n authorities complete the tally, privacy holds against t-1 colluding authorities, and verifiability against all of them. The voter proves that her committed shares form a Reed-Solomon codeword whose value at zero is a valid vote; the parity checks cost no communication, and tallying interpolates public column sums without norm growth. Complaints of authorities, including those about ciphertexts that do not decrypt, are publicly verifiable given an encryption scheme with publicly verifiable opening; we define its interface and show that it can be instantiated under LWE. We prove privacy, verifiability, individual verifiability and robustness in the classical random oracle model; the verifiability reduction for the efficient instantiation is not tight. In a C implementation, a voter's yes/no ballot for four authorities takes 109 KB without encryption overhead and signatures, and an authority aggregates 10^4 ballots in about three minutes on one core.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2500) | 2026-10-15
