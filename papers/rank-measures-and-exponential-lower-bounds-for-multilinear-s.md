---
title: "Rank Measures and Exponential Lower Bounds for Multilinear Secret Sharing"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1769"
summary: "A multilinear secret-sharing scheme shares a vector secret and can therefore amortize share size over the secret dimension. This amortization can invalidate lower bounds proved for one-dimensional lin"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

A multilinear secret-sharing scheme shares a vector secret and can therefore amortize share size over the secret dimension. This amortization can invalidate lower bounds proved for one-dimensional linear schemes, and the best previous explicit lower bound for multilinear schemes was quasipolynomial, n^{Omega(log n)}. We prove that the Razborov--Gal rank measure survives amortization: the normalized size of a multi-target monotone span program is at least the rank measure of the function it computes. Combined with the rank witnesses of Pitassi and Robere, this gives an explicit family of access structures for which every perfect multilinear scheme over every finite field has average and maximum information ratio 2^{Omega(n)}. The worst-case multilinear information ratio is therefore 2^{Theta(n)}, answering a question of Beimel. We further extend the bound to schemes whose sharing algorithm is arbitrary and whose reconstruction is affine-linear, under pairwise statistical privacy below one; combined with the degree-reduction theorem of Beimel, Othman, and Peter, this yields exponential normalized lower bounds for every fixed reconstruction degree whenever the secret dimension is 2^{o(n)}.



## Related
- [[classification-of-small-size-quantum-secret-sharing-schemes-|Classification of Small-size Quantum Secret Sharing Schemes using Uniform States]]
- [[quantum-secret-sharing-rates|Quantum Secret Sharing Rates]]
- [[an-efficient-and-perfect-secret-sharing-scheme-on-a-class-of|An Efficient and Perfect Secret Sharing Scheme on a Class of Non-Maximal Quantum Access Structure]]

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1769) | 2026-08-21
