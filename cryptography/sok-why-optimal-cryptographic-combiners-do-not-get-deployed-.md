---
title: "SoK: Why Optimal Cryptographic Combiners Do Not Get Deployed: Security, Complexity, and Adoption of Hybrid KEMs"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1754"
summary: "XtM (XOR-then-MAC) is provably optimal against quantum adversaries. As of March 2025, no production cryptographic library implements it. HKDF, with weaker security guarantees, is deployed in 91% of th"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

XtM (XOR-then-MAC) is provably optimal against quantum adversaries. As of March 2025, no production cryptographic library implements it. HKDF, with weaker security guarantees, is deployed in 91% of the 44 libraries we examined. This gap is not accidental. This Systematization of Knowledge (SoK) introduces the (A, P, phi) framework to explain it: A measures authentication strength, P measures IETF standardization maturity, and phi measures implementation complexity. To our knowledge, this is the first falsifiable, quantitative model predicting cryptographic adoption grounded in observable software engineering indicators. We apply this framework to seven combiner families and 44 cryptographic libraries, validate phi against measured integration LOC across 9 real-world repositories, and derive predictions verifiable by 2028. Our evidence suggests that implementation complexity is a first-order explanatory factor in cryptographic adoption. The most deployable construction is not the most secure one in isolation: it is the most secure one engineers can integrate, audit, and maintain at scale.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1754) | 2026-08-20
