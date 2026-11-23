---
title: "LatPRE: Compact Lattice-Based Proxy Re-Encryption with Security against Honest Re-Encryption Attacks"
date: "2026-11-20"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2964"
summary: "Proxy re-encryption (PRE) allows a proxy to transform ciphertexts for other recipients without learning their plaintexts. It is a versatile cryptographic tool enabling a wide range of real-world appli"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Proxy re-encryption (PRE) allows a proxy to transform ciphertexts for other recipients without learning their plaintexts. It is a versatile cryptographic tool enabling a wide range of real-world applications, e.g., email forwarding, file sharing, and digital identity management. For these applications, security against honest re-encryption attacks (HRA) is essential: decrypting re-encryptions of some ciphertexts originally under a public key should not help break other ciphertexts under the same key. However, existing lattice-based approaches incur substantial ciphertext overhead or impose restrictions such as private proxy state or encryption requiring receiver's secret key. In this work, we present LatPRE, a compact single-hop HRA-secure PRE scheme based on the standard module learning with errors (MLWE) assumption. To this end, we make two technical contributions: (i) a novel generic framework for HRA-secure PRE based on a new hint-CPA security notion and hint-assisted re-encryption simulation; and (ii) tighter spectral bounds for honestly sampled leakage matrices in Matrix Hint-MLWE, whose hardness follows from standard MLWE under suitable parameters. Our results substantially reduce the required Gaussian masking widths, thereby enabling a compact lattice instantiation. We believe both contributions to be of independent interest. Finally, we implement LatPRE in C and evaluate parameter sets targeting 128-bit security and supporting up to 2^40 source encryptions and 2^20 outgoing rekeys per key. For 256-bit messages, re-encrypted ciphertexts occupy only 1.8-2.8 KB, and re-encryption takes about 0.2-0.3 ms on a standard PC. Compared with the state of the art, LatPRE achieves around 23-37 times smaller re-encrypted ciphertexts and 7-9 times faster re-encryption. To demonstrate its practicality, we also integrate LatPRE with Proton Mail's open-source framework to build a hybrid post-quantum encrypted email-forwarding prototype.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2964) | 2026-11-20
