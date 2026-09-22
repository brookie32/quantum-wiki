---
title: "Delta-KLPT^+: Improved Norm Bounds for the Quaternion Isogeny Path Problem and an Application to Ring Signatures"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2108"
summary: "Computing smooth-degree isogenies between supersingular elliptic curves with known endomorphism rings is a fundamental task in isogeny-based cryptography. Via the Deuring correspondence, this task is "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Computing smooth-degree isogenies between supersingular elliptic curves with known endomorphism rings is a fundamental task in isogeny-based cryptography. Via the Deuring correspondence, this task is equivalent to finding a connecting ideal of smooth norm between the corresponding quaternion maximal orders. KLPT-type algorithms address this problem by transforming a known connecting ideal into an equivalent ideal of smooth norm. Although connecting ideals of norm approximately p are expected to exist, the best known such algorithms for general input only achieve norm widetilde{O}(p^{4.5}). In this paper, we propose Delta-KLPT^+, a new KLPT-type algorithm that lowers this bound to widetilde{O}(p^4). Our construction builds on Delta-KLPT, which attains a smaller norm bound but requires two input ideals of the same prime norm. To extend Delta-KLPT to arbitrary inputs, we introduce a new subroutine IdealNormReduce, which reduces the common norm of an ideal pair. By iterating IdealNormReduce, we obtain two ideals with a common norm below p. Then we apply Delta-KLPT to the resulting ideal pair to obtain a desired connecting ideal of smooth norm. As an application, we construct Delfar, a fully anonymous isogeny-based ring signature scheme. Compared to Erebor-full, Delfar achieves shorter signatures and lower signing and verification costs for large rings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2108) | 2026-09-19
