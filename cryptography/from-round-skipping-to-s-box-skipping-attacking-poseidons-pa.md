---
title: "From Round Skipping to S-Box Skipping: Attacking Poseidon's Partial Layer via Subspace Restriction"
date: "2026-08-15"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1692"
summary: "Poseidon [Grassi, Khovratovich, Rechberger, Roy, and Schofnegger; USENIX'21] is an arithmetization-oriented (AO) hash function designed to be efficient in real-world zero-knowledge (ZK) applications. "
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

Poseidon [Grassi, Khovratovich, Rechberger, Roy, and Schofnegger; USENIX'21] is an arithmetization-oriented (AO) hash function designed to be efficient in real-world zero-knowledge (ZK) applications. We present GSR, a generalized S-box skipping gadget that absorbs a single initial full round and t-2k partial rounds without increasing the polynomial degree of the Poseidon polynomial system with state size t and input-output constraints 2k. By restricting the subspace of the total constraints satisfying solutions, independent of the rounds constants and MDS matrix selection, the distinguisher expends input degrees of freedom to linearize the internal state transitions where the dense algebraic mixing usually occurs. This maps a computationally infeasible polynomial system into a bounded, low-degree ideal parameterized by k free variables. We show how to use the gadget to construct a probability 1 distinguisher over t-2k+1 rounds of Poseidon. We then show how this distinguisher can be used as a basis for interpolation-based attacks. We go on to present experimental solutions to the CICO-1 problem over 28 out of 31 rounds and CICO-2 problem over 25 out of 31 rounds in the setting set by the Ethereum Poseidon initiative (i.e., using the KoalaBear field with t=24 and alpha=3). Crucially, since the subspace restriction approach is tuned only by t and k, our results apply to the Poseidon structure regardless of the choice of round constants, MDS matrix, S-box exponent alpha, or field size p.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1692) | 2026-08-15
