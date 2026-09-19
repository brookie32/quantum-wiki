---
title: "Symmetry-Graded Digit Extraction Framework for Faster BGV Bootstrapping"
date: "2026-09-17"
updated: "2026-09-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2076"
summary: "Bootstrapping is the bottleneck of BGV/BFV homomorphic encryption, and for large plaintext primes p its cost is dominated by digit extraction. Recently, this stage has been accelerated along two separ"
last_verified: "2026-09-19"
review_by: "2026-12-18"
stale: false
---

Bootstrapping is the bottleneck of BGV/BFV homomorphic encryption, and for large plaintext primes p its cost is dominated by digit extraction. Recently, this stage has been accelerated along two separate routes. The first lowers the degree of the digit-extraction polynomial: the bounded-support construction of Ma et al. (Eurocrypt'24) confines its support, and the order-four filter of Xiong et al. (to appear in Asiacrypt'26) removes three quarters of its monomials. The second lowers the depth of its evaluation: the Galois norm map of Okada et al. (Asiacrypt'23) and Zhao et al. (Crypto'26) evaluates a degree-d factor in logarithmic depth. However, how the two routes relate and whether they compose has remained open. We propose a symmetry-graded framework that views the two evaluation routes as commuting group actions on the digit-extraction polynomial. Under this unified perspective, the existing evaluators correspond to different specializations of cost(D;r,d). For lower degree, we identify a novel rank-two lattice structure underlying digit extraction. The crystallographic restriction limits the filter order to rin{1,2,3,4,6}. In particular, the methods of Ma et al. and Xiong et al. correspond to r=2 and r=4, respectively. Moreover, our framework derives a sparser order-six digit-extraction polynomial, enabling order-six symmetry for Mersenne primes. For lower evaluation cost, we construct a composed evaluator that first folds P_A using the scalar filter and then evaluates the folded polynomial via the slot ring's Galois norm map. Since the rotation and Frobenius actions commute, the two optimizations can be combined within the same framework. Consequently, for any (p,m) we select the optimal (r,d) and evaluate digit extraction in 2sqrt{D/(rd)}+O(log D) non-scalar multiplications. On 13 general cyclotomic rings at geq 80-bit verified security, our single-threaded HElib implementation improves upon the state-of-the-art evaluator of Ma et al., accelerating digit extraction by 2.4–4.9imes and thin bootstrapping by 1.3–2.8imes, while modifying only the digit-extraction stage. In particular, on Ma et al.'s set IV with the Mersenne prime p=8191 and set V with p=65537, digit extraction is accelerated by 3.6imes and 3.8imes, respectively, reducing the total bootstrapping time from 180.4 s to 85.5 s and from 217.6 s to 103.1 s. The implementation is publicly available, and the core analysis is machine-checked in Lean 4.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2076) | 2026-09-17
