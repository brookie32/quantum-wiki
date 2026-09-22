---
title: "Multi-Key FHE with Compact Ciphertexts (or: MKFHE Strikes Back)"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2120"
summary: "Multi-Key Fully Homomorphic Encryption (MKFHE) is a variant of fully homomorphic encryption (FHE) that allows computations over data encrypted under different keys. Its support for non-interactive, dy"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Multi-Key Fully Homomorphic Encryption (MKFHE) is a variant of fully homomorphic encryption (FHE) that allows computations over data encrypted under different keys. Its support for non-interactive, dynamic participation and on-the-fly computation makes it an attractive primitive for multi-party applications. However, MKFHE has been largely overlooked in practice as its performance scales poorly, since the ciphertext size grows linearly with the number of participants in all existing constructions. Resolving this issue was a major open problem for almost a decade. In this work, we close this gap by providing the first construction of an MKFHE scheme with compact ciphertexts: the size of ciphertexts remains constant throughout the entire homomorphic evaluation, even when the number of participating parties changes during computation. As a result, our construction retains all the advantages of MKFHE while simultaneously offering fast evaluation performance similar to that of a single-key scheme. Our methodology is generic and applies to a broad class of RLWE-based FHE schemes. Concretely, we construct efficient multi-key variants of RGSW and FV-like schemes, and further develop a compiler that transforms a wide range of RLWE-based FHE schemes into their multi-key counterparts. We implement our multi-key FV scheme in Go. Empirical results show that our scheme achieves 30.6 imes faster multiplication and 60.6 imes faster automorphism for 16 parties compared to the state-of-the art construction by Kwak et al. (CCS '23), demonstrating the concrete efficiency of our construction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2120) | 2026-09-20
