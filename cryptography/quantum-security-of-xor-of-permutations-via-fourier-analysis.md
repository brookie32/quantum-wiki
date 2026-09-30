---
title: "Quantum Security of XOR of Permutations via Fourier Analysis"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2241"
summary: "The XOR of two or more independent random permutations (XoP) is the prototypical pseudorandom function built from permutations achieving the security beyond the birthday bound. The security of the XoP"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

The XOR of two or more independent random permutations (XoP) is the prototypical pseudorandom function built from permutations achieving the security beyond the birthday bound. The security of the XoP construction is now well established against classical adversaries, however, its security against quantum adversaries that query the construction in superposition has remained widely open. We prove that the XOR of rge 2 independent random permutations over {0,1}^n is indistinguishable from a random function by any q-query quantum algorithm with advantage [ Oleft(minleft{ frac{q^3}{2^{rn}},frac{q^{1.5}}{2^{(r-0.5)n}},frac{1}{2^{(r-1.5)n}} right} right) ] for all qle 2^n/57774, where the hidden factors depend only on r. In particular, the XoP construction remains secure throughout the entire query range, far beyond the 2^{n/3} quantum birthday bound due to the quantum collision finding attack. To our knowledge, this is the first construction from permutations that achieves the quantum version of the beyond birthday bound security. We present several heuristic attacks suggesting the tightness of our bounds. For qlesssim 2^{n/2}, the quantum collision finding-based attacks heuristically give the advantage Omega(q^3/2^{rn}) and Omega(q^{1.5}/2^{(r-0.5)n}), and for qapprox 2^n, the heuristic collision counting-based attack appears to have the advantage about 2^{-(r-1.5)n}. We use a Fourier-analytic variant of the polynomial method on the space of functions: the distinguishing advantage of any q-query quantum algorithm is controlled by the Fourier components of degree at most 2q, which is controlled by 2q input-output data of the construction. Most components are bounded as a ell_2 norm of the Fourier weights of the XOR of permutations, which gives the bound 2^{-(r-3/2)n}. For the bound q^3/2^{rn}, few low-degree components are too large. We reinterpret these low-degree components as (sums of) distinguishing advantages of the other problems. For example, the degree-2 and degree-4 terms are interpreted as the advantages against random functions with and without planted collisions, which in turn are bounded using Zhandry's small-range distributions. Finally, the q^{1.5}/2^{(r-0.5)n} bound can be proven using another bound for the planted collisions. This new bound is proven using the compressed oracle by interpreting the advantage as the other bound about random functions. It also gives a new bound for the small-range indistinguishability for (ironically) large ranges, which is of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2241) | 2026-09-28
