---
title: "Unshuffling Fisher-Yates: Practical Recovery of Length-128 Permutations and Application to ML-DSA"
date: "2026-10-27"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2658"
summary: "Shuffling is a standard hiding countermeasure against (single-trace) side-channel attacks on the number-theoretic transform (NTT) of lattice-based post-quantum schemes, such as ML-DSA. The Fisher-Yate"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

Shuffling is a standard hiding countermeasure against (single-trace) side-channel attacks on the number-theoretic transform (NTT) of lattice-based post-quantum schemes, such as ML-DSA. The Fisher-Yates algorithm can be used to generate the underlying random permutation. Recovering this permutation itself from a single trace has so far only been studied for short sequences. We present a practical attack on a software implementation of Fisher-Yates for sequences of length 128, the number of butterfly operations in one layer of ML-DSA’s NTT. We identify the exploitable leakage of the algorithm, detect and remove the timing variations caused by rejection sampling and extract Hamming weight and identity leakage from a single trace per shuffle. We encode these hints as a constraint-programming problem with a soft objective function and enumerate the most likely permutations in order of descending likelihood. Applied to a shuffled ML-DSA-44 NTT, the recovered permutations are used to re-order the butterfly leakage, and recover the secret polynomial s1 either directly or up to a few coefficients that are enumerated directly. Protecting ML-DSA’s NTT with Fisher-Yates-based shuffling does, therefore, not, by itself, prevent side-channel-assisted key recovery.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2658) | 2026-10-27
