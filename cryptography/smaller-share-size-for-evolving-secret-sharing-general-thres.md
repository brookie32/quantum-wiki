---
title: "Smaller Share Size for Evolving Secret Sharing: General Thresholds and Threshold Three"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2619"
summary: "Evolving secret sharing allows participants to join indefinitely without modifying previously distributed shares. We study the share size of perfectly secure evolving threshold secret sharing schemes "
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Evolving secret sharing allows participants to join indefinitely without modifying previously distributed shares. We study the share size of perfectly secure evolving threshold secret sharing schemes and obtain two improvements. For general thresholds, we introduce a polynomial sharing method that shares two secrets with adjacent reconstruction thresholds using one polynomial. Combining this method with the evolving scheme of Cheng et al. (ASIACRYPT 2025), we obtain an evolving k-threshold scheme whose t-th share has size [ leftlfloor frac{k}{2} rightrfloor log_2 t + O_k!left(ell+log_2log_2 tright) ] bits for an ell-bit secret. This reduces the leading coefficient of their general construction from k-1 to lfloor k/2rfloor. For threshold three, we give a separate construction that reduces the lower-order terms of the scheme of Cheng et al. We mask the short shares in all generations with the same random ell-bit value R, which is shared through an evolving 2-threshold scheme, we obtain [ log_2 t+(2+o(1))log_2log_2 t ] bits per share for fixed ell. Both constructions satisfy correctness and perfect information-theoretic security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2619) | 2026-10-23
