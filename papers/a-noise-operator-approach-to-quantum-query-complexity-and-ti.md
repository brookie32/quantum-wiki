---
title: "A Noise Operator Approach to Quantum Query Complexity and Time-Space Tradeoff Lower Bounds"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40334"
summary: "arXiv:2609.40334v1 Announce Type: cross Abstract: Time and space (memory) are two of the most important measures of cost in computation, even more so for quantum computation. In quantum computation ou"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40334v1 Announce Type: cross Abstract: Time and space (memory) are two of the most important measures of cost in computation, even more so for quantum computation. In quantum computation our tools for proving unconditional tradeoffs between time and space are surprisingly limited. The first quantum time-space tradeoff lower bounds were proven for sorting by Klauck, Spalek and de Wolf. Unfortunately, their method is limited to proving output-oblivious lower bounds (i.e. the lower bounds only apply to algorithms with a non-adaptive output schedule) and other methods have yielded nothing beyond output-oblivious lower bounds for sorting.We prove the first fully general quantum time-space tradeoff lower bound for sorting. We do so by introducing a novel method based on the noise operator to add to the analysis toolkit for proving quantum query and time space tradeoff lower bounds. By combining our resulting quantum noise stability bound with quantum recording query methods, we prove an Omega(n^{4/3} (log log n)/(S^{1/3} log n)) lower bound on the number of queries that a fully general quantum algorithm with at most S qubits of memory requires to sort n numbers from [n^2]. Applying our noise operator argument involves purely classical arguments, which makes it particularly simple to use. We also us it to prove that, for any strongly universal (pairwise independent) hash function family H from n bits to m bits, almost all hash functions in H require a quantum algorithm with at most S qubits of memory to make Omega(nm/S) queries to an input x in order to compute h(x), even with very small success probability. Previously, Mansour, Nisan, and Tiwari had shown a similar classical lower bound using their hash mixing lemma. Our noise operator method allows us to use a related but simpler property of hash functions to prove our lower bounds.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40334) | 2026-10-01
