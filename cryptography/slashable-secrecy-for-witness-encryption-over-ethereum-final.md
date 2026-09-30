---
title: "Slashable Secrecy for Witness Encryption over Ethereum Finality"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2273"
summary: "Witness encryption over blockchain state aims to release a secret on a ledger condition without a key custodian. Validators with enough stake to construct a valid fork witness can obtain the secret al"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Witness encryption over blockchain state aims to release a secret on a ledger condition without a key custodian. Validators with enough stake to construct a valid fork witness can obtain the secret although the condition never holds on the canonical chain. They finalize a private fork that satisfies the condition, and keeping the fork hidden withholds the conflicting votes that slashing needs. We propose slashable secrecy to address this gap with Ethereum’s native slashing rules, without an additional key-custody committee or separate collateral. In executions where the condition never holds on the finalized canonical chain through completion, an information advantage yields evidence of those votes against keys the adversary controlled, or a solution to a designated hard problem. We give a construction from a witness KEM and prove slashable secrecy conditionally on its extraction interface. We bound the implicated historical stake under changing validator weights. For an archived Ethereum mainnet state, the historical evidence-weight floor exceeds 3.5 percent of its active stake, about 1.44 million ETH, under stated budget and coverage assumptions. Experiments on a synthetic Ethereum network confirm native processing of the evidence, without WE decryption. Two limitations remain. A witness KEM satisfying the full relation and extraction interface remains uninstantiated. Enforcement requires that the evidence is available, converted to native form and included while its signers remain eligible.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2273) | 2026-09-30
