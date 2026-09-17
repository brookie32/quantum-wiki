---
title: "Robust Side Channel Analysis with Blocking and Quantification of Leakage"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2023"
summary: "While an abundance of SCA methodologies have arisen over the years with impressive theoretical backgrounds, they fail to take into account some important real-world aspects in the analysis. Most of th"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

While an abundance of SCA methodologies have arisen over the years with impressive theoretical backgrounds, they fail to take into account some important real-world aspects in the analysis. Most of them fail on three key points. First, most assume IID or normally distributed data points in their framework without verifying that the experimental setup indeed meets that requirement. Second, most methods rely on visual aspects or failed statistical tests to define the success or failure of the tests without quantifying the precision of their measurement with formal boundaries. Third, in most cases, the test harness is not completely oblivious to the secret data, remaining completely free of data-dependent branching, conditional formatting, or conditional triggering, which can leak environmental noise and contaminate the data points. We are proposing a new SCA methodology, which we named BLAQ, to bridge this gap between the theoretical mathematical models and the real-world imperfect testing environment.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2023) | 2026-09-14
