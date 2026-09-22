---
title: "Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Limited Architecture Knowledge Setting"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2127"
summary: "Deep Neural Networks (DNNs) have emerged as a cornerstone of modern AI systems, rendering their internal parameters highly valuable intellectual property. Consequently, the security of DNNs against mo"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Deep Neural Networks (DNNs) have emerged as a cornerstone of modern AI systems, rendering their internal parameters highly valuable intellectual property. Consequently, the security of DNNs against model extraction attacks has garnered significant research attention. Recent cryptanalytic extraction methods have demonstrated that recovering DNN parameters is feasible in polynomial time, both when attackers have exact logit access and in the more restrictive hard-label setting. However, a critical limitation of these state-of-the-art frameworks is the assumption that the attacker possesses a complete architecture knowledge of the target network, including the exact depth and width of the hidden layers. To date, the efficacy of parameter extraction algorithms under limited architecture knowledge remains unexplored. This paper demonstrates that in the limited architecture knowledge scenario, existing cryptanalytic attacks suffer from neuron omission, which causes subsequent parameter recovery to fail entirely. To address this, we propose a general adaptive extraction workflow integrated with a novel error detection algorithm capable of identifying missing neuron anomalies and successfully recovering the correct parameters. Through experiment, we achieve the first successful extraction of a four-hidden-layer ReLU network (comprising over 1.1 million parameters) trained on CIFAR-10 under the limited architecture knowledge setting, while maintaining a 100% error detection recall.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2127) | 2026-09-20
