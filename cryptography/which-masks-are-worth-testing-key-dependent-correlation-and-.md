---
title: "Which Masks Are Worth Testing? Key-Dependent Correlation and Symmetry in Lightweight Block Ciphers"
date: "2026-11-21"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2977"
summary: "The quality of a differential--linear candidate and the cost of selecting one are separate questions. We study both in reduced-round lightweight block ciphers. First, for 11-round CRAFT, we compare an"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

The quality of a differential--linear candidate and the cost of selecting one are separate questions. We study both in reduced-round lightweight block ciphers. First, for 11-round CRAFT, we compare an alternative output mask with the published mask of Zhou et al. at the same input difference. In a paired study with 128 master keys, the alternative increases the observed mean signed correlation by factors of 1.69 to 1.86 across four tweak settings. Approximate simultaneous 95% confidence intervals for the four mean differences lie above zero. A separate held out study of ranking rules selects two distinct masks and gives inconclusive simultaneous intervals for detection-rate gains at a fixed data budget. Second, for restricted two-round linear sections, we use cell permutations to identify masks with the same distribution of absolute correlation over keys. We observe reductions in the number of evaluated masks in MIDORI-64 and QARMA-64. For three symmetric QARMA-64 cases, 81 masks reduce to 21, 45, and 36 representatives. Exact evaluation agrees with exhaustive search for RMS, stability, lower-tail, and threshold coverage objectives. The tested coordinate-permutation family gives only the identity in the selected SKINNY-64-64 section.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2977) | 2026-11-21
