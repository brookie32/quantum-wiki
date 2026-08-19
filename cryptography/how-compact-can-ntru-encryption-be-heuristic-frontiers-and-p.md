---
title: "How Compact Can NTRU Encryption Be? Heuristic Frontiers and Practical Schemes"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1715"
summary: "NTRU is one of the longest-tested lattice-based public-key encryption families and is often viewed as a compact alternative to (R/M)-LWE. Yet, after three decades of research, its potential for compac"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

NTRU is one of the longest-tested lattice-based public-key encryption families and is often viewed as a compact alternative to (R/M)-LWE. Yet, after three decades of research, its potential for compactness remains an open area for further exploration: recent designs such as NEV (Asiacrypt 2023) and DAWN (Asiacrypt 2025) suggest that there is still room for improvement. This raises a natural question: Has NTRU reached its compactness limit? If not, how compact can it be while still remaining secure and efficient? Motivated by this question, we aim to formalize a unified relationship between compactness and efficiency under the required security level. We present a common two-stage view of NTRU decryption. In the first stage, the decoder constructs a small set of candidate wrap-around errors. In the second stage, it verifies these candidates using either algebraic redundancy or trapdoor-derived distributional information. We introduce Free Candidate Localization (FCL), a generic first-stage method that ranks coordinates by their proximity to the centered boundary. FCL could be used in most lattice-based encryptions; we instantiate it in ML-KEM to achieve a 10% smaller ciphertext at the cost of a 5% slower overall runtime in the reference C implementation under NIST-I. We organize modern NTRU encryptions into two frameworks. NTRU with Encoding leverages algebraic structure via auxiliary quotient rings. NTRU with Trapdoor exploits geometric structure through the NTRU trapdoor, then verifies candidate corrections using distributional tests. These frameworks give a common language for existing NTRU designs and for the compactness searches in this paper. Within an explicit search model, we derive heuristic compactness frontiers for both frameworks. At NIST-I, the encoding frontier yields a total public-key plus ciphertext size of 812 bytes, and the trapdoor frontier yields a size of 754 bytes, 15%/21% smaller than the previous lowest size of 964 bytes in DAWN. Furthermore, we propose END, an instantiation of NTRU with Trapdoor plus FCL. At NIST-I, extsf{END} has a 384-byte ciphertext, which is exactly half the size of the 768-byte ciphertext of ML-KEM-512, and is 12-19% smaller than the shortest prior NTRU-style ciphertexts in BAT (TCHES 2022) and DAWN. In our reference C implementation, the combined encapsulation and decapsulation cost of END-512 is about 3% higher than that of ML-KEM-512.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1715) | 2026-08-17
