---
title: "Geometric Forgeries: Structural Cryptanalysis of MAYO"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2247"
summary: "MAYO is a post-quantum signature scheme based on UOV that uses the whipping transformation to achieve more compact public keys and retain efficient signing. We present the first structural forgery att"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

MAYO is a post-quantum signature scheme based on UOV that uses the whipping transformation to achieve more compact public keys and retain efficient signing. We present the first structural forgery attack that exploits the geometry of the resulting multivariate quadratic (MQ) maps. Our starting point is the observation that whipping amplifies polar cancellations in the underlying MQ map, producing subspaces with low-dimensional quadratic and polar images. We combine this geometric insight with the Pseudo-Oil Attack (ASIACRYPT 2026) and a descent to the binary field into a structural forgery algorithm. Independently, we introduce a multi-target reduction for homogeneous MQ maps. Projecting onto a quotient of the codomain reduces the number of equations, and homogeneity allows suitable solutions to be rescaled to the original targets. Concretely, the combination of our forgery attacks lowers the estimated bit security of the Security Level I and III parameter sets of MAYO Round 2 by roughly 18 and 16 bits, respectively. In particular, the Level I parameter set falls 15 bits short of its required security level. For the recently released MAYO Round 3 parameters, our attack still reduces the estimated security by roughly 6, 4 and 2 bits for the new MAYO1, MAYO2 and MAYO3 respectively, bringing MAYO2 below the required security by 3 bits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2247) | 2026-09-28
