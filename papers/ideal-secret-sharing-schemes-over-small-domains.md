---
title: "Ideal Secret Sharing Schemes over Small Domains"
date: "2026-08-24"
updated: "2026-08-27"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1794"
summary: "In any secret sharing scheme, the size of each share must be at least as large as the size of the secret. Schemes that attain this lower bound are called k-ideal, where k is the size of the domain of "
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

In any secret sharing scheme, the size of each share must be at least as large as the size of the secret. Schemes that attain this lower bound are called k-ideal, where k is the size of the domain of the secrets and shares, or simply ideal if they are k-ideal for some k. An access structure is called k-ideal if it admits a k-ideal secret sharing scheme. The characterization of ideal access structures is a longstanding open problem at the intersection of cryptography, matroid theory, and information theory, previously solved only for k=2 and k=3. In this work, we solve this problem for k=4 and k=6. Our results exploit the connections between ideal secret sharing schemes and matroids and new techniques based on latin squares. For k=4, we show that an access structure is 4-ideal if and only if it admits a F_4-linear ideal secret sharing scheme, i.e., a scheme where the shares and the secret are elements of F_4 and the sharing and reconstruction functions are linear. To prove this result, we show that the class of matroids determined by ideal F_4-linear schemes coincides with those determined by 4-ideal schemes. For k=6, we prove that an access structure admits a 6-ideal scheme if and only if it admits a k-ideal scheme for every kgeq 2. This result shows that domains of size k=6 are the most restrictive domains for constructing ideal secret sharing schemes, and that 6-ideal schemes can be essentially built by combining ideal F_2-linear schemes with ideal F_3-linear schemes via the Chinese Remainder Theorem. Beyond these characterizations, our main technical contributions are the introduction of new techniques for analyzing ideal secret sharing schemes, extending the connections between ideal threshold schemes and latin squares to the general case, and the classification of the values of k for which some relevant matroids are k-entropic.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1794) | 2026-08-24
