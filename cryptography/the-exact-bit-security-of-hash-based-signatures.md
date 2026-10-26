---
title: "The Exact Bit Security of Hash-Based Signatures"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2626"
summary: "In this work, we analyze the security of hash-based signatures in Lean4. We examine how different ways of accounting for an adversary’s work yield different notions of bit security. As our working exa"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

In this work, we analyze the security of hash-based signatures in Lean4. We examine how different ways of accounting for an adversary’s work yield different notions of bit security. As our working example, we study two instances of XMSS with 128 bit digests. Under most of the accounting modes we consider, we get 127 bit security for strong unforgeability. However, under the most conservative convention that counts only the adversary’s direct random oracle queries, we only get 122 bits of security. We prove these bounds in the random oracle model without computational hardness assumptions and give matching attacks. We also prove a tight bound of 127 bits of strong unforgeability for SLH-DSA-128s. Our work is primarily motivated by recent autoresearch competitions, and it demonstrates the concrete impact of resource accounting. We hope that it helps designers of future challenges make an informed decision when choosing a notion of bit security that reflects their needs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2626) | 2026-10-24
