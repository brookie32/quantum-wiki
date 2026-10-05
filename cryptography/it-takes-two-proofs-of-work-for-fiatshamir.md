---
title: "It Takes Two: Proofs of Work for Fiat–Shamir"
date: "2026-10-03"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2326"
summary: "In the random oracle model (ROM), proof of work (PoW) serves two roles in the Fiat–Shamir transformation. First, in challenge grinding, the prover must solve a puzzle for each candidate challenge, whi"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

In the random oracle model (ROM), proof of work (PoW) serves two roles in the Fiat–Shamir transformation. First, in challenge grinding, the prover must solve a puzzle for each candidate challenge, which amplifies soundness and reduces proof size and verifier time. This requires a non-amortizing PoW: computing k distinct accepted puzzle–solution–proof triples costs, in expectation, roughly k times the work of computing one. Second, PoW can prevent diagonalization attacks, in which the statement's circuit computes its own challenge. The XFS transformation of Arnon and Yogev (CRYPTO 2025) uses a strong PoW: an adversary that does substantially less work than the honest prover solves a random puzzle with only negligible probability, even after bounded preprocessing. Can a single PoW be both strong and non-amortizing? We prove that it cannot, whenever the verifier is sufficiently cheaper than the prover. Our main technical tool converts computational uniqueness into statistical uniqueness without increasing verifier query complexity. Combined with the search bound of Guan, Riazanov, and Yuan (CRYPTO 2025), which builds on Smyth (STOC 2002), it resolves their open question. To overcome this barrier, our XFS-with-grinding transformation for relativized Sigma-protocols composes a strong PoW with a non-amortizing one. The resulting non-interactive argument retains the soundness amplification of grinding and the security guarantee of XFS in the relativized ROM, with additive prover work for the two PoWs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2326) | 2026-10-03
