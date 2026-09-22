---
title: "Mist: Transparent Polynomial Commitments from Class Group Subset-Product Accumulators"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2112"
summary: "We construct the first polynomial commitment in groups of unknown order that simultaneously requires no trusted setup, has quasilinear prover time, and has constant-size opening proofs. Our main techn"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We construct the first polynomial commitment in groups of unknown order that simultaneously requires no trusted setup, has quasilinear prover time, and has constant-size opening proofs. Our main technical contribution is a transparent class group realization of the subset-product accumulator relation introduced by Morphic accumulators (CRYPTO ’26). It supports accumulating a fixed family of class group elements and proving prescribed algebraic relations among the accumulated elements, yielding constant-size range arguments with quasilinear prover time. Combining these range proofs with the DewTwo framework (CRYPTO ’25) gives the first transparent polynomial commitment with quasilinear prover time and constant-size openings. Concretely, our construction also gives the shortest known opening proofs (1.3 KB) among transparent polynomial commitments. We prove security under falsifiable class group assumptions and also develop new extraction techniques over dyadic rationals, which may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2112) | 2026-09-19
