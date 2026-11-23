---
title: "Authority Without Priority: The Revocation Trilemma and the Price of Stablecoin Freezes"
date: "2026-11-21"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2976"
summary: "Stablecoin contracts let issuers freeze an address, but a freeze is an ordinary transaction that block producers order like any other, so a transfer submitted after it can still execute first. We defi"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Stablecoin contracts let issuers freeze an address, but a freeze is an ordinary transaction that block producers order like any other, so a transfer submitted after it can still execute first. We define the missing guarantee as extit{revocation priority}: once a restriction is submitted, no prohibited operation submitted later takes effect before it. We prove a trilemma: with revenue-maximizing block producers, no blockchain platform can provide revocation priority together with immediacy, which makes a transfer’s effects usable upon inclusion, and neutrality, which rules out preferential inclusion or ordering for any sender. Ethereum keeps immediacy and neutrality and gives up revocation priority. Using USDT and USDC freezes on Ethereum from 2017 to 2026, we examine how issuers and their targets compete for execution order. In one case, a freeze had long been pending when a transfer submitted after it executed first. The competition has escalated from fee bidding to private submission to execution delegated through intent-based orders. Overall, the issuer pays more for order than its target. These patterns follow from the two sides’ incentives, which we model as a Tullock contest. In equilibrium the issuer outbids its target but cannot buy certainty. Stricter freeze obligations thus strengthen its incentive to integrate into ordering infrastructure, at the expense of neutrality.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2976) | 2026-11-21
