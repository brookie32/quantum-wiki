---
title: "Wasp: Succinct Non-Interactive Zero-Knowledge Proofs from VOLE"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1988"
summary: "Zero-knowledge proofs (ZKPs) based on vector oblivious linear evaluation (VOLE) excel in prover efficiency but typically require linear communication and verification. Antman (Weng et al., CCS '22) in"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Zero-knowledge proofs (ZKPs) based on vector oblivious linear evaluation (VOLE) excel in prover efficiency but typically require linear communication and verification. Antman (Weng et al., CCS '22) introduced information-theoretic polynomial authentication codes (IT-PACs) to achieve sublinear communication: O(B + C) for SIMD (single-instruction-multiple-data) circuits and O(B^3 + C) for general circuits, where N=B dot C is the total circuit size and B,C are batch size and subcircuit size, respectively. Antman++ (Bui et al., J. Cryptol. '25) further reduced the general-case communication to O(B + C). However, these protocols remain interactive and cannot be made non-interactive via traditional techniques like Fiat-Shamir, due to limited functionalities of IT-PACs; also, the verifier of Antman++ is not succinct for processing Nimes N public matrices. In this work, we present a succinct non-interactive ZKP system mathsf{Wasp}. Specifically, (1) we enhance the IT-PAC primitive to a fully functional polynomial commitment scheme (PCS) with the support of generic evaluation openings. With this PCS, we construct mathsf{Wasp^S}, a non-interactive ZKP for SIMD circuits based on Antman; also, we build mathsf{Wasp^G}, a general zkSNARK with constant verifier time and proof size based on the Plonkish constraint system. (2) We optimize the SIMD-to-general compiler from Antman++ by exploiting sparse representation of matrices and extending preprocessing techniques to the SIMD setting, and achieve a sublinear verifier. All our protocols achieve non-interactivity in the VOLE-hybrid model (i.e., given preprocessed VOLE correlations). Experiments show the non-interactive verifier of our SIMD zkSNARK mathsf{Wasp^S} is 1sim 2 orders of magnitude faster than the interactive one of Antman; when compiled with our compiler, the general-case verifier is 2sim 3 orders of magnitude faster than the one in Antman++. Our general zkSNARK mathsf{Wasp^G} has a 1sim 2 orders of magnitude faster prover than pairing-based, coding-based and lattice-based zkSNARKs, with less than 1 ms verifier time and 122 KB proof size; compared to the non-succinct VOLE-based ZKP, mathsf{Wasp^G} is 3sim22imes slower in proving but can be 4 orders of magnitude faster in verification with 3 orders of magnitude smaller proof size.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1988) | 2026-09-12
