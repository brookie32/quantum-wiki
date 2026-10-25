---
title: "For Thirty Pieces of Silver: Overcoming Non-IID via ZKP Sample-Level Auditing and Forcing Attackers into Traitors in Federated Learning"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2611"
summary: "As a privacy-preserving distributed learning paradigm, federated learning faces severe security threats, especially data poisoning, gradient tampering, distributed attacks, and adaptive attacks. Exist"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

As a privacy-preserving distributed learning paradigm, federated learning faces severe security threats, especially data poisoning, gradient tampering, distributed attacks, and adaptive attacks. Existing gradient-based detection methods encounter three major bottlenecks in practical applications. First, they cannot distinguish between benign and malicious gradients under distributed attacks in non-IID scenarios. Second, defenders lack prior knowledge of trigger patterns. Third, attackers can launch adaptive attacks against these defense mechanisms. To address these challenges, we propose a novel defense paradigm. This paradigm shifts away from gradient detection, instead leveraging zero-knowledge proofs to conduct sample-level inspections on the local datasets of clients, eliminating the defense degradation caused by distributed attacks under non-IID settings. Then, through a staking mechanism, attackers are forced to train on discovered malicious samples with flipped labels, generating counter-gradients to neutralize hidden malicious samples, achieving targeted backdoor removal without requiring any prior knowledge of backdoor features. Furthermore, through zero-knowledge proof commitments, training gradients must be generated based on the same locked data. This prevents dynamic adaptive attacks based on reference model parameters and precludes gradient tampering. Experimental results demonstrate that under the highly non-IID setting of ext{Dir}(0.1), our proposed scheme successfully defends against distributed backdoor attacks and edge-case attacks on CIFAR-10, suppressing the attack success rate to below 6%. To the best of our knowledge, this is the first framework to achieve such defense results.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2611) | 2026-10-23
