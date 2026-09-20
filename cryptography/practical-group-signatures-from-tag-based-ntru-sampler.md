---
title: "Practical Group Signatures from Tag-Based NTRU Sampler"
date: "2026-09-18"
updated: "2026-09-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2077"
summary: "The post-quantum migration for key agreements and signatures being well underway, the focus naturally shifts to other properties and primitives that still lack efficient solutions. One such area is th"
last_verified: "2026-09-20"
review_by: "2026-12-19"
stale: false
---

The post-quantum migration for key agreements and signatures being well underway, the focus naturally shifts to other properties and primitives that still lack efficient solutions. One such area is that of privacy-enhanced primitives, with a growing number of post-quantum constructions. Among the most fundamental are group signatures, which represent an important milestone of anonymity and accountability towards more involved designs. However, despite recent progress, most compact lattice constructions are either computationally intensive or suffer large key materials, or both. In this paper, we introduce a new lattice group signature scheme that reaches compact signatures and keys, while being runtime-efficient in all its procedures. Our key element is a new tag-based gadget sampler that properly interfaces with NTRU, then benefiting from the desirable properties of such trapdoor frameworks for advanced constructions while leveraging the compactness of NTRU. Although applied to group signatures, our sampler may be of independent interest and used for more expressive privacy-driven primitives like anonymous credentials. We also introduce two assumptions, which can be seen as hybrid versions of NTRU and ISIS, that independently underly the security of our group signature. Despite their similarities with the recently introduced NTRU-ISIS_f assumption, they appear strictly harder and even admit reductions from R-ISIS in some parameter settings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2077) | 2026-09-18
