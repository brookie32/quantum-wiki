---
title: "Automated Verification of Glitch- and Transition-Robust Composable Masked Circuits via Logic Simulations"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3022"
summary: "Power analysis attacks can extract sensitive information processed by electronic circuits. To mitigate information leakage, the most common approach is to transform the circuit using the masking count"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Power analysis attacks can extract sensitive information processed by electronic circuits. To mitigate information leakage, the most common approach is to transform the circuit using the masking countermeasure. Specifically, such a transformation replaces each circuit gate with a masked counterpart, known as a gadget. This process represents a key step in security-aware EDA flows and yields a provably secure circuit, provided that an efficient and provably composable secure gadget library exists. This work contributes to the automated verification of such gadgets, thereby enabling the systematic development of gadget libraries for secure hardware designs. Although several automated solutions exist for verifying the security of gadgets, particularly against glitch-induced leakages under the PINI security notion, an automated method for verifying the absence of joint leakages arising from both glitches and signal transitions, captured by the O-PINI security notion, remains lacking. To address this gap, this work introduces an automated procedure for checking whether a gadget satisfies O-PINI, and provides an analysis report covering the gadgets existing in the literature.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3022) | 2026-11-24
