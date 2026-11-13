---
title: "The Price of Geometry for Private Distance-Sensitive Filters: ell_infty versus ell_2"
date: "2026-11-11"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2871"
summary: "A distance-sensitive set representation stores a set S in a metric space and must accept points within distance r of S and reject points farther than cr, each with error probability at most alpha. Und"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

A distance-sensitive set representation stores a set S in a metric space and must accept points within distance r of S and reject points farther than cr, each with error probability at most alpha. Under differential privacy, even exact membership costs a privacy loss of ln(1/alpha); we ask how much more the geometry of the space forces. Earlier lower bounds cover only restricted mechanisms, such as partition-based ones or those whose outputs contain no scattered false positives (``dust''). We prove lower bounds for every mechanism. In ell_infty^d with c<3 the extra cost is Theta_c(d), which proves a recent conjecture in this range; when lfloor crrfloor-r+1 divides 2r, a randomly shifted grid is optimal up to ilde O(alpha) per dimension. In ell_2^d the extra cost is instead Theta_c(min(d,ln(1/alpha))): a new mechanism that outputs a single very large ball shows that dimensions beyond about ln(1/alpha) are free, so partition-based constructions are optimal in ell_infty but not in ell_2. The same arguments bound the space of every correct representation of k-sets, private or not: Omega(k(log(1/alpha)+d)) bits in ell_infty^d with c<3, and Omega_c(k(log(1/alpha)+min(d,log(1/alpha)))) bits in every ell_p^d.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2871) | 2026-11-11
