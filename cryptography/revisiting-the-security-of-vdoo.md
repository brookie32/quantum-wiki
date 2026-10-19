---
title: "Revisiting the Security of VDOO"
date: "2026-10-18"
updated: "2026-10-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2528"
summary: "VDOO is a multivariate signature scheme submitted to the Next-generation Commercial Cryptographic Algorithms Program (NGCC). We study the security of its submitted parameter sets. In this paper, VDOO "
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

VDOO is a multivariate signature scheme submitted to the Next-generation Commercial Cryptographic Algorithms Program (NGCC). We study the security of its submitted parameter sets. In this paper, VDOO is described as a multilayer Rainbow construction. By retaining only its last oil space, we obtain a generalized UOV instance and apply existing wedge attacks. For the parameter set targeting 512-bit security, we estimate costs of 2^{432} and 2^{379} gates for the reconciliation and intersection variants, respectively. These estimates rely on the assumptions of the attack model and are below both the claimed security level and the attack costs reported in the specification. Our analysis uses only the generalized UOV structure. The additional information in the multilayer structure may allow further improvements. Our results also motivate further study of parameter choices that balance resistance to known attacks with signing efficiency.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2528) | 2026-10-18
