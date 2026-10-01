---
title: "Exponential quantum speedup for F_3^n-Subset-Sum? Or, rigorous classical algorithms for Binary-Error LWE"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40321"
summary: "arXiv:2609.40321v1 Announce Type: new Abstract: We study vector subset sum over F_3^n: given m random vectors from F_3^n, find a nonempty subset that sums to zero; the smaller m, the more difficult it"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40321v1 Announce Type: new Abstract: We study vector subset sum over F_3^n: given m random vectors from F_3^n, find a nonempty subset that sums to zero; the smaller m, the more difficult it is to find such a subset. Chen, Liu, and Zhandry (EUROCRYPT'22) introduced an efficient quantum algorithm that solves this problem when mapprox n^2/2, where a naive classical algorithm would require exponential time. Subsequently, Kothari, O'Donnell, and Wu (STOC'2026) gave an efficient classical algorithm that only requires m approx n^2/3 vectors, thus removing the hope for an exponential quantum advantage in this parameter regime. Using the framework of Chen, Liu, and Zhandry, we give quantum algorithms that require much fewer input vectors, renewing the possibility of an exponential quantum speedup: for any fixed epsilon>0, our quantum algorithm solves F_3-subset sum in polynomial time with m=epsilondot n^2 vectors. More generally, we establish a full sample--time tradeoff that interpolates between exponential and polynomial runtime. The main ingredient is a deterministic classical algorithm for the binary-error Learning-with-Errors problem, which is of independent cryptographic interest. For this, we rigorously establish a sample--time tradeoff that was predicted by earlier algebraic heuristics. For vector subset sums over larger fields, we also significantly improve classical algorithms in Kothari, O'Donnell, and Wu (STOC'2026).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40321) | 2026-10-01
