---
title: "On FROST and Unconditional LDVR Security"
date: "2026-09-24"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2203"
summary: "Inspired by the recent polynomial-time adaptive attacks on threshold Schnorr signatures, we contextualize the Low-Dimensional Vector Representation (LDVR) assumption and its impact on relevant thresho"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Inspired by the recent polynomial-time adaptive attacks on threshold Schnorr signatures, we contextualize the Low-Dimensional Vector Representation (LDVR) assumption and its impact on relevant threshold Schnorr signature schemes. Our analysis focuses in large part on FROST, a widely deployed threshold Schnorr signature scheme. However, our analysis is applicable to any relevant threshold Schnorr signature scheme, such as Lindell's three-round threshold Schnorr protocol. We show that for cases where FROST is used with 131 parties and fewer, and for parameter choices of 128-bit generic (discrete log) security, FROST is secure for any signing threshold. This bound increases to 260 parties for parameter choices of 256-bit security; our analysis similarly can be extended to other parameter choices. This bound assumes the best possible LDVR adversary, even more powerful than the results by Rodríguez García and Tessaro. In other words, for real-world uses of FROST with parameter choices of 128-bit security, and with a small (131 and fewer) number of parties, the security of FROST is determined entirely by the hardness of the Algebraic One-More Discrete Logarithm (AOMDL) assumption, as LDVR is unconditionally hard for this parameter regime. It is an open research question whether the concrete attacks given by Rodríguez García and Tessaro can be improved to approach the unconditional LDVR security bound considered in our analysis. We then show for each additional party for 132 total number of signers and greater, again for parameter choices of 128-bit generic security, the resulting security of FROST is at worst reduced by approximately one bit (or less) of security for the worst-case choice of corruption threshold. This analysis can be used by practitioners to determine the worst possible security of even large-scale FROST deployments. Finally, we give two variants to FROST that build upon prior masking techniques to allow for full adaptive security. The first variant allows for masking keys to be derived from Diffie-Hellman identity keys, allowing for constant memory overhead, at the tradeoff of increased computation. The second variant allows for a 50% reduction in memory overhead for storage of pairwise masking keys, by employing symmetric key predistribution techniques.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2203) | 2026-09-24
