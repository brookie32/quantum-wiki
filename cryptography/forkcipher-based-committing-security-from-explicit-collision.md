---
title: "Forkcipher-Based Committing Security from Explicit Collision Security Assumptions"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2110"
summary: "Context-committing security binds an authenticated encryption (AE) ciphertext uniquely to its encryption context. Many conventional AE schemes lack this guarantee, while most generic committing transf"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Context-committing security binds an authenticated encryption (AE) ciphertext uniquely to its encryption context. Many conventional AE schemes lack this guarantee, while most generic committing transforms rely on idealized primitives. We develop committing AE from explicit forkcipher collision-resistance properties: mathsf{fCR} and zero-message collision resistance (mathsf{zmCR}). For an n-to-2n-bit forkcipher, we establish matching query complexities of order 2^{n/2} and 2^n, respectively. MILP- and SAT-based differential and reduced-round collision analyses of extsf{ForkSkinny-128-384} support the corresponding generic security levels for the full-round primitive. We also analyze collisions in ButterKnife and ZIP-AES. We lift mathsf{fCR} and mathsf{zmCR} through FCPRF and FixM to fixed-length collision-resistant PRFs. We introduce nonce-based PRF security to capture the nonce-respecting pseudorandomness needed by our constructions, and construct FHashN, proving its variable-input-length collision resistance, pseudorandomness, and nonce-based pseudorandomness. We present AEaH-2K, a two-key variant of AEaH combining secure AE with a variable-input-length collision-resistant PRF. Including the AE key in the commitment input gives confidentiality, authenticity, and CMT-4 security in the standard model. We also construct extsf{FCTR-CMT}, an AEAD mode using a single forkcipher, and prove nonce-respecting privacy, authenticity, and CMT-4 security. With FHashN based on FCPRF, extsf{FCTR-CMT} achieves n-bit confidentiality and n/2-bit authenticity and CMT-4 security; with FixM, all 3 reach n bits. All construction proofs reduce to explicit pseudorandomness and collision-resistance assumptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2110) | 2026-09-19
