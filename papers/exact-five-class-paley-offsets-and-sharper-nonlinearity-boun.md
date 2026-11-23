---
title: "Exact Five-Class Paley Offsets and Sharper Nonlinearity Bounds Exceeding the Patterson-Wiedemann Direct-Sum Threshold"
date: "2026-11-21"
updated: "2026-11-23"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2975"
summary: "In a recent landmark preprint (IACR ePrint 2026/2680), Tang and Maitra established the first explicit fixed-dimension improvement over the Patterson-Wiedemann direct-sum nonlinearity bound N_PW(n) = 2"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

In a recent landmark preprint (IACR ePrint 2026/2680), Tang and Maitra established the first explicit fixed-dimension improvement over the Patterson-Wiedemann direct-sum nonlinearity bound N_PW(n) = 2^(n-1) - 27*2^((n-11)/2) = N_BC(n) + 81920*2^((n-39)/2), proving the existence of (balanced) Boolean functions in n = 375 variables--and hence every odd n >= 375--with nonlinearity exceeding N_BC(n) + 81921*2^((n-39)/2). Their framework combines index-two Gauss-period offsets on multiplicative cosets of GF(2^n)* with an unequal-threshold linear-feasibility criterion of Reis and Song and a sampling-without-replacement balancing lemma. Building directly on Tang and Maitra's framework, we make four contributions. First, we prove an elementary closed-form theorem showing that, for every prime q = 3 (mod 4) with n = ord_q(2) = (q-1)/2 odd and Gauss sum G_1 = 2^((n-h)/2-1)*(a + b*i*sqrt(q)) (b > 0, sigma = sgn(a)), the unmodified translated quadratic-residue template S = c + sigma*R (with Legendre symbol e_c = sigma) produces an exact universal five-class offset magnitude distribution, eliminating case-by-case enumeration. Second, evaluating the Reis-Song potential directly on the unmodified template S = 3 - R at n = 375 (q = 751) sharpens the certified threshold from C = 1.193239 to C = 1.192508, yielding NL(f) > 2^(n-1) - 442096*2^((n-39)/2) = N_BC(n) + 82192*2^((n-39)/2) for every odd n >= 375 (both unbalanced and balanced)--enlarging the strict margin above N_PW(n) from 2^((n-39)/2) to 272*2^((n-39)/2) while simplifying the construction to zero label exchanges. An exhaustive check over all 140,625 weight-preserving single exchanges confirms that 3 - R is locally optimal for the potential at n = 375; by contrast, at n = 431 (q = 863), where the isolated class carries 51.8% of the potential, two potential-guided exchanges strictly improve the threshold from C = 1.184952 to C = 1.183620. Third, a complete Hensel-Cornacchia screening of all 208 prime-order index-two candidates in 375 2^(n-1) - 26*2^((n-11)/2) at n >= 743 and NL(f) > 2^(n-1) - 24*2^((n-11)/2) at n >= 4935, closing 69.38% of the normalized gap between the Patterson-Wiedemann constant and Schmidt's asymptotic limit. Fourth, we establish a structural lower bound q >= 713 for single-coset Reis-Song feasibility and summarize a Stickelberger-LLL screening of higher-index primes below n = 375. All numerical inequalities are certified by exact integer and rational arithmetic.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2975) | 2026-11-21
