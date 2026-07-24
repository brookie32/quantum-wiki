---
title: "Proof of Demand Is Not Proof of Work: On the Limits of Demand-Weighted Consensus under Free Pseudonyms"
date: "2026-07-21"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1492"
summary: "Proof-of-useful-work (PoUW) certifies computational hardness, not utility: a certified computation need not be anyone's demanded job. We separate three properties of a work receipt — work soundness (m"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

Proof-of-useful-work (PoUW) certifies computational hardness, not utility: a certified computation need not be anyone's demanded job. We separate three properties of a work receipt — work soundness (mathsf{W}), job binding (mathsf{B}), and demand exogeneity (mathsf{E}) — and locate the gap at mathsf{E}. Two results are unconditional. First, payments between coalition-controlled requesters and workers are recoverable transfers that contribute no Sybil-resistant cost, so no security lower bound may count them (Lemma 1). Second, under free pseudonyms and endogenous observation a coalition can simulate the receipts of economically independent requesters, so endogenous receipts cannot certify mathsf{E} (Theorem 1); we lower-bound the cost of evading a stated class of provenance estimators. Building on these, a robustness bound: because a permissionless mechanism must remain live on the zero-demand path, its leader-election floor cannot depend on the demand component of service receipts (Theorem 2), and any admissible receipt boost is quantitatively capped. Fork-independent salvage value of useful outputs can leave security neutral, negative, or positive depending on salvage asymmetry and demand, which we characterize in a stylized free-entry model. Constructively, an irrecoverable tax on every settled payment makes the burn — not proof of independence — the security resource. Deployed evidence comprises one reported audit (Pearl cuPOW) and a reward-program farming analogue; the election-side failure is, at present, a model prediction. Useful-computation receipts are appropriate instruments for payment, collateral, and loss allocation — and a bounded, priced election boost — but not the leader-election floor.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1492) | 2026-07-21
