---
title: "Connecting Cryptanalytic Distinguishers through Divisibility"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2471"
summary: "Integral distinguishers can reveal more than a zero-sum property: the number of ones in an output component may be divisible by a high power of 2, rather than merely being even. To exploit this divisi"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Integral distinguishers can reveal more than a zero-sum property: the number of ones in an output component may be divisible by a high power of 2, rather than merely being even. To exploit this divisibility, we relate linear, integral, differential-linear, and restricted differential sums through two-way conversions with explicit divisibility guarantees and data complexity, recovering established links as special cases. We derive exact random-permutation probabilities and rigorous bounds to quantify the distinguishing strength while accounting for dependencies between output conditions. To discover these properties, we develop automated MILP/SAT models that use complete-round Walsh coefficients or combine Walsh and ultrametric representations to obtain stronger bounds. These weighted models prove finite divisibility even when compatible trails exist, beyond what trail-existence tests alone can establish. For differential-linear sums, we show that combining differential and linear propagation with local DLCT zeros can give false zero-correlation claims. We address this limitation with exact mix-basis models that establish zero correlation and finite divisibility. To complement these symbolic methods, we provide a black-box algorithm using exact histograms and the fast Walsh-Hadamard transform to search all output masks for selected input conditions and identify zeros and finite divisibility properties. Our MILP/SAT models significantly improve the divisibility bounds reported by Beyne and Verbauwhede in 674 cases across the SIMON family, as well as for PRESENT, without trail enumeration and at unchanged data complexity, e.g., from 2^5 to 2^{11} on 9-round SIMON32 and from 2^6 to 2^{22} on 10-round SIMON48. To our knowledge, we are the first to prove higher divisibility for 8-round SPECK and for BEANIE, with new bounds for GIFT-64 and Ascon and exact counts for SKINNY-64. Our black-box searches reveal new properties on RC5, ChiLow-32, KeeLoq, and KATAN32, including output-bit combinations missed by single-bit searches, and lead us to introduce probabilistic divisibility.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2471) | 2026-10-14
