---
title: "The Covering Radius of ext{RM}(1,9) is Precisely 242"
date: "2026-10-18"
updated: "2026-10-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2529"
summary: "Let ext{RM}(r,n) be the rth order Reed-Muller code of length 2^n, and let rho(r,n) denote its covering radius, so that rho(1,n) is the largest possible nonlinearity of a Boolean function in n variable"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

Let ext{RM}(r,n) be the rth order Reed-Muller code of length 2^n, and let rho(r,n) denote its covering radius, so that rho(1,n) is the largest possible nonlinearity of a Boolean function in n variables. For odd n, the value of rho(1,n) was previously known only for nle 7. It is known that 242lerho(1,9)le 244, but the exact determination of rho(1,9) has been a long-standing open question. We give a computer-assisted proof that rho(1,9)=242. We first show that a function of nonlinearity 243 would yield one of nonlinearity 244, so it suffices to exclude 244. Divisibility properties of the Walsh spectrum then attach to any function of nonlinearity 244 a cubic p whose spectrum attains the sharp bound sumlimits_a|W_p(a)|le 10240, and the cases of equality take one of two forms. One form is eliminated directly. The other is eliminated by an exhaustive computation that leverages the classification of the 349 orbits in ext{RM}(3,9)/ext{RM}(2,9) under ext{GL}(9,2), using Langevin's catalog of representatives together with an audit of its completeness, and the enumeration is carried out twice with independent implementations. The notebook to verify the computer search portion, exttt{Verify_RM(1,9).ipynb}, contains all data and recomputes each check, and may be found in the repository rl{https://github.com/FreemanSlaughter/Covering-Radius}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2529) | 2026-10-18
