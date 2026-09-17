---
title: "Silent Payments, Formally: Security, Scanning Costs, and Blind Collaborative Payments"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2037"
summary: "Silent payments (BIP-352) let Bitcoin users publish one static address and receive at fresh, unlinkable outputs. The protocol already ships in major wallets, yet its own specification concedes it has "
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Silent payments (BIP-352) let Bitcoin users publish one static address and receive at fresh, unlinkable outputs. The protocol already ships in major wallets, yet its own specification concedes it has no formal security proof—and 2026 brought a worst-case scanning attack, a funds-locking hardware-wallet disclosure, and an omitted-payment bug. We supply the missing analysis. Receiver and co-transactor unlinkability are proved under DDH, with the label system as a corollary that includes an executable linking attack and its fix. We then quantify what scanning costs and what an attacker can buy with it. The community's K_max cap turns quadratic attack amplification into linear; every compliant scanner needs Ω(N+KM) work; our set-probing scanner meets this bound and runs 39× faster in our measurements; and a year of fee data prices a full-block attack as low as 0.0015 BTC. For collaborative transactions we show what the specification's warning was about (the transaction assembler can always identify the recipient's output, and malformed partial secrets burn payer funds, the failure class disclosed in August 2026), and we construct the variant the warning called for: blind collaborative payments with information-theoretic payer privacy. Delegation, finally, offers no safe default: scanning servers either learn too much or can hide payments. A twelve-experiment benchmark suite accompanies the paper.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2037) | 2026-09-15
