---
title: "Stable Private Intersection with Consistency"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3069"
summary: "Private set intersection (PSI) enables two mutually distrusting parties to learn only the intersection of their private sets. Malicious security for PSI, however, constrains how a party computes and n"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Private set intersection (PSI) enables two mutually distrusting parties to learn only the intersection of their private sets. Malicious security for PSI, however, constrains how a party computes and not which inputs it computes on. A party running multiple PSI sessions can use different inputs each time or change its inputs across sessions to bias the output or infer more information from the intersection. Recent work binds parties to committed sets [Goel et al., USENIX Security 2026; Sun et al., CCS 2024, 2025] but gives the sender only weak input consistency. That is, the sender cannot inject elements but it can omit any elements from the intersection. Omitting elements causes (1) false negatives (i.e., an element in both sets is silently dropped from the intersection) and (2) biased outputs (i.e., the sender picks which intersection elements each receiver gets). We introduce Stable Private Intersection with Consistency (SPICy), a framework that binds both parties to their exact committed input sets across an unbounded number of intersections. We define two notions of input consistency: (1) strong input consistency (SIC) wherein each party uses its full committed set, though the receiver's output may still differ from the intersection of the committed sets; (2) complete input consistency (CIC) wherein the receiver's output is the exact intersection of the committed sets. SPICy builds on MiniPSI [Rosulek and Trieu, CCS 2021], the fastest known small-set PSI protocol, through a new primitive, the Mutual Oblivious PRF (MOPRF). In an MOPRF, both parties evaluate a PRF under their own keys, and the receiver learns the sender's output only on elements held by both parties. SPICy achieves CIC for both the sender and receiver and requires a single round of online communication. We implement SPICy in Rust and evaluate it end-to-end on deployed PSI applications. For sets of sizes between 2⁷ and 2¹⁰, SPICy has 1.7–1.9× online runtime overhead and around 4.5× communication overhead compared to MiniPSI.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3069) | 2026-11-26
