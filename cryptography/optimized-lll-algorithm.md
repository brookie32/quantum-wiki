---
title: "Optimized LLL Algorithm"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2361"
summary: "The LLL algorithm involves reductions and swaps, corresponding to projection and ordering conditions. But the transformation ec{b}'_ileftarrow ec{b}_i- lfloormu_{i,k} rceilec{b}_k is not a general siz"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

The LLL algorithm involves reductions and swaps, corresponding to projection and ordering conditions. But the transformation ec{b}'_ileftarrow ec{b}_i- lfloormu_{i,k} rceilec{b}_k is not a general size-reduction, where mu_{i,k}=frac{langle ec{b}_i, ec{b}_k^* rangle}{langle ec{b}_k^*, ec{b}_k^* rangle} , ec{b}_k^* is the orthogonalized vector of ec{b}_k, which cannot ensure |ec{b}'_i|leq |ec{b}_i|. The condition (elta-mu_{i+1,i}^2)|ec{b}_i^*|^2leq |ec{b}_{i+1}^*|^2 for eltain(1/4, 1), cannot ensure |ec{b}_i|leq |ec{b}_{i+1}|. The two drawbacks possibly result in: (1) the first vector could be longer than others, (2) some vectors could be further reduced. In this paper, we present an optimized LLL algorithm which is independent of rthogonalization and reduces the complexity from O(n^4) to O(n^3). By a probabilistic argument, we show the new algorithm runs in polynomial time.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2361) | 2026-10-05
