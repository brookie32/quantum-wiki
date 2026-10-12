---
title: "Lattice Bingo: Asynchrony and One-Shot Adaptivity in Verifiable Secret Sharing via Erasure Code Commitments"
date: "2026-10-09"
updated: "2026-10-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2432"
summary: "Asynchronous verifiable secret sharing (AVSS) allows a dealer to distribute a secret among parties while preserving privacy and consistent reconstruction, despite Byzantine faults and arbitrary messag"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

Asynchronous verifiable secret sharing (AVSS) allows a dealer to distribute a secret among parties while preserving privacy and consistent reconstruction, despite Byzantine faults and arbitrary message delays. It is a fundamental building block for Byzantine agreement, distributed key generation, and secure multiparty computation. Packed AVSS protocols share many secrets together to reduce communication per secret. The best known AVSS protocols achieve quadratic communication while sharing linearly many secrets. In particular, Bingo (Abraham et al., CRYPTO 2023) shares a batch of Theta(k) secrets among k parties using O(lambda k^2) words of communication, while also achieving adaptive security, but relies on assumptions that are not post-quantum secure. Known post-quantum alternatives have higher worst-case communication for comparable batch sizes or require substantially larger batches to achieve linear amortized communication. We present Lattice Bingo, a lattice-based packed AVSS protocol with quadratic communication and linear packing. For every constant epsilon>0, it shares Theta(k) secrets among kgeq(3+epsilon)f parties, tolerates f Byzantine parties, and uses O(k^2operatorname{poly}(lambda)) words of communication. It additionally achieves one-shot adaptive secrecy: the adversary may adaptively choose its corruption and reconstruction requests based on the public transcript observed so far, but must submit these requests together in a single batch. Our main technical contribution is a commitment scheme for two-dimensional linear codes based on the PowerBASIS assumption. We combine PowerBASIS commitments with the linear code based secret sharing of Applebaum, Nir, and Pinkas, replacing the Reed–Solomon encoding and KZG commitments used in Bingo. Our commitment supports proof interpolation, enabling parties to recover missing shares and their opening proofs. It additionally achieves a notion that we call one-shot simulation hiding. Together, these properties allow us to adapt Bingo’s framework to obtain Lattice Bingo with the same efficiency and one-shot adaptive security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2432) | 2026-10-09
