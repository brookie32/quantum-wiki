---
title: "SILMARILS-MV: Information-Theoretically Secure Multi-Verifier Signatures with Dealer-Free Key Issuance and Linear Aggregation for Permissioned Blockchains"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.31814"
summary: "arXiv:2610.31814v1 Announce Type: cross Abstract: Permissioned blockchains authenticate transactions, votes and quorum certificates with computationally secure signatures, and post-quantum replacement"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2610.31814v1 Announce Type: cross Abstract: Permissioned blockchains authenticate transactions, votes and quorum certificates with computationally secure signatures, and post-quantum replacements inflate consensus traffic by orders of magnitude. Information-theoretic alternatives have required a trusted authority, quantum channels, per-signature interaction, or single-use keys with bounded transfer. We present SILMARILS-MV, a multi-verifier unconditionally secure signature in which a signature is the vector alpha = A,e(m) and each verifier holds a secret functional c_i = Gamma^T lambda(x_i) derived from virtual anchors Gamma that nobody learns. Against unbounded adversaries corrupting up to omega verifiers and any signers, and observing every decision, an honest verifier accepts a forged or invalid signature with probability at most Q/q + 1/(q-1), a bound that is tight in its leading term. The scheme is strongly unforgeable, non-repudiable, transferable across unboundedly many hops, and linearly aggregatable. Keys are issued by the validators through perfectly secure MPC for t < n/3, without broadcast. To scale, we let the committee itself sign: in threshold notarization, finality certificates have constant size 32(omega+1) bytes and per-validator issuance cost no longer depends on n. Arbiter-verified keys give clients 32-byte signatures, robust redistribution supports membership changes and share refresh, and verifiers can be enrolled retroactively. A certificate verifies in 2.4 microseconds. In an analytic normal-case model at 1000 validators, threshold notarization needs 71 KiB of authentication traffic per validator per block, 22x less than ML-DSA-44 for admitted verifiers. In a Rust HotStuff prototype with 100 validators, SILMARILS-MV commits 2.8x more transactions per second than ML-DSA-44 with 67x less cryptographic CPU, and Monte-Carlo attacks match the bounds.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.31814) | 2026-10-26
