---
title: "Backdooring the AI-Native Air Interface: One Poisoned Supply Chain Hijacks CSI Feedback and Beam Management"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2036"
summary: "The 5G-Advanced air interface is acquiring its first AI-native functions (AI/ML-based CSI feedback compression and beam management, studied by 3GPP since Release 18) and their models increasingly arri"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

The 5G-Advanced air interface is acquiring its first AI-native functions (AI/ML-based CSI feedback compression and beam management, studied by 3GPP since Release 18) and their models increasingly arrive through third-party supply chains. We present the first cross-use-case backdoor study of this interface. Poisoning as little as 0.5% of the training data implants an arbitrary trigger-to-target association into CRNet (and, at 5% poisoning, into CsiNet): attack success is 100% with no measurable clean cost, with physical triggers so weak that a 2-bit RIS suffices to launch them. The same trigger and pipeline hijack a second standardized function, beam prediction, with 99.5% success. Hijacked feedback steers gNB beamforming toward a phantom channel: a victim's rate falls by 98%, and the diverted beam concentrates 88% of the array-gain ceiling onto the attacker, raising interception probability to 100%. An adaptive attack that matches codeword statistics drives both statistical detectors from ≈1.0 to 0.53 AUC with attack strength unchanged, yet behavioral consistency still detects it: codewords can be disguised, behavior cannot.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2036) | 2026-09-15
