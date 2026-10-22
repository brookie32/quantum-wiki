---
title: "A Systematic Evaluation of Fault Attacks and Countermeasures on ML-DSA Rejection Sampling"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2567"
summary: "This paper presents a systematic evaluation of fault attacks on the rejection sampling of ML-DSA (FIPS 204) and of the countermeasures proposed against them. Using the identity (mathbf{Az} - ct = math"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

This paper presents a systematic evaluation of fault attacks on the rejection sampling of ML-DSA (FIPS 204) and of the countermeasures proposed against them. Using the identity (mathbf{Az} - ct = mathbf{Ay} - cdotmathbf{s}_2 = mathbf{r}), we prove that the quantity compared by the "third rejection test" of patent WO2025261784A1 is exactly (mathbf{r}_1), which is already produced during signing, while check 2 passing is what implies (mathbf{r}_1 = mathbf{w}_1). The third check therefore re-verifies a condition that check 2 guarantees, rather than being an independent test. We further show that the six embodiments claimed by the patent reduce to only two independent conditions, both covering only skips of the second check. An experiment with 30,000 fault injections confirms that all six embodiments detect the skip of the (mathbf{z})-norm check — the route that directly recovers the signing key (mathbf{s}_1) — at a rate of zero. Building on this blind spot, we fully recover (mathbf{s}_1) against a third-check-protected implementation (all 1024 coefficients of the four polynomials) under randomized signing, the default form in FIPS 204. We then report a complete evaluation matrix over three fault models and two implementation variants, and show that the third check and sign-then-verify are complementary with neither being sufficient on its own: the latter fails entirely against the second-check skip on the reference implementation (all faulty signatures pass verification), while the cheapest embodiment of the former detects every exploitable signature, whereas against the (mathbf{z})-check skip only sign-then-verify is effective. Their union covers every attack path we evaluate, and deploying either one alone leaves a complete attack path open. Overhead measurements show that this embodiment costs 0.04–0.05% of a signing on x86-64 and 0.83% on Cortex-M4, about 460–590 and 48 times less than sign-then-verify on the same platforms (22–24% and 40.0%, respectively). We therefore recommend deploying both, at a combined cost that is almost entirely sign-then-verify's.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2567) | 2026-10-20
