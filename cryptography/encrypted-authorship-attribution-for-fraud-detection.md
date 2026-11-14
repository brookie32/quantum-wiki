---
title: "Encrypted Authorship Attribution for Fraud Detection"
date: "2026-11-12"
updated: "2026-11-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2876"
summary: "Authorship attribution techniques are routinely used to re- late anonymous or disputed texts to known authors through characteris- tic writing styles. Within the financial sector, such techniques may "
last_verified: "2026-11-14"
review_by: "2027-02-12"
stale: false
---

Authorship attribution techniques are routinely used to re- late anonymous or disputed texts to known authors through characteris- tic writing styles. Within the financial sector, such techniques may sup- port investigations of phishing campaigns, impersonation attempts, in- vestment scams, or other forms of fraud. More concretely, these methods can be leveraged to determine whether newly observed communications are linked to previously identified actors. In practice, however, both the communications under investigation and the intelligence databases used for attribution may contain sensitive information that cannot be shared across organizational boundaries. In this work, we investigate the privacy-preserving evaluation of sty- lometric authorship attribution through fully homomorphic encryption (FHE). We focus on Burrows’ Delta, a widely studied authorship attribu- tion method based on token frequency statistics and z-score comparisons. We present a homomorphic implementation of Burrows’ Delta, describe a motivating fraud-analysis scenario together with its threat model and trust assumptions, and then analyze the resulting computational com- plexity. Finally, we evaluate the practicality of the proposed approach us- ing the CKKS homomorphic encryption scheme and show that the com- plete pipeline can be executed without bootstrapping while maintaining high numerical accuracy. Our results demonstrate that stylometric au- thorship attribution constitutes a realistic target for privacy-preserving outsourced analytics and illustrate how homomorphic encryption can support confidential fraud investigations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2876) | 2026-11-12
