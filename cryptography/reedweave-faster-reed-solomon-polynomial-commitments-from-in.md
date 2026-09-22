---
title: "ReedWeave: Faster Reed-Solomon Polynomial Commitments from Interleaving and Folding"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2147"
summary: "Polynomial commitment schemes (PCSs) allow a prover to commit to a polynomial and later prove its evaluations succinctly. Among hash-based constructions, FRI (Ben-Sasson et al., ICALP 2018) and its fo"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Polynomial commitment schemes (PCSs) allow a prover to commit to a polynomial and later prove its evaluations succinctly. Among hash-based constructions, FRI (Ben-Sasson et al., ICALP 2018) and its follow-up works achieve polylogarithmic proofs by recursively ``folding'' Reed-Solomon (RS) codes. However, their concrete evaluation costs remain relatively high, as the first few folding rounds operate on the largest codewords and dominate the prover work. We present ReedWeave, a Reed-Solomon PCS that successfully incorporates interleaving with folding, achieving the best of the two worlds. ReedWeave decomposes a degree-d polynomial into m smaller components and commits to their RS encodings over a common domain. Under our novel decomposition, a random linear combination of these codewords is exactly an m-ary folding. At a high level, ReedWeave starts with an m-ary folding, followed by standard binary folding as in FRI. The prover costs are substantially reduced in the sense that at the very beginning it suffices to do interleaved-RS encoding rather than standard RS encoding. That is, we reduce prover costs from O(d log d) to O(dlog(d/m)) for constant code rate while maintaining efficient polylogarithmic verification. Moreover, our approach essentially works for arbitrary m, relaxing the smoothness requirements of the underlying fields by a multiplicative factor of m. We benchmark our Rust implementation over Goldilocks using 32 threads and targeting 100-bit security. At d=2^{24}, rho=1/4, and m=64, the DEEP variant commits in 475.0 ms, opens in 111.6 ms, verifies in 2.07 ms, and produces a 594.7 KiB proof. Compared with FRI (ICALP 2018), commitment, opening, and verification are 6.9imes, 51.5imes, and 4.2imes faster, respectively. Against STIR (CRYPTO 2024), the corresponding speedups are 2.9imes, 68.5imes, and 2.1imes. Its proof is only 0.69imes the size of FRI's and 2.31imes that of STIR's.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2147) | 2026-09-22
