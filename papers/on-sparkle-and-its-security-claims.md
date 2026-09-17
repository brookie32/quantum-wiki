---
title: "On Sparkle+ and its Security Claims"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2044"
summary: "We revisit the security bounds of Sparkle+, the threshold Schnorr signature scheme which first appeared in 2023. This scheme has been updated and corrected in several versions and papers (also of othe"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

We revisit the security bounds of Sparkle+, the threshold Schnorr signature scheme which first appeared in 2023. This scheme has been updated and corrected in several versions and papers (also of other authors). However, no version or paper has checked in detail the final bounds of Theorem 1 and 2 of the June 2025 version, which have therefore, to the best of our knowledge, been taken for granted in the related literature. There, the derivation of the final bounds of its Theorems 1 and 2, on full static security under DL and on adaptive security up to t/2 corruptions under AOMDL, from the intermediate inequalities established by their proofs is left to the reader. Carrying it out, we obtain bounds that differ from the stated ones in three distinct algebraic respects: the terms produced by the two game hops precede the rewinding and therefore appear outside the square root rather than inside it; the whole game-hop aggregate, and not only its collision part, re-enters through the extraction inequality with coefficient 2q rather than 1; and the exact inversion of the general forking lemma contributes q/2p outside the root together with q^2/4p^2 inside it, with q the number of queries and p the group order, its standard relaxation combining the two into an additive q/p, and the statements carry none of this. We prove the bounds that do follow, for both theorems, and determine exactly when each of ours and the original is the tighter. Conditional on the correctness of the game transitions from which those inequalities come, the asymptotic security conclusions are unaffected.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2044) | 2026-09-15
