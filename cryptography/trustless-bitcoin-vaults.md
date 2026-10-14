---
title: "Trustless Bitcoin Vaults"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2466"
summary: "Bitcoin (BTC) is the largest crypto asset, yet the Bitcoin blockchain offers few applications in which BTC can be used. A standard approach to make BTC useful is bridging: BTC is deposited on the Bitc"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Bitcoin (BTC) is the largest crypto asset, yet the Bitcoin blockchain offers few applications in which BTC can be used. A standard approach to make BTC useful is bridging: BTC is deposited on the Bitcoin chain and a wrapped asset is minted on a chain such as Ethereum, where it can be used in smart contract applications. Unfortunately, all Bitcoin bridges to date require trust assumptions on a centralized party or a committee running the bridge to enable withdrawals of the deposited BTC, including state-of-the-art BitVM bridges. In this paper, we observe that while bridges are application-agnostic, most BTC holders are interested in collateral-based applications, where BTC is deposited as collateral, and only the depositor or a set of known counterparties can withdraw the asset. For this class of applications, we propose a primitive, Trustless Bitcoin Vaults, that guarantees that the BTC depositor or the counterparties can withdraw the deposited BTC following only the logic of the application smart contract without trusting any third party. We present a protocol that achieves the security guarantees of this primitive and instantitate it for a lending application where the deposited BTC is used as collateral to borrow against a set of liquidators on the Aave v4 smart contracts on Ethereum. Our mainnet experiments show that at the current Bitcoin price and fee rate, a deposit costs about 0.7 in fees while a withdrawal costs at most 7.7. Our construction is built on recent advances in efficient proof verification for Bitcoin.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2466) | 2026-10-14
