---
title: "TFNP in the Random Oracle Model"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2748"
summary: "We determine which major TFNP classes are hard in the random oracle model (ROM). Prior work establishes average-case hardness of highly structured subclasses of TFNP from strong cryptographic assumpti"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

We determine which major TFNP classes are hard in the random oracle model (ROM). Prior work establishes average-case hardness of highly structured subclasses of TFNP from strong cryptographic assumptions such as LWE and indistinguishability obfuscation. It is not known whether weaker assumptions such as one-way functions imply hardness of any of the standard TFNP subclasses, even in the worst case. The ROM, where all parties have query access to a random function, lies, morally, between these two regimes: a random function is one-way, but public-key cryptography cannot be built from it in a black-box way. We refer to this setting as Romantica. Our first result settles a long-standing open problem: PPAD, the class of total search problems reducible to finding a Nash equilibrium, is hard on average in Romantica. Combined with the known hardness of PLS (local search), this gives average-case hardness of EoPL = PPAD ap PLS. In contrast, we show that UEoPL can be solved in Romantica with polynomially many oracle queries by a computationally unbounded solver, a sharp distinction between EoPL and UEoPL. This resolves the black-box hardness landscape of all major TFNP classes in Romantica. Finally, we initiate the study of separations between TFNP subclasses in Romantica: PWPP and PPA do not reduce to PLS under public-coin reductions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2748) | 2026-11-03
