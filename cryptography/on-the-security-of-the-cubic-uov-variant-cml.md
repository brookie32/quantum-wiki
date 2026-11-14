---
title: "On the Security of the Cubic UOV Variant CML"
date: "2026-11-12"
updated: "2026-11-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2872"
summary: "CML is a cubic multivariate signature scheme proposed over F_q with q = 2^8. Earlier cubic Oil--Vinegar variants such as CUOV and CSSv were broken by differential and high-rank attacks. CML adds an el"
last_verified: "2026-11-14"
review_by: "2027-02-12"
stale: false
---

CML is a cubic multivariate signature scheme proposed over F_q with q = 2^8. Earlier cubic Oil--Vinegar variants such as CUOV and CSSv were broken by differential and high-rank attacks. CML adds an ell-invertible cycle system and a secret position-hiding map to hide the cubic positions. We show that the cubic homogeneous parts of the public key span a space of dimension at most two, so a publicly derived output combination has degree at most two. After restriction to the oil-direction space, the polar matrices of the publicly derived quadratic components span rank-two matrices associated with the edges of a path. This structure yields a procedure for recovering an equivalent key. Our implementation recovered an equivalent key in under 5~minutes for each tested parameter set, including the set targeting 256-bit security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2872) | 2026-11-12
