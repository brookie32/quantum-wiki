---
title: "QEDist: Practical Exact Distance Certification for Stabilizer Codes"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.21709"
summary: "arXiv:2611.21709v1 Announce Type: new Abstract: We present QEDist, a method and software package that certifies the distance of qubit stabilizer codes. Building on tree-search methods, QEDist construc"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.21709v1 Announce Type: new Abstract: We present QEDist, a method and software package that certifies the distance of qubit stabilizer codes. Building on tree-search methods, QEDist constructs candidate logical operators one qubit at a time, using sparse parity checks, stabilizer equivalence, and verified symmetries to reduce the work. For a cutoff W, a completed search either finds a nontrivial logical operator of weight at most W or proves that none exists. Because satisfying one check can violate another, we use both satisfied and unsatisfied checks to lower-bound the weight needed to complete a logical operator, and prune branches whose bound exceeds the remaining budget, which substantially reduces net search time. We benchmark QEDist mainly on Calderbank-Shor-Steane (CSS) codes; the same formulation extends to non-CSS codes and to the fault distance of syndrome-extraction circuits. For lifted-product (LP) codes, we further exploit the product structure to replace part of the full-code search with a smaller search on a classical constituent. We establish exact distances for codes with up to several thousand qubits, including Abelian and non-Abelian LP codes whose distances were previously reported only as upper bounds. In several seconds of search on one laptop core, QEDist certifies exact distances up to 20 for many of these codes and fault distance 10 for the syndrome-extraction circuit of the [[144,12,12]] code. With orders-of-magnitude speedups over the tested exact solvers, QEDist makes exact distance certification a practical tool for selecting and optimizing finite-length quantum codes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.21709) | 2026-11-18
