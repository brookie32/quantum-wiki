---
title: "SEC: One-Share Everywhere-Short Secret Sharing from Lossless Expanders"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2841"
summary: "We introduce (mathsf{SEC}), an expander-code-based ramp secret sharing scheme over (Z)-modules, particularly suitable for lattice-based distributed cryptography. It is everywhere-short: bounded secret"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

We introduce (mathsf{SEC}), an expander-code-based ramp secret sharing scheme over (Z)-modules, particularly suitable for lattice-based distributed cryptography. It is everywhere-short: bounded secret coefficients yield bounded share coefficients, and the integer reconstruction vectors have bounded entries. Moreover, each participant receives exactly one share, regardless of the number of parties and the privacy and reconstruction thresholds. This improves on prior schemes with bounded share coefficients and bounded entries in the integer reconstruction vectors, in which the number of sub-shares or shares per participant grows either with the number of parties and the threshold or with the security parameter. The construction rests on a coding-theoretic observation: in the bi-adjacency matrix of a lossless bipartite expander, unique-neighbor peeling completes every sufficiently small set of columns to a square unimodular submatrix. We prove correctness, everywhere-shortness, and linearity, and give a publicly computable entrywise bound on the reconstruction vector our algorithm returns for each authorized set. For privacy, we introduce hard-core local leakage resilience, which strengthens the leakage-resilience notion of Nielsen and Simkin (EUROCRYPT 2020) to protect a hard-core function of the secret, and we prove that (mathsf{SEC}) satisfies it against correlated multi-query local leakage under the (mathsf{MatrixHintext{-}MLWE}) problem, which admits a reduction from the standard (mathsf{MLWE}) problem. For (n=60) participants and security parameter (kappa = 128), (mathsf{SEC}) achieves privacy threshold (6) against (2^{64}) leakage queries and empirical reconstruction threshold (46). The ideal entropy-coded secret and share sizes are about (3.5) KiB and (6.4) KiB, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2841) | 2026-11-09
