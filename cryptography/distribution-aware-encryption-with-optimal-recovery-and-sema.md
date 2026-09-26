---
title: "Distribution-Aware Encryption with Optimal Recovery and Semantic Security"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2192"
summary: "Distribution-aware encryption seeks guarantees tailored to the probability law of the protected data and the secret key. We study simultaneous message-recovery, key-recovery, and target-distribution s"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Distribution-aware encryption seeks guarantees tailored to the probability law of the protected data and the secret key. We study simultaneous message-recovery, key-recovery, and target-distribution semantic security for arbitrary finite joint distributions, without assuming that messages and keys are independent. We represent encryption by a decomposition of the joint probability matrix and construct this decomposition through capacity-controlled randomized rounding. A stepwise conditional sampler turns the rounding process into a correct encryption algorithm without enumerating its output distribution or rejecting complete samples. Let p_star and q_star be the largest message and key probabilities. Our construction attains the exact message-recovery optimum max{p_star,q_star}, has key-recovery success below 2q_star, and provides O(sqrt{q_star}) advantage against prediction of every fixed Boolean message predicate. The semantic guarantee follows from negative correlation of the binary row-rounding remainders. We prove that the key-recovery factor cannot be uniformly improved while preserving exact message-recovery optimality, and that the semantic bound has the optimal worst-case order. We also establish additive robustness under distribution error and short-ciphertext existence by preserving only the moments needed for the security proof. The general sampler runs in expected polynomial time in the explicit rational input size; short ciphertexts do not by themselves imply efficient preprocessing or compact public descriptions. Structured sources admit additional efficient implementations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2192) | 2026-09-23
