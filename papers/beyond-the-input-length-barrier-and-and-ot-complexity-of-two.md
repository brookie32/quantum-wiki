---
title: "Beyond the Input-Length Barrier: AND and OT Complexity of Two-Party Computation"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3038"
summary: "A natural quantitative question in secure two-party computation is how many calls to a complete primitive (AND, Oblivious Transfer) are necessary to securely compute a given function. Beimel and Malki"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

A natural quantitative question in secure two-party computation is how many calls to a complete primitive (AND, Oblivious Transfer) are necessary to securely compute a given function. Beimel and Malkin (2004) initiated a systematic study of this question for one-sided AND in perfect information-theoretically secure model against semi-honest adversaries. They gave lower bounds of n, the per party input length, for functions satisfying explicit combinatorial characterizations. The secure zero-communication reduction framework of Narayanan, Prabhakaran, and Prabhakaran (2020) recovered this input-length frontier by a different route. Nevertheless, unconditional lower bounds for both AND, OT beyond the per party input length for deterministic Boolean functions have remained elusive, even existentially. Our first result gives explicit AND lower bounds beyond the input length. For Inner Product, equality and Hamming proximity of n bit strings, we prove lower bounds of (1.29n+Omega(log n)) AND calls. We then consider OT and show almost every Boolean function on two (n)-bit inputs requires (1.26n-O(log n)) OT calls. For Inner Product we also improve the classical (2n) AND upper bound, giving a perfectly secure randomized protocol using (1.71n+o(n)) AND calls. The combinatorial constructions underlying this protocol may be of independent interest. Finally, we revisit the role of private randomness. We prove a general derandomization theorem showing that, near the natural counting limit, randomized protocols can be derandomized in a fully parallel way without increasing the number of AND calls. This settles the 2 and 3 AND call derandomization cases left open by Beimel and Malkin and, together with their 4 call separation, identifies 4 as the first level at which randomness helps.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3038) | 2026-11-25
