---
title: "Cryptanalysis of the DIZY Stream Cipher with Provable Security"
date: "2026-08-24"
updated: "2026-08-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1788"
summary: "With the increasing deployment of resource-constrained devices in daily life, ultra-lightweight ciphers become a necessity to tackle the security and privacy concerns in resource-constrained devices. "
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

With the increasing deployment of resource-constrained devices in daily life, ultra-lightweight ciphers become a necessity to tackle the security and privacy concerns in resource-constrained devices. In 2023, Gul and Kara studied the question of how to design a secure ultra-lightweight stream cipher with a small internal state, and introduced a new small-state stream cipher called DIZY. The cipher utilizes Truncated Pseudorandom Permutations (TPP) and has a provable security in the indistinguishability model. It consists of two versions, called DIZY-128 with a 128-bit key and DIZY-80 with an 80-bit key, respectively. In this paper, effective key recovery attacks on DIZY-80 and DIZY-128 are proposed. Both attacks leverage the weakness of DIZY that the attacker can easily reach a weak state in the middle of the initialization using chosen IVs. Based on constructing Hellman tables, the key recovery attacks on DIZY-80 and DIZY-128 are further improved. The cryptanalytic results show that DIZY-80/DIZY-128 can only provide a 65/86-bit security level against the key recovery attack, while it is claimed to provide an 80/112-bit security level by the designers. Finally, an improved variant of DIZY, called DIZYa, is proposed. The analysis on DIZYa shows that the improved variant can provide better security resistance against all known attacks including our attacks on DIZY, while maintaining the commendable characteristics of DIZY. This makes DIZYa a more suitable small-state stream cipher choice for resource-constrained devices like RFID tags.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1788) | 2026-08-24
