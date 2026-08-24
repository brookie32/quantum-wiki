---
title: "A Practical Optimization for Wiedemann XL"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1787"
summary: "Wiedemann XL is a variant of the XL algorithm that has been widely used in algebraic attacks. Usually, the cost of applying Widemann XL is estimated as 3N^2 ω, where N is the width of the Macaulay mat"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Wiedemann XL is a variant of the XL algorithm that has been widely used in algebraic attacks. Usually, the cost of applying Widemann XL is estimated as 3N^2 ω, where N is the width of the Macaulay matrix, and ω is the average row weight of the Macaulay matrix. Among 3N^2 ω, 2N^2 ω is from the 1st phase of the algorithm, while N^2 ω is from the 3rd phase of the algorithm. This paper shows a practical optimization that reduces the cost of the 3rd phase by a huge factor so that its cost becomes essentially negligible compared to that of the 1st phase. Our optimization makes use of the fact that to obtain a solution of the multivariate system, only a small part of the kernel vectors is needed.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1787) | 2026-08-24
