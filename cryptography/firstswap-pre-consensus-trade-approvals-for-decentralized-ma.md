---
title: "FirstSwap: Pre-Consensus Trade Approvals for Decentralized Market Design"
date: "2026-11-06"
updated: "2026-11-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2807"
summary: "Decentralized exchanges typically give traders no execution guarantee until a block is finalized. In the meantime, external prices move, traders strategically delay submission, and block producers can"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

Decentralized exchanges typically give traders no execution guarantee until a block is finalized. In the meantime, external prices move, traders strategically delay submission, and block producers can influence inclusion and ordering. We introduce FirstSwap, a DEX built on a constant-function market maker pricing curve that gives traders an early pre-approval before consensus, guaranteeing inclusion and execution within their submitted price limit, with final ordering determined by limit prices rather than by a block producer. We demonstrate the benefits of trade pre-approvals in an economic model combining auction theory with CEX-DEX arbitrage. When the CEX price changes gradually, FirstSwap rewards earlier traders with better prices, discouraging strategic delay and yielding higher social welfare and gains to AMM liquidity providers than a batch auction. When the CEX price jumps abruptly, FirstSwap yields higher welfare and smaller AMM losses than fair ordering. The central challenge is delivering fast trade pre-approvals without consensus. We introduce a decentralized, scaled admissibility protocol under which each validator reserves only a fraction of the available liquidity at every price. A trader obtains approval in a single round of messages with a quorum of validators. Somewhat surprisingly, despite Byzantine validators who may approve trades arbitrarily, we show that all quorum-certified trades are jointly admissible and execute within their limits. Our protocol extends naturally to a setting where buy and sell orders can be pre-approved against each other before a block is finalized.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2807) | 2026-11-06
