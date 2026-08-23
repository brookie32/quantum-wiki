---
title: "New Lower Bounds for Rows of d-Disjunct Matrices via Recursive Potentials"
date: "2026-08-22"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1771"
summary: "In nonadaptive combinatorial group testing, given n items with at most d positives, the goal is to identify them using as few pooled tests as possible. A times n binary matrix represents the design, w"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

In nonadaptive combinatorial group testing, given n items with at most d positives, the goal is to identify them using as few pooled tests as possible. A times n binary matrix represents the design, where rows are tests and columns are items. The matrix is d-disjunct if no column is contained in the Boolean union of any d others. Let T(d) be the minimum t for which such a matrix exists with n>t. Shangguan and Ge proved T(d)ge frac{15+sqrt{33}}{24}d^2 by counting private pairs (IEEE Trans. Inf. Theory, 62(12):7518-7521, 2016). In this paper, we strengthen their argument by introducing a column-deletion recurrence in which the light-heavy threshold varies with the recursive state z=(n-t)/d^2, rather than remaining fixed. This yields the improved bound T(d)ge 0.9283d^2-O(d). The analytic core reduces to a first-order ODE, and a self-contained interval-arithmetic certificate verifies that the solution reaches the required contact point.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1771) | 2026-08-22
