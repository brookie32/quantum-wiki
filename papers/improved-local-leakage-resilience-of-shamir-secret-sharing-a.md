---
title: "Improved Local Leakage Resilience of Shamir Secret Sharing and Worst-Case Optimal Polynomial Intersection"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.12357"
summary: "arXiv:2610.12357v1 Announce Type: new Abstract: We study two problems: Local Leakage Resilience (LLR) for Shamir secret sharing, and worst-case Optimal Polynomial Intersection (OPI). Both problems con"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.12357v1 Announce Type: new Abstract: We study two problems: Local Leakage Resilience (LLR) for Shamir secret sharing, and worst-case Optimal Polynomial Intersection (OPI). Both problems concern polynomials Q(X) of degree less than k, over a prime-order finite field F_p. In LLR for Shamir secret sharing, one asks how much one can learn about Q(0) given a few bits leaked from each of Q(alpha_1), ldots, Q(alpha_n), for distinct non-zero evaluation points alpha_i in F_p. In OPI, one is given input list S_1, ldots, S_n subset F_p, and wants to find a polynomial Q(X) of degree less than k so that Q(alpha_i) in S_i for as many i as possible. Leveraging recent connection between these two problems due to (Sun, Wootters 2026), we improve the state-of-the-art for both problems. For LLR, we show that there is some constant elta > 0 so that, as long as R := k/n geq 1/2 - elta, Shamir secret-sharing is one-bit locally leakage resilient (meaning that one can learn only a negligible amount about Q(0)). This is the first result to break the so-called "one-half barrier" for LLR, and improves over the previous best known result, requiring R geq 0.668 (Kasser, 2025). For OPI, we give a quantum algorithm that finds a polynomial Q(X) that agrees with at least a mathsf{SCL}_rho(R)-arepsilon fraction of the lists in expectation, for every fixed arepsilon>0, where mathsf{SCL}_rho is the semicircle law of (Jordan et al., 2025). This improves previous algorithmic (and existential) results of (Jo, 2026) and (Horinaga, Yamakawa, 2026). We also give further improved existential results. We also adapt the hardness result of (Yamakawa, Zhandry, 2024) to apply to OPI (rather than a folded version); over large fields, this gives an unconditional separation between the quantum and classical hardness of OPI relative to a membership oracle.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.12357) | 2026-10-09
