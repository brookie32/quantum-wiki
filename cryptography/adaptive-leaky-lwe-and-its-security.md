---
title: "Adaptive Leaky LWE and Its Security"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2837"
summary: "The Leaky LWE problem, proposed by Lai, Swarnakar, and Woo (CiC '25), studies whether LWE samples remain pseudorandom in the presence of noisy linear information about their secrets and errors. In Lea"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

The Leaky LWE problem, proposed by Lai, Swarnakar, and Woo (CiC '25), studies whether LWE samples remain pseudorandom in the presence of noisy linear information about their secrets and errors. In Leaky LWE, the leakage matrix may depend on the public matrix, but must be chosen before the LWE challenge is revealed. We study t-round adaptive Leaky LWE, where each leakage matrix may depend on the challenge and all preceding leakage answers. Under explicit norm, smoothing, and sampling conditions, we reduce Gaussian-secret LWE to this problem at the corresponding source parameters for polynomially many rounds. The reduction preserves the public-matrix distribution and access to its correlated oracle, and supports rectangular leakage matrices and non-spherical discrete Gaussians over arbitrary orders in number fields.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2837) | 2026-11-09
