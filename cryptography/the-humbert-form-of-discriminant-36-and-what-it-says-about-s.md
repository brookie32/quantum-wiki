---
title: "The Humbert Form of Discriminant 36, and What It Says About Splitting Detection"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2327"
summary: "Explicit equations for the locus L_n of genus-two curves with a maximal degree-n elliptic subcover have been computed only for n le 5, and by elimination, whose cost is not predictable in advance. The"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Explicit equations for the locus L_n of genus-two curves with a maximal degree-n elliptic subcover have been computed only for n le 5, and by elimination, whose cost is not predictable in advance. The degree formula of [22] changes this. It gives eg_w F_n = k(H_{n^2}) - 10,nu(n) in closed form, and with it a reduced monomial support for the associated Humbert modular form G_{n^2}, so that the reconstruction becomes a determined linear problem whose every dimension is known before any computation begins. We carry this out for the first new case it opens, discriminant 36: we determine k(H_{36}) = 720, nu(6) = 12, eg_w F_6 = 600 and an admissible modular basis of size 41962, and we compute the four Siegel generators explicitly along Kumar's rational parametrisation of H_{36}, obtaining in particular a complete factorisation of hi_{10} whose factors recover the degenerate loci of the family from the modular side. We then draw the consequences for isogeny-based cryptography. The equation overline{F}_n decides optimal (n,n)-splitting at every point of the moduli space in characteristic p, with no hypothesis on the Newton polygon; this is asserted but not proved in the cryptographic literature, and the available proof excluded exactly the superspecial locus where the question is asked. The weight k(H_{n^2}) bounds, unconditionally and with explicit constants, the number of superspecial nodes that detection at level n adds to the target set of the best known attack in dimension two. And the same torsion count nu(n) that appears in the degree formula governs the cost of both known detection routes, which places a barrier on raising the level and singles out n = 6 as the one case where a new equation can matter in practice.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2327) | 2026-10-04
