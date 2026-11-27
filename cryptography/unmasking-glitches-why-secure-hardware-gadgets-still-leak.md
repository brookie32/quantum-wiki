---
title: "Unmasking Glitches: Why Secure Hardware Gadgets Still Leak"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3030"
summary: "Probing-based security notions underpin the design and verification of masked hardware. Glitch-aware extensions, such as the robust probing model, provide strong guarantees within their abstraction an"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Probing-based security notions underpin the design and verification of masked hardware. Glitch-aware extensions, such as the robust probing model, provide strong guarantees within their abstraction and enable systematic gadget constructions and automated verification. Yet these guarantees do not preclude physically observable leakage: prior work shows that temperature or voltage manipulations can still induce leakage, often blamed on transient glitches without a clear root cause. To clarify, we perform a gate-level evaluation of three representative masked AND gadgets, namely HPC2, HPC3, and COMAR, under timing perturbations induced by input transitions, clock skew, and temperature variation. Our results show that these seemingly different factors share a common mechanism: they create timing differences in signal arrivals, which in turn alter glitch onset, duration, and propagation. We introduce three metrics to determine whether a glitch can reveal sensitive value-dependent behavior: (1) change of glitch behavior across sensitive equivalence classes, (2) variation of glitch timing with the sensitive value, and (3) recurrence of glitches on the same internal node for one sensitive value but not another. Using these metrics, we show that timing perturbations can induce reproducible, sensitive-value-dependent glitches that indicate potential vulnerabilities. We support these observations with HSPICE supply-current NICV and correlation analyses, as well as post-route glitch-only NICV. We further complement the simulation study with the first-of-its-kind post-silicon optical probing measurements that support the same timing-difference mechanism in secure gadgets. Overall, our results show that even gadgets with formal probing security and composability guarantees can exhibit observable, data-dependent glitch patterns, motivating timing-aware refinement layers for secure hardware evaluation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3030) | 2026-11-24
