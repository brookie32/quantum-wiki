---
title: "Poisoned Cryptography: Solving Direct-Sum LIP in Half the Dimension"
date: "2026-09-30"
updated: "2026-10-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2281"
summary: "We analyse the Lattice Isomorphism Problem framework of Ducas and van Woerden when it is instantiated with the direct sum of two rescaled integral Barnes-Wall lattices, Lambda_{mathbf{S}}=gBW^{Z}_{m}o"
last_verified: "2026-10-03"
review_by: "2027-01-01"
stale: false
---

We analyse the Lattice Isomorphism Problem framework of Ducas and van Woerden when it is instantiated with the direct sum of two rescaled integral Barnes-Wall lattices, Lambda_{mathbf{S}}=gBW^{Z}_{m}oplus(g+1)BW^{Z}_{m}. All primitives of the framework share the same key pair, a public form mathbf{P}=mathbf{U}^{op}mathbf{S}mathbf{U} and a secret unimodular matrix mathbf{U}, so recovering mathbf{U} from mathbf{P} breaks each of them. We take the hash-and-sign signature scheme as an example, whose security rests on distinguishing the class of mathbf{S}=operatorname{diag}(g^{2}mathbf{R},(g+1)^{2}mathbf{R}) from that of the auxiliary form mathbf{Q}^{-1}=operatorname{diag}(mathbf{R},g^{2}(g+1)^{2}mathbf{R}). We show that the g^{2}-hull maps each of the two classes onto the other, is computable from the public key alone, and rescales the two blocks from (g, g+1) to (1, g(g+1)) without changing the automorphism group, so that solutions of the transformed instance lift back. The transformed instance then splits into two isomorphism problems for the public Barnes-Wall lattice in half the dimension. At d=1024, g=43 the estimated cost of key recovery drops from 220 to 124 classical bits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2281) | 2026-09-30
