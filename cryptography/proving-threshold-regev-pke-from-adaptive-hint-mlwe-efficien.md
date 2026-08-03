---
title: "Proving Threshold Regev PKE from Adaptive Hint-MLWE: Efficient, Non-interactive, and CCA Secure"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1585"
summary: "Threshold public-key encryption (tPKE) has recently attracted renewed interest, largely due to NIST's call for Multi-Party Threshold Cryptography. While classical tPKE has approached a high state of m"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

Threshold public-key encryption (tPKE) has recently attracted renewed interest, largely due to NIST's call for Multi-Party Threshold Cryptography. While classical tPKE has approached a high state of maturity, its post-quantum counterpart has not. Indeed, thresholdizing the celebrated lattice-based Regev PKE, which forms the basis of ML-KEM, remains unsatisfactory. Interestingly, how to thresholdize Regev PKE has not fundamentally changed in over a decade --- the only thing that has gradually progressed is its security analysis. To this day, it remains open whether threshold Regev can be proven secure while simultaneously satisfying a polynomial modulus, non-interactive decryption, and CCA-compatibility, each of which is essential for practical deployment. We answer this affirmatively, providing the first proof that threshold Regev is secure under the MLWE assumption while satisfying all three requirements. In fact, we prove that it satisfies a very strong form of simulation-based security --- even stronger than what was known under a super-polynomial modulus --- allowing the adversary to obtain partial decryptions even of the challenge ciphertext. At the technical heart of our result is the adaptive hint-MLWE (AHMLWE) problem, an adaptive variant of hint-MLWE where the adversary obtains hints on the MLWE secret with adaptively chosen coefficients. We show that AHMLWE reduces tightly to standard MLWE, which may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1585) | 2026-08-03
