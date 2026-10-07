---
title: "Comparative Evaluation of Open-Source Gröbner Basis Implementations for Small-Scale AES Polynomial Systems over GF(2)"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2364"
summary: "The practical performance of Gröbner basis implementations depends on the polynomial systems being solved. This work evaluates 20 open-source imple- mentations with Magma as a proprietary reference on"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

The practical performance of Gröbner basis implementations depends on the polynomial systems being solved. This work evaluates 20 open-source imple- mentations with Magma as a proprietary reference on systems derived from small-scale AES over GF(2). The Easy, Medium, and Hard experiments use field equations and ten input instances each, comparing wall-clock runtime, peak memory, success rate, and CPU usage. Implementations with no successful runs are excluded from subsequent experiments. In Hard, msolve and Singular’s slimgb completed all ten runs successfully, with mean runtimes of 164 and 269 seconds and mean peak memory consumption of 3693 and 4343 MiB, respectively, com- pared with 319 seconds and 16853 MiB for Magma. During these runs, msolve used an average of 13.4 CPU cores, while slimgb and Magma used about one core each. Magma had the shortest mean runtime in Medium, whereas msolve was fastest in Easy and Hard. Changing the plaintext-ciphertext pair count affected implementations differently, and runtimes varied between instances. The results show that open-source implementations can be competitive alternatives to Magma, with their relative performance depending on the input systems.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2364) | 2026-10-05
