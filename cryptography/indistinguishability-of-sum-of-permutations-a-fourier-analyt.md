---
title: "Indistinguishability of Sum of Permutations: A Fourier Analytic Route to Classical and Quantum Security"
date: "2026-09-27"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2230"
summary: "We study classical and quantum indistinguishability of sums of independent random permutations and related transformations from permutations to functions. Let G be a finite abelian group of order N, a"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

We study classical and quantum indistinguishability of sums of independent random permutations and related transformations from permutations to functions. Let G be a finite abelian group of order N, and let pi^k_+(x)=pi_1(x)+dots+pi_k(x) for kgeq2 independent uniform random permutations of G. We give a unified Fourier analytic treatment in which the construction is represented by its probability density and a distinguisher by its acceptance function, with the classical and quantum query models imposing different restrictions on the Fourier support of the latter. Classically, we obtain the bound O_k(q/N^{k-1/2}) for every q<N, and refine it below the birthday threshold to O_k(q^2/N^k). In the quantum model, a simulation argument gives O_k(N^{-(k-3/2)}) for qleq(N-1)/2, while Fourier interpolation gives concrete finite bounds up to qleq4N/15 and the query-dependent bounds [ O!left(minleft{N^{-1/2},frac{q^3}{N^2}+frac1Nright}right), qquad O_k!left(minleft{frac{q^3}{N^k},N^{-(k-3/2)}right}right), ] for k=2 and k geq 3, respectively, throughout 1leq qleq(N-1)/2. For q = 1, the first bound sharpens to O(N^{-2}). Over G=mathbb F_2^n, a one-query Fourier attack matches the order of our one-query bound, while an N/2-query parity attack with advantage 1/2 shows that our bounds reach the constant-advantage query threshold. We further study two variants of sum of permutations over binary vector spaces. First, we allow arbitrary surjective linear postprocessing, which includes truncation, and obtain classical and quantum bounds that retain the output-size dependence. Second, we analyse Dinur's variable-output single-permutation construction, mathsf{LXoP}, for every fixed output width, and derive its classical and quantum security bounds; for one- and two-block outputs, we give concrete quantum security bounds.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2230) | 2026-09-27
