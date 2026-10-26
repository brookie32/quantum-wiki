---
title: "Decision Attacks on Known-Covariance Ring-LWE via Public Gram Determinants"
date: "2026-10-25"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2638"
summary: "Known-Covariance Ring-LWE (KCov-RLWE) was introduced by Micciancio and Suhl to support simulation-secure threshold encryption. It strengthens ordinary Ring-LWE by revealing an exact quadratic summary "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Known-Covariance Ring-LWE (KCov-RLWE) was introduced by Micciancio and Suhl to support simulation-secure threshold encryption. It strengthens ordinary Ring-LWE by revealing an exact quadratic summary of the hidden secret and errors, and its decisional hardness was left open. We give explicit polynomial-time decision attacks for broad families of prime moduli at ring rank one. Our key observation is that the public sample and the covariance hint together determine a bordered Gram matrix whose determinant exposes a hidden residual with a different distribution for genuine and uniform samples. After reducing the ring into finite-field components, this residual has one of two forms: a product across reciprocal components, or a Hermitian norm when a component is preserved by conjugation. The latter case yields a particularly strong distinguishing signal. Moreover, reduction modulo any divisor preserves the KCov real and random experiments exactly, so every attackable odd prime divisor of a composite modulus transfers the corresponding distinguisher with no loss of advantage. The attack covers the one-sample setting globally in the self-reciprocal regime and, under the coefficient-product Gaussian specialization, locally in the completely split regime. More generally, we obtain a complete classification of how this residual-based attack behaves for odd prime moduli when mge2, and extend these guarantees to arbitrary moduli possessing a suitable odd prime divisor. The classification does not imply insecurity for every parameter family: when the relevant residue fields are sufficiently large, the guaranteed distinguishing advantage in the reciprocal case can become negligible, and pure power-of-two moduli remain outside the divisor-reduction extension. Accordingly, our results invalidate the KCov pseudorandomness assumption in the quantified families; they do not show that every parameter choice permitted by the motivating Ring-PKE sketch is insecure, nor do they give a direct IND-CPA break of the complete threshold-encryption construction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2638) | 2026-10-25
