---
title: "Multidimensional Hill Cipher Substitution– Permutation Network"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1763"
summary: "MD-Hill-SPN is the first Hill-based construction to combine a multi-tier diffusion mix layer, a memory-hard KDF, and a simultaneous multi-metric empirical evaluation. Two independent runs of the full "
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

MD-Hill-SPN is the first Hill-based construction to combine a multi-tier diffusion mix layer, a memory-hard KDF, and a simultaneous multi-metric empirical evaluation. Two independent runs of the full metric suite yield: (a) full plaintext avalanche from round 1 (mean 63.97–64.67 of 128 bits, ideal 64); (b) the differential-probability sampling floor of 2 × 10−5 reached at round 4 (50,000 of 50,000 output differences distinct, both sessions); (c) algebraic-degree lower-bound saturation at the maximum observable value from round 1; (d) linear-bias indistinguishable from random (combined exceedance 4.40%, below the 4.55% noise floor); and (e) branch numbers at the Singleton (MDS) bound for every tier (B = 5 for 4 × 4, B = 9 for 8 × 8, B = 17 for 16 × 16), computed exhaustively over weight-1 inputs. MD-Hill-SPN therefore moves beyond theoretical construction to a construction that passes a defined empirical evaluation suite: avalanche, differential sampling, linear-bias probing, algebraic-degree lower bounds, and MDS branch numbers under single-key, known-plaintext conditions with fixed parameters, an evaluation no prior Hill cipher variant has reported in full.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1763) | 2026-08-21
