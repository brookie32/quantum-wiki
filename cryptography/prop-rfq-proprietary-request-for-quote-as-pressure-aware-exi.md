---
title: "Prop RFQ: Proprietary Request for Quote as Pressure-Aware Exit Pricing for Redeemable Real-World Asset Tokens"
date: "2026-08-19"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1739"
summary: "Redeemable real-world asset tokens can trade onchain faster than their backing assets can be sold or settled. An immediate-exit facility cannot treat reported net asset value (NAV) as fully liquid. Wi"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

Redeemable real-world asset tokens can trade onchain faster than their backing assets can be sold or settled. An immediate-exit facility cannot treat reported net asset value (NAV) as fully liquid. Within our scope, the mechanisms we compare do not jointly provide permissionless access, order-splitting resistance, and favorable small exits. In this paper, we propose a Proprietary Request for Quote (Prop RFQ), an onchain facility that prices exits against available reserves and mitigates, but does not eliminate, split-order incentives. Its quote combines NAV, an order-size curve, a funded-liquidity wall, decaying sell pressure, and a cadence response to repeated sells. The design seeks to keep isolated small exits useful while limiting reserve depletion and gains from splitting a concentrated exit. We evaluate the implemented Solana pricing path with fixed workloads and ablations, then sweep 15,120 parameter configurations. At the reference parameters, cadence reduces aggregate split advantage by 9.67% against matched pressure-only pricing, improves 34 of 40 split workloads, and raises worst-case reserve remaining from 10.49% to 17.66%. No simple policy or Prop RFQ ablation in our comparison dominates the reference configuration on common metrics. After correcting epoch rollover, implementation quotes match the explicitly rolled model at every tested recovery point. However, low-value sells enable cheap cadence griefing.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1739) | 2026-08-19
