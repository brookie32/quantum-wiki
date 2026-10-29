---
title: "An Algebraic Polynomial Evaluation Datastructure for Fields of Large Characteristic"
date: "2026-10-28"
updated: "2026-10-29"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2668"
summary: "In this work, we study (multivariate) polynomial evaluation datastructures, i.e. algorithms that can evaluate a multivariate polynomial at any input point, using random access to some precomputed enco"
last_verified: "2026-10-29"
review_by: "2027-01-27"
stale: false
---

In this work, we study (multivariate) polynomial evaluation datastructures, i.e. algorithms that can evaluate a multivariate polynomial at any input point, using random access to some precomputed encoding of the polynomial. Multiple constructions have been proposed in the literature, with the work by Bhargava, Ghosh, Guo, Kumar and Umans (2024) achieving optimal datastructure size and query complexity, up to polynomial factors. For n in d^{o(1)} this is equivalent to having datastructure size d^{n + o(n)} (d n log q)^{O(1)} and query complexity (d n log q)^{O(1)} for an n-variate polynomial of total degree d over F_q. However, the algorithm of Bhargava et al. is not algebraic, since it requires lifting prime field elements to Z. An algebraic algorithm would be desirable, as an algebraic model of computation is natural for studying polynomial evaluation and is the standard model in algebraic complexity theory. One approach to finding algebraic polynomial evaluation datastructures is to use univariate polynomial interpolation to reconstruct the polynomial along algebraic curves. This approach was first made explicit by Bhargava, Ghosh, Kumar and Mohapatra (2023), who used it to build an essentially optimal algebraic polynomial evaluation datastructure for fields of small characteristic p = char(F_q) in d^{o(1)}. Over these fields, their construction refutes a previous conjecture by Miltersen. For fields of larger characteristic, it remains an open problem to find an algebraic algorithm with optimal datastructure size and query complexity. In this work, we propose a new way to construct algebraic curves over prime fields that allow polynomial interpolation: by deriving curves from the base-eta representation of (lifts of) prime field elements, we are able to recursively reduce the evaluation problem to points in boxes of decreasing size. This leads to a datastructure whose performance scales much more favourably with p. Concretely, we improve the dependency of the query complexity on p from p^{O(1)} to d^{2log_2 lnln p} ln p, and completely remove the dependency on p from the datastructure size. Its query complexity is still slightly super-polynomial in d log p. Nevertheless, a variant of our results is enough to disprove Miltersen's conjecture for all finite fields, including prime fields. We further show that for a certain class of datastructures, which captures natural generalizations of our approach, the query complexity is lower-bounded by d^{(1 - o(1))log_3lnln p}. Consequently, within this class, our construction is optimal up to a constant in the exponent.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2668) | 2026-10-28
