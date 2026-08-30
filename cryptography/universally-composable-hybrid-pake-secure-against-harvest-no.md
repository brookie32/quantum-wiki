---
title: "Universally Composable Hybrid PAKE Secure Against Harvest-Now-Decrypt-Later Attacks"
date: "2026-08-29"
updated: "2026-08-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1832"
summary: "We present a hybrid password-authenticated key exchange (PAKE) protocol that is secure against harvest-now-decrypt-later (HNDL) attacks by quantum adversaries, and is universally composable under the "
last_verified: "2026-08-30"
review_by: "2026-11-28"
stale: false
---

We present a hybrid password-authenticated key exchange (PAKE) protocol that is secure against harvest-now-decrypt-later (HNDL) attacks by quantum adversaries, and is universally composable under the parallel composition framework of Lyu and Liu (EUROCRYPT 2025). Existing hybrid PAKE constructions combine a classical PAKE with a post-quantum (PQ) PAKE, with the overall security intended to rely on the stronger of the two. However, identifying which PAKE is stronger is non-trivial, given the limited maturity of post-quantum PAKE designs. Recognizing that the immediate quantum threat is passive, we propose a different hybrid compiler: rather than combining two PAKEs, we encapsulate a classical PAKE within a standard post-quantum Key Encapsulation Mechanism (KEM). This modular separation avoids the fragility of post-quantum password handling while neutralizing HNDL attacks. Our compiler works with any two-pass or three-pass PAKEs. As a concrete instantiation, we construct a three-pass protocol that combines J-PAKE and a post-quantum KEM. We also implement the resulting protocol and provide performance results demonstrating that the hybrid construction remains practical, with the complete handshake executing in 2.81ext{ ms}. This construction has the distinctive advantage that it does not require any ideal cipher, (constant-time) hash-to-curve, or trusted setup assumptions. Within the Lyu-Liu framework, we show that J-PAKE satisfies the notion of a Full DH-type PAKE. We model the KEM as a password-independent Simulatable DH-type component satisfying the minimal simulation properties required for parallel composition. To capture the prospective quantum threat, we formalize a stronger variant of the standard HNDL threat model—where the quantum adversary is explicitly granted the plaintext password—and prove that our protocol achieves Session Key Security and Post-Quantum Forward Secrecy. Our construction relies solely on standardized and widely deployed primitives, yielding a hybrid PAKE that is UC-secure, efficient, and well-suited for real-world deployment during the post-quantum transition.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1832) | 2026-08-29
