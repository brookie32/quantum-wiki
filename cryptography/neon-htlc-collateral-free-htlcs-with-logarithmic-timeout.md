---
title: "Neon-HTLC: Collateral-Free HTLCs with Logarithmic Timeout"
date: "2026-11-23"
updated: "2026-11-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3008"
summary: "Hashed time-lock contracts (HTLCs) are fundamental building blocks for decentralized finance, enabling trustless cross-chain asset exchanges and off-chain payment networks. However, standard HTLCs are"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

Hashed time-lock contracts (HTLCs) are fundamental building blocks for decentralized finance, enabling trustless cross-chain asset exchanges and off-chain payment networks. However, standard HTLCs are vulnerable to bribery attacks, where malicious actors incentivize miners to censor honest transactions. While recent works propose incentive-compatible HTLCs to mitigate these attacks, they suffer from a severe scalability bottleneck: to secure a given payment amount, they require either a linear collateral or superlinear timelock (both in the payment amount). We formalize this barrier by showing that the above tradeoff holds for a generalized class of HTLCs that we call "two-phase". Our analysis also identifies optimal parameter settings for two-phase HTLCs, improving on the previous state-of-the-art, He-HTLC (NDSS'23). We then present Neon-HTLC, a novel incentive-compatible HTLC protocol that eliminates the need for collateral while drastically reducing protocol timeout. Neon-HTLC overcomes prior limitations by leveraging a novel punishment mechanism that increases exponentially over time. Consequently, Neon-HTLC achieves a timeout that scales only logarithmically with the payment amount. This timeout is not only asymptotically but also concretely practical: even for the total amount of Bitcoin, the required timeout is a small constant (max 51 blocks, or approx 8.5 hours). Our evaluation demonstrates that Neon-HTLC outperforms the state-of-the-art He-HTLC by several orders of magnitude: for a 100,000 USD payment, Neon-HTLC safeguards the transfer in just 26 blocks with zero collateral, whereas He-HTLC requires a 496-block timeout and 5,000 USD collateral.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3008) | 2026-11-23
