---
title: "On the Fault Injection Security of White-box Ciphers"
date: "2026-08-29"
updated: "2026-08-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1833"
summary: "White-box security settings assume an extremely powerful adversary having full visibility and control of the software implementation and internal computations. Leakage-based attacks extract secret inf"
last_verified: "2026-08-30"
review_by: "2026-11-28"
stale: false
---

White-box security settings assume an extremely powerful adversary having full visibility and control of the software implementation and internal computations. Leakage-based attacks extract secret information via a local passive attacker (e.g., malware) and transmit it to a remote server. However, an active adversary, who can perform fault injections in a white box setting, has received limited attention, especially in the symmetric-key setting. In this paper, we initiate a formal study of active data-only adversaries in the white-box setting. Such adversaries preserve the control flow of the implementation but corrupt a bounded number of key-embedded lookup-table entries, enabling precise and repeatable manipulation of table values. Unlike leakage-based attacks, which are constrained by the bandwidth and existence of firewalls, such fault attacks can operate entirely locally. We focus on a data-only tampering adversary that preserves the control flow of the white-box implementation, but corrupts a bounded number of key-embedded lookup-table entries. Even under this stealth-preserving restriction, the adversary can cryptographically weaken the implementation and make faulty ciphertexts significantly easier to decrypt. We formalize such an active adversary by defining a new security notion and studying its impact on contemporary table-based white-box implementations. Our analyses reveal a structural disparity between two major design paradigms: Feistel-based white-box ciphers appear significantly more vulnerable to fault injection than SPN-based designs. Finally, we propose a software-based fault detection mechanism that detects fault injections with high probability, strengthening resilience. We provide detailed analysis of the SPN-based cipher WEM (the same analyses also work for other SPN-based ciphers like SPNbox), and two Feistel-based ciphers SPACE and Galaxy. Our analyses reveal that SPACE and Galaxy are significantly more vulnerable than WEM, under our fault-based security setting. Precisely, we show that WEM achieves high security under all the adversarial models, whereas SPACE and Galaxy instances can be attacked with a very high message recovery probability of 2^{-8}, when the adversary can choose the fault positions and the values and corrupts up to one fourth of the implementation table entries.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1833) | 2026-08-29
