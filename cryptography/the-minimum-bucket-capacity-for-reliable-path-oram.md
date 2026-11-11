---
title: "The Minimum Bucket Capacity for Reliable Path ORAM"
date: "2026-11-08"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2820"
summary: "Path ORAM hides memory access patterns by storing N data blocks in a binary tree whose buckets have capacity Z, using a client-side stash for blocks that cannot be placed in the tree. Smaller buckets "
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Path ORAM hides memory access patterns by storing N data blocks in a binary tree whose buckets have capacity Z, using a client-side stash for blocks that cannot be placed in the tree. Smaller buckets reduce storage and communication costs but increase the risk of stash overflow. The revised Path ORAM analysis in 2014 established an exponentially decreasing stash overflow probability for Z geq 5. Experiments suggest small stashes at Z=4 and substantially larger ones at Z=3. However, it remained unknown whether Z=4 admits a uniform exponential stash bound or whether such a bound is impossible at Z=3. We establish a sharp threshold at Z=4 for binary Path ORAM with tree depth L=lceil log_2 N rceil. For Z=4, we prove that, uniformly over all database sizes and fixed access sequences, the stash size S after the final refill satisfies [ Pr[S>R] leq frac{23}{28}left(frac{5}{7}right)^R ] for every integer R geq 0. For Z=3, we exhibit a family of instances on which a single sequential scan of all N blocks produces a stash of size Omega(N) with probability bounded away from zero. Thus, four is the minimum bucket capacity admitting a uniform exponential stash bound: a logarithmic stash suffices for polynomial-length executions with inverse-polynomial failure probability at Z=4, whereas at Z=3 no sublinear stash can make the overflow probability vanish uniformly. Our proofs connect the actual Path ORAM process with dependent node loads to an auxiliary model with independent geometric node loads. This independence enables a recursive analysis of overflow that avoids the union bound over rooted subtrees used in the previous Z=5 proof. The main challenge is to transfer bounds from the auxiliary model to the actual process, which requires different techniques for the upper and lower bounds. For Z=4, we develop a two-stage randomization argument that bounds the actual process's exponential overflow moment by that of the auxiliary model. For Z=3, we develop a local continuous-time approximation with controlled errors that transfers an overflow surplus from the auxiliary model to the actual process, yielding the linear stash lower bound. Together, these arguments establish the sharp threshold at bucket capacity four.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2820) | 2026-11-08
