---
title: "Derivatives of Quantum Randomness: Separating Pseudorandom Unitaries from Pseudorandom (Function-like) States"
date: "2026-09-13"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2002"
summary: "Quantum computation gives rise to new pseudorandom primitives for states and unitaries, including pseudorandom state generators (PRSGs), pseudorandom function-like state generators (PRFSGs), and pseud"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Quantum computation gives rise to new pseudorandom primitives for states and unitaries, including pseudorandom state generators (PRSGs), pseudorandom function-like state generators (PRFSGs), and pseudorandom unitaries (PRUs). In this paper, we show a full unitary oracle separation between PRFSGs and PRUs. The separation holds between the strongest state notion and the weakest unitary notion: even adaptively secure, quantum-accessible PRFSGs do not imply non-adaptively secure, forward-only PRUs, even when their implementations are allowed to be non-unitary and use an arbitrary number of ancillary qubits. This reveals a fundamental distinction between pseudorandomness for quantum states and for quantum unitaries. Our main technical idea is to view a candidate PRU construction with access to state generation oracles as a map from the underlying oracle states to implemented unitaries, and to study the derivatives of this map. These derivatives are inherently low rank, and we exploit this low-rank structure to distinguish the resulting unitaries from truly random ones. We believe this differential perspective may be useful for studying other structural questions about quantum states and unitaries.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2002) | 2026-09-13
