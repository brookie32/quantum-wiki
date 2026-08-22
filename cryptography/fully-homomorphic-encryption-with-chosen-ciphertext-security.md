---
title: "Fully Homomorphic Encryption with Chosen-Ciphertext Security from LWE"
date: "2026-08-21"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1756"
summary: "We construct (1-hop) fully homomorphic encryption (FHE) schemes with chosen-ciphertext (CCA) security from the learning with errors (LWE) assumption in the standard model. Security of our construction"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

We construct (1-hop) fully homomorphic encryption (FHE) schemes with chosen-ciphertext (CCA) security from the learning with errors (LWE) assumption in the standard model. Security of our construction only relies on the circular-secure LWE, which matches the assumptions needed for FHE with the basic chosen-plaintext security. Besides, the scheme achieves a security notion that is strictly stronger than the CCA1 security. Prior FHE schemes with even just CCA1 security require either the random oracle model or non-falsifiable assumptions. The construction follows the well-known Naor-Yung double encryption paradigm. However, unlike previous works [Boneh et al., ITCS 2012; Canetti et al., PKC 2017; Manulis and Nguyen, Eurocrypt 2024], which employ general zero-knowledge succinct non-interactive arguments of knowledge (ZK-SNARKs), we design a special succinct argument to prove the validity of FHE ciphertexts. The succinct argument is constructed from batch arguments for NP and a new primitive called predicate extractable commitment, which may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1756) | 2026-08-21
