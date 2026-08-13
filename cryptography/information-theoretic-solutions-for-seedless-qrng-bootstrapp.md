---
title: "Information-Theoretic Solutions for Seedless QRNG Bootstrapping and Hybrid PQC-QKD Key Combination"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.26907"
summary: "arXiv:2603.26907v3 Announce Type: replace Abstract: This paper considers two challenges faced by practical quantum networks: the bootstrapping of seedless Quantum Random Number Generators (QRNGs) and "
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2603.26907v3 Announce Type: replace Abstract: This paper considers two challenges faced by practical quantum networks: the bootstrapping of seedless Quantum Random Number Generators (QRNGs) and the resilient combination of Post-Quantum Cryptography (PQC) and Quantum Key Distribution (QKD) keys. These issues are addressed using universal hash functions as strong seeded extractors, with security foundations provided by the Quantum Leftover Hash Lemma (QLHL). First, the 'randomness loop' in QRNGs -- the requirement of an initial random seed to generate further randomness -- is resolved by proposing a bootstrapping method using raw data from two independent sources of entropy, given by seedless QRNG sources. Second, it is argued that strong seeded extractors are an alternative to XOR-based key combining that presents different characteristics. Unlike XORing, our method ensures that if the combined output and one initial key are compromised, the remaining key material retains quantifiable smooth min-entropy and remains secure in exchange of longer keys. Furthermore, the proposed method allows binding of transcript information with key material in a natural way, providing a tool to replace computationally based combiners to extend ITS security of the initial key material to the final combined output. By modeling PQC keys as having HILL (Hastad, Impagliazzo, Levin and Luby) entropy, the framework is extended to hybrid PQC-QKD systems. This unified approach provides a mathematically rigorous and future-proof mechanism for both randomness generation and secure key management against quantum adversaries.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.26907) | 2026-08-13
