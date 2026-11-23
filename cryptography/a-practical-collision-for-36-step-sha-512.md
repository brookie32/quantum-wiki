---
title: "A Practical Collision for 36-Step SHA-512"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2991"
summary: "We give a colliding message pair for SHA-512 reduced to 36 steps, starting from the standard initial value. To our knowledge it is the first practical collision for 36-step SHA-512; the previous pract"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

We give a colliding message pair for SHA-512 reduced to 36 steps, starting from the standard initial value. To our knowledge it is the first practical collision for 36-step SHA-512; the previous practical record was 35 steps. The attack is not new. It uses the 36-step differential characteristic and the memory-efficient two-block framework of Li et al. (ePrint 2026/1120), whose estimated time complexity is 2^{66.2}. Our contribution is to make it practical by: (i) counting the degrees of freedom and the uncontrolled conditions more precisely; (ii) re-solving (A_0, E_4) on the fly for each first block, which makes the cost of the first block negligible; and (iii) a meet-in-the-middle lookup on 19 bits of E_{16} whose table fits in the GPU's L2 cache. The collision was found after about 3 hours of wall-clock time on three NVIDIA Blackwell GPUs (one RTX 5090 and two RTX PRO 6000), i.e. about 8.9 GPU-hours. At the compression-function throughput we measured on the same hardware, this equals about 2^{49.2} evaluations of the 36-step compression function. The measured stage-by-stage pass rates agree with the cost model; for example, the step-22 survivors that also satisfy elta W_{23} number 9, against 9.3 expected. We verified the pair with an independent implementation, and independently re-measured the tail probabilities on 2dot 10^{10} generated message pairs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2991) | 2026-11-23
