---
title: "MuCPay: Breaking the Quadratic Bottleneck in Scriptless Multi-Party Oracle-Based Conditional Payments"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2732"
summary: "Oracle-based conditional payments triggered by real-world events support decentralized finance applications. However, dense independent bilateral deployments require Theta(Nn^2) outcome authorizations"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Oracle-based conditional payments triggered by real-world events support decentralized finance applications. However, dense independent bilateral deployments require Theta(Nn^2) outcome authorizations and Theta(n^2) settlement signatures for n parties and N outcomes. To go beyond two-party settings, we propose MuCPay, a multi-party oracle-based conditional payment protocol combining (i) Theta(Nn) off-chain signing shares with one on-chain settlement signature and (ii) BIP340-compatible scriptless settlement on Bitcoin. At its core, MuCPay introduces hash-bound adaptor multi-signatures (HB-AMS) that aggregate parties' conditional authorizations into a compact joint pre-signature. Its single-nonce structure and hash-bound adaptor integration enable efficient multi-party pre-signing. Unlike Double-Layer AMS (EuroS&P'26), HB-AMS produces a standard BIP340 signature under an aggregate public key, enabling direct Taproot key-path settlement. Under static corruption with one honest signer, we prove concurrent new-message unforgeability (CUF) and early-settlement resistance (ES) under our stated algebraic random-oracle model. For 128 parties and 16 outcomes, median complete local preparation takes AuditFullPrepare~s. For protocol preparation (AuditProtocolPrepare s for MuCPay), native-profile projections place VweTS (NDSS’23) and ParaSwap (USENIX’25) work at 1.67 × 10⁴ and 5.05 × 10⁵ times MuCPay's, respectively. Settlement uses one 64-byte signature, while the modeled independent-DLC deployment requires 281.5× as many transaction vbytes. These results demonstrate practical, scalable multi-party oracle-based conditional payments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2732) | 2026-11-03
