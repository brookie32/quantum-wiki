---
title: "Enhanced Differential-Linear Cryptanalysis of ChaCha Based on Bit Puncturing"
date: "2026-08-30"
updated: "2026-09-02"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1837"
summary: "ChaCha is one of the most extensively deployed symmetric ciphers. The security margin of ChaCha is directly related to the safety of many widely used lightweight security protocols and operating syste"
last_verified: "2026-09-02"
review_by: "2026-12-01"
stale: false
---

ChaCha is one of the most extensively deployed symmetric ciphers. The security margin of ChaCha is directly related to the safety of many widely used lightweight security protocols and operating systems for constrained devices, such as TLS 1.3, SSH, Noise, WireGuard, S/MIME 4.0, Linux, Android, Chromium/Chrome, Firefox and Safari. This paper introduces a novel extit{guessed key covering technique}. The objective of this technique is to identify partitioning-based functions whose required key bits are covered by those guessed for bit puncturing-based functions, enabling them to be processed jointly. Building on this, we propose a refined framework for differential-linear cryptanalysis of ChaCha called exttt{ReBitP}, which combines the ideas of the bit puncturing technique, the partitioning technique and a two-phase distillation strategy. The key insight of exttt{ReBitP} is to incorporate a carefully selected set of functions that are evaluated using the partitioning technique with different tail lengths into the first phase, without requiring additional key bits to be guessed. This early filtering via parity checks simultaneously lowers the time cost of the first phase and the time complexity of constructing the distillation table in the second phase. As applications, enhanced key recovery attacks on 7- and 7.5-round ChaCha256 are presented, achieving time complexities of 2^{142.08} and 2^{242.02}, respectively. The cryptanalytic results are 2^{6.12} and 2^{1.58} times faster than the existing attacks, respectively. So far as we know, these are the best known key recovery attacks on 7- and 7.5-round ChaCha256. This definitely demonstrates the superiority of the refined framework exttt{ReBitP}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1837) | 2026-08-30
