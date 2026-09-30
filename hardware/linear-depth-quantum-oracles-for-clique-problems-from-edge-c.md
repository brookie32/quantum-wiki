---
title: "Linear-depth quantum oracles for clique problems from edge colorings and graph states, with linear non-Clifford cost and a provably bounded-error k-clique search"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2308.16827"
summary: "arXiv:2308.16827v3 Announce Type: replace Abstract: Quantum algorithms for clique problems are usually analyzed in the query model, where the graph is accessed through an oracle of unit cost. When the"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2308.16827v3 Announce Type: replace Abstract: Quantum algorithms for clique problems are usually analyzed in the query model, where the graph is accessed through an oracle of unit cost. When the oracle must itself be compiled into gates, published k-clique circuits have depth quadratic in the number n of vertices, and every oracle that counts edges spends at least one non-Clifford gate per edge. We first show that scheduling the commuting edge gates by a proper edge coloring yields adjacency-type oracles, including an exact k-clique oracle, whose depth and width are linear in n, within a logarithmic factor of a depth--width lower bound. Our central result is a k-clique oracle in which the graph enters only through the Clifford gate that prepares a graph state, so that its non-Clifford cost is linear in n for every graph. We analyze this oracle exactly: on a candidate vertex set it acts as a reflection whose overlap is -1 for cliques and, as we prove, at most 5/8 in modulus otherwise, a tight bound that tends to 1/2 as the candidate set grows. A two-qubit phase-estimation filter turns the reflection into a one-sided bounded-error phase oracle, and amplitude amplification then finds a k-clique with O(sqrt{inom nk}) oracle calls, each of depth O(Delta+log n) for maximum degree Delta. The guarantee holds for two or more estimation registers; exact simulations on 312 induced subgraphs of two brain networks confirm it and show that the cheaper single-register variant performs nearly as well.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2308.16827) | 2026-09-30
