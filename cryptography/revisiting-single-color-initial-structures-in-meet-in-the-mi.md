---
title: "Revisiting Single-Color Initial Structures in Meet-In-The-Middle Attacks"
date: "2026-09-13"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1999"
summary: "The meet-in-the-middle (MITM) attack framework is one of the most powerful cryptanalytic techniques with broad influence to preimage, key recovery, and collision attacks. In this paper, we present two"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

The meet-in-the-middle (MITM) attack framework is one of the most powerful cryptanalytic techniques with broad influence to preimage, key recovery, and collision attacks. In this paper, we present two generic techniques. First, we observe that the constant space in MITM attacks is an exploitable source of degrees of freedom: its value-independence enables MITM-style partition and acceleration of attack subprocesses. With this intuition in mind, we revisit the single-color initial structure technique by Chen et al. at Asiacrypt 2025, and find an improved algorithm that relaxes the canonical optimization objective in automatic search for MITM attacks. Second, we extend the partial-target-preimage-to-collision conversion by Li, Isobe, and Shibutani at FSE 2012 used in MITM-based collision attacks to the settings of chosen-prefix collision and diamond structure construction. We demonstrate the practical relevance of our techniques by presenting a number of improved results in (pseudo-)preimage, (chosen-prefix) collision, and herding attacks on AES-like constructions over the state-of-the-art.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1999) | 2026-09-13
