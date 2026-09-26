---
title: "Lifting Symmetries for Dimension Reduction in Module-LIP: rank 2 and rank 4"
date: "2026-09-24"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2198"
summary: "The module lattice isomorphism problem (module-LIP), introduced with HAWK, has attracted growing interest. Its most studied case is {mathcal O_{L}}^2-LIP, underlying HAWK key recovery, where L is a po"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

The module lattice isomorphism problem (module-LIP), introduced with HAWK, has attracted growing interest. Its most studied case is {mathcal O_{L}}^2-LIP, underlying HAWK key recovery, where L is a power-of-two cyclotomic field and {mathcal O_{L}} its ring of integers. Three recent independent algorithms reduce this 2n-dimensional problem to polynomially many exact-SVP calls: the Claude-derived algorithm uses dimensions at most n/2+1, and the ChatGPT-derived and Mureau--Pellet-Mary algorithms use 3n/4+1. These improve Ducas's generic mathbb ZLIP bound n+1 (DCC 2024). Although known SVP methods still give exponential running times, the impact on parameter selection led the HAWK team to withdraw the scheme. All three approaches rely substantially on rank-two structure. Higher-rank module-LIP is a possible direction for alternatives, calling for further study of its hardness. We first use the symmetric square to obtain a rank-two reduction, matching the bound 3n/4+1 above. Its auxiliary objects correspond geometrically and algebraically to those of the ChatGPT-derived algorithm, so this does not constitute a substantively new reduction; the differences lie in the interpretation and post-processing. This viewpoint nevertheless motivates our dimension reduction in rank four. In rank four, the conjugate Hodge star on the exterior square yields a publicly computable fixed lattice isometric to mathbb Z^{3n}, from whose orthonormal basis we reconstruct a module isomorphism. For {mathcal O_{L}}^4-LIP with the standard free module as reference, we reduce the 4n-dimensional problem to polynomially many SVP calls in dimensions at most 3n/2+1, improving the generic bound 2n+1. All computation outside the oracle runs in deterministic polynomial time.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2198) | 2026-09-24
