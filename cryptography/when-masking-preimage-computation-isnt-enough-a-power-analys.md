---
title: "When Masking Preimage Computation Isn’t Enough: A Power Analysis Attack on Masked Implementations of Falcon"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2313"
summary: "In this paper, we present a novel power analysis attack targeting a Falcon implementation protected by a masked preimage computation. By analyzing the ratio between the real and imaginary parts of the"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

In this paper, we present a novel power analysis attack targeting a Falcon implementation protected by a masked preimage computation. By analyzing the ratio between the real and imaginary parts of the public hash polynomial, we demonstrate that the leakage during the share recombination phase can be exploited to recover the secret key. We propose two attack variants: a chosen-message attack, where the adversary controls input messages to force extreme coefficient ratios, and a non-chosen-message attack that filters for naturally occurring vulnerable hashes. Through experimental evaluations using the ELMO leakage simulator for an ARM Cortex-M0 architecture, our experiments achieve a 98.3% success rate with 4,000 traces. Finally, while a fully masked implementation of Falcon prevents our attack, we propose a practical countermeasure based on rejection sampling to avoid the prohibitive computational overhead of a fully masked Gaussian sampler.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2313) | 2026-10-02
