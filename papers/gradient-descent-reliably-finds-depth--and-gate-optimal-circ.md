---
title: "Gradient descent reliably finds depth- and gate-optimal circuits for generic unitaries"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.03123"
summary: "arXiv:2601.03123v2 Announce Type: replace Abstract: When the gate set has continuous parameters, synthesizing a unitary operator as a quantum circuit is, in principle, always possible using exact meth"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2601.03123v2 Announce Type: replace Abstract: When the gate set has continuous parameters, synthesizing a unitary operator as a quantum circuit is, in principle, always possible using exact methods. However, efficiently finding depth- and gate-minimal circuits remains a major challenge. The landscape is very different for compiled unitaries, which arise from programming and typically have short circuits, as compared with generic unitaries, which use all parameters and typically require circuits of maximal size. Previous approaches based on random combinatorial search indicate a low success rate even when the circuit ansatz is nominally adequately parameterized, motivating the use of heavily overparameterized circuits. In this work, we present a gradient-based optimization framework that enables the synthesis of depth- and gate-optimal circuits for generic unitaries without overparameterization, even under restricted hardware connectivity. We prescribe parameter-optimal circuit skeletons and eliminate the need for random combinatorial search. We further show that the poor performance of earlier random-search approaches can be attributed to the inadvertent selection of parameter-deficient circuit topologies. By systematically avoiding such skeletons, our approach achieves reliable convergence while maintaining parameter efficiency.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.03123) | 2026-08-18
