---
title: "A Spectral Theory of Local-to-Global Leakage"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2571"
summary: "This paper studies how local leakages characterize the global leakage in additive secret sharing over a finite abelian group, which is a special case of linear secret sharing and side-channel masking."
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

This paper studies how local leakages characterize the global leakage in additive secret sharing over a finite abelian group, which is a special case of linear secret sharing and side-channel masking. Our main finding is structural: local-to-global leakage is governed by two disjoint components---the magnitude of local leakage and its spectral alignment across shares, while existing literature attempted to characterize the global leakage only by local mutual information (MI). We first give an exact decomposition of leakage in additive secret sharing. The decomposition reveals a structural parameter invisible to MI, while previous literature conjectured that the local MI alone suffices to characterize global leakage. We then show that this missing parameter is indispensable: two leakage channels with identical local MI can induce exponentially different global leakage. Our exact decomposition identifies the missing structural quantity and completely characterizes this phenomenon. We then show the separation theorem with its realizability---local MI, despite governing the classical leakage bounds, does not even determine the exponential rate at which leakage vanishes under homomorphic composition. More strongly, we establish a universal separation theorem: even when all permutation-invariant scalar measures of local leakage agree, the global leakage can exhibit exponentially different decay rates. We further provide the characterization of the spectral alignment factor and derive its lower bound through character-order multiplicity and Möbius inversion. We then extend the framework to automorphism-weighted sharing. We establish that automorphism-weighted sharing can achieve perfect leakage cancellation with finitely many shares, even for non-trivial full-support local leakage channels. In sharp contrast, such perfect cancellation is impossible for ordinary additive sharing with non-trivial i.i.d local leakage channels and finitely many shares. Consequently, local leakage magnitudes correctly measure the average amount of local leakage, but discard the compatibility structure needed for composition. Magnitude-only bounds must optimize over structural alignments that the actual leakage channel does not realize.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2571) | 2026-10-20
