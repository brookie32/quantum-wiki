---
title: "Four Dimensions Strike Back: Fast Isogeny Computation via Special Automorphisms"
date: "2026-11-22"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2983"
summary: "Four-dimensional isogeny representations enable fast signing in SQIsignHD (Eurocrypt 2024) and efficient key genera- tion and encryption in FastPOKÉ-4D, but their computational cost remains a bottlene"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Four-dimensional isogeny representations enable fast signing in SQIsignHD (Eurocrypt 2024) and efficient key genera- tion and encryption in FastPOKÉ-4D, but their computational cost remains a bottleneck for verification and decryption. We present an algorithm that exploits two automorphisms of the structured abelian fourfolds underlying these representations. The first pre- serves the half-chain kernels and induces an action of the extra automorphism of Weil type (2, 2) on the intermediate varieties. With compatible symplectic markings, its action becomes a per- mutation of theta coordinates. This allows us to apply the two- point techniques of MIKE and propagate only two kernel repre- sentatives through the generic isogeny steps. The second automor- phism exchanges the two half-chain kernels. We determine the re- sulting middle involution explicitly as a Hadamard transform fol- lowed by a coordinate permutation, allowing the complete repre- sentation to be evaluated using one constructed half-chain and its stored dual-evaluation data. We apply this algorithm to SQIsignHD verification and FastPOKÉ-4D decryption. We also describe a fast heuristic SQIsignHD variant (denoted as F-SQIsignHDH ) with di- rect smooth-isogeny commitment generation, alongside an instan- tiation using Qlapoty for key generation and commitment. We pro- vide C implementations and compare the resulting protocols with their two-dimensional variants. Our experimental results demon- strate that, with the Broadwell implementation, F-SQIsignHDH gains overall speedups of 1.66×–1.92× compared with SQIsign-v3.0 in terms of the total running time of the signing phase and verifi- cation across NIST-I, -III, and -V.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2983) | 2026-11-22
