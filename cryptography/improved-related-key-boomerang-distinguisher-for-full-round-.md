---
title: "Improved Related-Key Boomerang Distinguisher for Full-Round FUTURE"
date: "2026-09-04"
updated: "2026-09-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1891"
summary: "FUTURE is a lightweight block cipher with a 64-bit block, a 128-bit key and 10 rounds, proposed at AFRICACRYPT 2022 for low-latency hardware. This study analyzes FUTURE in the related-key setting with"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

FUTURE is a lightweight block cipher with a 64-bit block, a 128-bit key and 10 rounds, proposed at AFRICACRYPT 2022 for low-latency hardware. This study analyzes FUTURE in the related-key setting with a bit-level constraint model that carries the exact weights of the differential distribution table and the exact entries of the boomerang connectivity table, and whose objective function 2w_0 + 2w_1 + w_{bct} = -log_2(p^2q^2r) optimizes both sub-ciphers and the middle layer of the sandwich framework together. The model returns a full-round distinguisher whose objective function value 36 is optimal over all switching rounds and whose probability is P = hat{p}^2,ar{r},hat{q}^2 = 11dot 2^{-39} approx 2^{-35.54}, at a cost of 2^{37.54} queries under four related keys and 2^{37.54} XOR operations. Running it on the full cipher over 2^{44.34} quartets returns 341 right quartets and an experimental probability of 2^{-35.92}, in 63.9 hours on an ordinary personal computer; at the previous full-round probability 2^{-45.8} the same computer would take about 6.8 years. The distinguisher is therefore a practical one, and improves the best previously known full-round related-key boomerang distinguisher of FUTURE by a factor of 2^{10.26} in probability, in data and in time. An 8-round distinguisher placed into the unified key recovery framework further gives a full-round attack with 2^{51.05} data, 2^{64} time and 2^{64} memory, whose time complexity attains the optimum of the framework at any memory within the codebook and improves the best previously known attack by a factor of 2^{6}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1891) | 2026-09-04
