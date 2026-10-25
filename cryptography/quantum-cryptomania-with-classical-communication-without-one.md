---
title: "Quantum Cryptomania with Classical Communication without One-Way Functions"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2607"
summary: "In classical cryptography, one-way functions are necessary for most of cryptography. In the quantum world, however, Kretschmer at TQC'21 and subsequent works have demonstrated that quantum versions of"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

In classical cryptography, one-way functions are necessary for most of cryptography. In the quantum world, however, Kretschmer at TQC'21 and subsequent works have demonstrated that quantum versions of various primitives in minicrypt, such as signatures and private-key encryption, do not require quantum-computable one-way functions (qOWFs). However, the question of the necessity of qOWFs for primitives in Cryptomania like public-key encryption with classical public-keys and ciphertexts (qPKE) has remained open. We provide a comprehensive picture of the relationship between qPKE and qOWF. First, our main result is a black-box separation between qOWFs and qPKE. In particular, we show that relative to a unitary, real, and self-inverse oracle, there exists a qPKE scheme (with classical keys and ciphertexts), but qOWFs do not exist. Further, our oracles admit a point-function obfuscation construction, thus ruling out black-box construction of qOWF from point function obfuscations. On the positive side, we construct qPKE from quantum indistinguishability obfuscation for quantum circuits with classical obfuscated descriptions and efficiently verifiable one-way puzzles, which is known to be a potentially weaker assumption than qOWFs, due to an existing black-box separation. Our construction is the quantum analog of the classical construction of PKE from one-way functions and indistinguishability obfuscation in the quantum computation with classical communication (QCCC) setting.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2607) | 2026-10-23
