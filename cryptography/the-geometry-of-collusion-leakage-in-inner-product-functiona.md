---
title: "The Geometry of Collusion Leakage in Inner-Product Functional Encryption"
date: "2026-10-07"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2404"
summary: "Inner-product functional encryption (IPFE) allows the holder of a functional key for a vector y to learn langle x,yrangle from an encryption of x, and nothing more. Keys, however, accumulate: a coalit"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

Inner-product functional encryption (IPFE) allows the holder of a functional key for a vector y to learn langle x,yrangle from an encryption of x, and nothing more. Keys, however, accumulate: a coalition holding sufficiently many independent keys recovers the plaintext. We model each institution by the span W_ileqF_q^n of its authorized key vectors and show that a coalition I determines the plaintext exactly modulo (sum_{iin I}W_i)^perp; for a uniform plaintext it learns exactly imsum_{iin I}W_i field symbols. The resulting leakage function is a representable and entropic polymatroid. We then study authorization spaces of dimension r whose pairwise intersections have dimension at most h. We prove that some coalition of size cgeq2 always learns at least min{n,2r-h+c-2} dimensions, and we give a Vandermonde-type construction in which every coalition of size c learns exactly this amount, for all c simultaneously. Hence the largest achievable reconstruction threshold is n-2r+h+2, which gives an exact tradeoff between functional diversity and collusion resistance. The optimal configuration is a sunflower, an equidistant subspace code and a generalized arc; its orthogonal complements form a generalized dual arc, and for r=1 it reduces to Reed--Solomon secret sharing.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2404) | 2026-10-07
