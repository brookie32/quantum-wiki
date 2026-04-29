---
title: "Quantum CORDIC -- Arcsine on a Budget"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2411.14434"
summary: "arXiv:2411.14434v2 Announce Type: replace Abstract: This work introduces a quantum algorithm for computing the function arcsine, with arbitrary accuracy. We leverage a technique from embedded computin"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2411.14434v2 Announce Type: replace Abstract: This work introduces a quantum algorithm for computing the function arcsine, with arbitrary accuracy. We leverage a technique from embedded computing and Field-Programmable Gate Arrays, called COordinate Rotation DIgital Computer (CORDIC). CORDIC is a family of iterative algorithms that, in a classical context, can approximate various trigonometric, hyperbolic, and elementary functions using only bit shifts and additions. Adapting CORDIC to the quantum context is non-trivial, as the algorithm traditionally uses several non-reversible operations. We detail a method for CORDIC that avoids such non-reversible operations. We propose multiple approaches to calculate the arcsine function reversibly with CORDIC. For n bits of precision, our method has space complexity of order n qubits, a layer count in the order of n times log n, and a CNOT count in the order of n squared. This primitive function is a required step for the Harrow-Hassidim-Lloyd (HHL) algorithm, is necessary for quantum digital-to-analog conversion, can simplify a quantum speed-up for Monte-Carlo methods, and has direct applications in the quantum estimation of Shapley values.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2411.14434) | 2026-04-29
