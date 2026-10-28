---
title: "Tractable, Not Truncated: Colored-Noise TRNG Security via Fractional Brownian Motion"
date: "2026-10-27"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2662"
summary: "Oscillator-based true random number generators derive randomness from timing fluctuations driven by thermal and flicker noise, and flicker gains weight as technology advances and transistors shrink. I"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

Oscillator-based true random number generators derive randomness from timing fluctuations driven by thermal and flicker noise, and flicker gains weight as technology advances and transistors shrink. Its long memory leaks information about past, which existing models either discard or truncate, overstating security. We introduce a rigorous and tractable framework for colored noise, including the white and flicker noise of oscillators. We model the oscillator phase by fractional Brownian motion and prove a quasi-renewal property: the phase uncertainty left after conditioning on the entire past depends only on the elapsed time. This yields closed-form worst-case min-entropy and sampling requirements. We also extend spectral and Allan-variance analysis to finite samples, so the noise parameters are estimated consistently from a single timing trace. The pipeline from measurement to sampling requirement is closed-form and needs no simulation. Experiments across FPGA and ASIC platforms show that flicker dominates: its variance meets white noise within about 100 cycles and accounts for more than 99% of uncertainty behind the targeted 0.99 min-entropy rate. Methods relying exclusively on thermal noise require adjustment or redesign: incorporating flicker noise enables a two-to-three orders of magnitude increase in bitrate.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2662) | 2026-10-27
