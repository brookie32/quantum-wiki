---
title: "Quadratic Sums-of-Powers for Fixed-Parameter Tractable Quantum-Circuit Simulation"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.29944"
summary: "arXiv:2605.29944v2 Announce Type: replace Abstract: Strongly simulating a quantum circuit, that is, computing an output amplitude, can be done by summing the circuit's Feynman paths: a weighted count "
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2605.29944v2 Announce Type: replace Abstract: Strongly simulating a quantum circuit, that is, computing an output amplitude, can be done by summing the circuit's Feynman paths: a weighted count over assignments to Boolean path variables. The circuit's gates induce correlations among these variables, forming a graph whose structure controls several exact simulation routes. This sum-of-powers (SOP) viewpoint underlies recent simulators built on binary decision diagrams and weighted model counting. For a quadratic SOP with n variables, even modulus r, and a rank-decomposition of its variable graph of width k, our dynamic program (DP) computes an amplitude using only O(4^kpoly(n)) arithmetic operations. For Clifford+T circuits, the amplitude is given by an SOP with modulus 8. Rank-width never exceeds linear rank-width, which governs some decision-diagram approaches, and is at most one greater than the Markov--Shi contraction complexity of the circuit tensor network. Moreover, there are non-Clifford families of bounded rank-width where both competing parameters diverge. We also present a stabilizer-rank optimization, exploiting that the DP tables are stabilizer-type Gauss sums. Each subtree runs at the width price of its cut-ranks or at a magic price that discharges the non-Clifford phases below it. The resulting best total cost never exceeds O(4^kpoly(n)), yet is polynomial on mixed families where the pure rank-width and pure T-count guarantees are both exponential. Clifford amplitudes take polynomial time on any graph, the exact-amplitude consequence of Gottesman--Knill. A prototype evaluation on standard circuit benchmarks finds treewidth bucket elimination the strongest baseline, with the new rank-width DP complementary: it wins on structured families where treewidth blows up.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.29944) | 2026-08-21
