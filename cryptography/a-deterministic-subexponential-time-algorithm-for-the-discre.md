---
title: "A Deterministic Subexponential-time Algorithm for the Discrete Logarithm Problem"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3020"
summary: "Classical deterministic algorithms for the discrete logarithm problem (DLP) in prime fields F_p^* and on elliptic curves E(F_p) require p^{1/2+o(1)} bit operations in the worst case when no unproven n"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Classical deterministic algorithms for the discrete logarithm problem (DLP) in prime fields F_p^* and on elliptic curves E(F_p) require p^{1/2+o(1)} bit operations in the worst case when no unproven number-theoretic hypotheses are assumed. Following the October 2026 refutations of the Exponential Time Hypothesis (ETH), Akshima et al. (2026) and Kaarelson (2026) obtained Las Vegas subexponential algorithms for the elliptic-curve discrete logarithm problem over prime fields, while leaving deterministic p^{o(1)} discrete logarithm algorithms open even in F_p^*. In this paper, we show that assuming the Cauchy--Hermite Boolean tensor contraction construction of OpenAI (October 2026), there is a uniform deterministic multitape Turing machine that solves both the discrete logarithm problem on prime-order elliptic curves over F_p (p > 3) and the discrete logarithm problem in F_p^* in worst-case time [ 2^{O(b/sqrt{loglog b})} = p^{o(1)} ] and space 2^{O(b/(log b)^{1/4})}, where b = lceil log_2 p rceil. The algorithm uses zero random bits and relies on neither the Generalized Riemann Hypothesis nor smoothness heuristics. Our proof combines two technical ingredients: (i) a deterministic conditional-expectation construction of small affine-interval factor bases whose 2m-fold sumsets cover the entire group, and (ii) a terminal-preserving partial contraction procedure that bypasses the degree barrier of candidate-label table lookups by compressing the low-degree arithmetic core onto Theta(b) boundary wires prior to exact digitwise contraction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3020) | 2026-11-24
