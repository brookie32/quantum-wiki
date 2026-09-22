---
title: "Couplet: Multivariate Polynomial Commitments with Two-Group-Element Openings"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2106"
summary: "We present Couplet, a new pairing-based multivariate polynomial commitment scheme (PCS). Couplet is the first multivariate PCS whose opening proofs are solely two group elements. In addition, for the "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We present Couplet, a new pairing-based multivariate polynomial commitment scheme (PCS). Couplet is the first multivariate PCS whose opening proofs are solely two group elements. In addition, for the case of multilinear polynomials, Couplet is the first constant-proof PCS with a prover that requires only a sublinear number of group operations. We achieve those properties simultaneously at the expense of a quasilinear, polynomial-specific, one-time preprocessing phase, whose cost can be amortized over multiple subsequent openings. On BN254, our implementation opens multilinear polynomials with 20 variables about 20imes faster than Mercury after preprocessing, breaking even in total prover time after roughly 100 openings. Our approach generalizes to batched evaluation proofs, yielding a constant-size proof for multiple evaluation points without using random oracles. Applications include verifying repeated inferences of a committed model as well as more efficient auditable authenticated dictionaries. Our main technique involves compressing Papamanthou--Shi--Tamassia (PST) evaluation proofs, giving a single commitment which encodes all log n quotient polynomials which are normally given out separately in a PST proof. In doing this, we reduce the verification to a univariate sumcheck problem, which we solve with techniques from Groth16 using a single additional group element. We prove extractability in the algebraic group model under a parameterized discrete-logarithm assumption. We give hiding variants and prove perfect zero-knowledge of the opening protocols. All opening protocols are noninteractive and require no random oracle.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2106) | 2026-09-19
