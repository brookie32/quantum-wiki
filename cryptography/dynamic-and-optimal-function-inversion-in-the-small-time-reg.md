---
title: "Dynamic and Optimal Function Inversion in the Small-Time Regime"
date: "2026-08-22"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1777"
summary: "The classic function-inversion problem considers the task of constructing a data structure which, given access to a constant-time oracle for a function f : [N] rightarrow [N], supports efficient inver"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

The classic function-inversion problem considers the task of constructing a data structure which, given access to a constant-time oracle for a function f : [N] rightarrow [N], supports efficient inverse-queries on f. This problem has been studied extensively in the small-space/large-time regime, where one wishes to use space S, say, N^{1 - Omega(1)} bits, and where the query time is intended to be a small polynomial of N. Much less attention has been given to the small-time/large-space regime, where S = (N log N) / t for some relatively small t, and where the goal is to achieve a good space bound as a function of t. In this paper, we give an optimal solution in the small-time regime, achieving space S = O(N log N / t) and time O(t) for any t le O(log N / log log N). This matches a lower bound by Yao (and is the first parameter regime where the lower bound has been matched for general functions). Additionally, we extend our solution to support point-updates to f, also in O(t) time. Our techniques for supporting point updates also extend to the classic function-inversion solution of Fiat and Naor. All of our results are motivated by the data-structural perspective on function inversion, in which the goal is to supplement an already-existing data structure D_1 (which, as part of its functionality, encodes some function f) with a small secondary data structure D_2 that supports inverse queries. Our results allow D_2 to be implemented in (N log N)/t bits with O(t) query (and update) times -- if D_1 is itself Theta(N log N) bits, this results in the overall space usage increasing by only a (1 + O(1/t)) factor. As a sample application of our results, we show how to construct dynamic unordered graphs that use space (1 + epsilon)-close to information-theoretically optimal while offering adjacency queries, neighborhood queries, and edge insertions/deletions in amortized time O(epsilon^{-1}).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1777) | 2026-08-22
