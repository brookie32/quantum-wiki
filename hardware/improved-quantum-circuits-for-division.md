---
title: "Improved quantum circuits for division"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.18110"
summary: "arXiv:2603.18110v2 Announce Type: replace Abstract: Arithmetic operations are an important component of many quantum algorithms. Optimizing quantum circuits for these operations therefore leads to mor"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2603.18110v2 Announce Type: replace Abstract: Arithmetic operations are an important component of many quantum algorithms. Optimizing quantum circuits for these operations therefore leads to more efficient implementations of the corresponding algorithms. In this paper, we develop new fault-tolerant quantum circuits for various integer division algorithms (both reversible and non-reversible). These circuits, when implemented in the Clifford+T gate set, achieve improvements in the asymptotic T-count and CNOT-count from O(n^2) to O(nm), and in the asymptotic T-depth from O(n^2) to O(n log m), where n and m are the bit lengths of the dividend and divisor, respectively. The qubit counts are significantly lower than those in previous works. We achieve this through careful modifications of the division algorithms and by expressing them in terms of a primitive we call COMP-N-SUB that compares two integers and conditionally subtracts them. We show that this primitive can be implemented at a cost, in terms of both Clifford and non-Clifford gates, comparable to that of one addition. By contrast, performing comparison and conditional subtraction separately would cost roughly as much as a controlled addition plus a regular addition.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.18110) | 2026-09-07
