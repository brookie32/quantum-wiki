---
title: "A Unified Framework for Statistical Side-Channel Distinguishers: From Leakage Assessment to Key Recovery"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2041"
summary: "Side-channel analysis (SCA) has historically developed along two parallel research avenues: key recovery attacks (e.g., CPA, MIA, Templates) and leakage assessment methodologies (e.g., TVLA, t-tests, "
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Side-channel analysis (SCA) has historically developed along two parallel research avenues: key recovery attacks (e.g., CPA, MIA, Templates) and leakage assessment methodologies (e.g., TVLA, t-tests, F-tests, Kolmogorov-Smirnov tests). While both paradigms fundamentally process trace distributions partitioned by intermediate values or key hypotheses, they are typically viewed as disparate techniques with distinct mathematical formulations. In this paper, we propose a unifying statistical framework that decomposes side-channel distinguishers into orthogonal building blocks: (i) a subkey-induced leakage partition, (ii) a distribution comparison statistic (categorized into binary (two-distribution) or multi-class (multi-distribution) comparison operators), (iii) an aggregation operator over pairwise distribution comparisons, and (iv) a global decision rule. This formalization proves that classical key distinguishers and leakage tests are instances of a single generic model. Furthermore, our framework transforms statistical leakage tests into fully functional key recovery attacks, naturally introducing novel distinguishers based on non-parametric statistics (Kolmogorov-Smirnov, Anderson-Darling, MMD, Energy Distance) paired with suitable aggregation operators. We evaluate 18 statistical metrics across experimental configurations combining 8-bit AVR XMEGA and 32-bit ARM Cortex-M4 targets, unmasked and masked AES, under both targeted and automated POI scenarios. Our results demonstrate that the vast majority of these newly introduced attacks successfully achieve complete key recovery. Crucially, no single metric consistently dominates across all targets and leakage conditions, highlighting the complementary nature of statistical distinguishers and paving the way for metric combination and ensemble strategies.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2041) | 2026-09-15
