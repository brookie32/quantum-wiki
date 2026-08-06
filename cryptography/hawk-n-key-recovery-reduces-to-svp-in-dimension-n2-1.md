---
title: "HAWK-n Key Recovery Reduces to SVP in Dimension n/2 + 1"
date: "2026-08-03"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1593"
summary: "HAWK is a lattice signature scheme that is currently a third-round candidate in NIST's post-quantum signature competition. We give an unconditional, deterministic polynomial-time reduction from HAWK-n"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

HAWK is a lattice signature scheme that is currently a third-round candidate in NIST's post-quantum signature competition. We give an unconditional, deterministic polynomial-time reduction from HAWK-n key recovery over K_n=Q(zeta_{2^ell}) to poly(n) calls to an exact Shortest Vector Problem (SVP) oracle in dimension n/2+1, where n=2^{ell-1} is the ring degree. The reduction uses a nontrivial automorphism of the key lattice, supplied by the Galois involution au:zetamapsto-zeta and recoverable as a shortest vector of a public rank-n lattice isometric, up to scaling, to Z^{n/2+1}oplussqrt{2},Z^{n/2-1}. Ducas's block reduction on this near-hypercubic class finds the automorphism, and the descent of van Gent and Pulles recovers the key from it. In the gate-count model, the attack lowers the key-recovery cost of HAWK-512 from 2^{150} to 2^{108} and of HAWK-1024 from 2^{288} to 2^{182}. We demonstrate this with a practical implementation that recovers a HAWK-256 secret key end-to-end in a few hours on a single server. The construction does not transfer to Falcon. Conductors min{p^k,2p^k} (p an odd prime), i.e. the m>4 with cyclic (Z/m)^imes, evade the attack.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1593) | 2026-08-03
