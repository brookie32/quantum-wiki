---
title: "Quantum Sampling of Random Spanning Trees via Amortized Data Structures"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40314"
summary: "arXiv:2609.40314v1 Announce Type: new Abstract: We present a quantum algorithm that generates a uniform superposition over the spanning trees of a graph -- also known as a q-sample -- using only a sub"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40314v1 Announce Type: new Abstract: We present a quantum algorithm that generates a uniform superposition over the spanning trees of a graph -- also known as a q-sample -- using only a sub-linear number of queries to the graph. This goes beyond previous work that focuses on generating classical samples, including a recent quantum algorithm by Apers, Gao, Ji, and Liu [ICALP 2025]. For an n-vertex, m-edge graph, our algorithm admits a pre-processing step of ilde{O}(sqrt{mn} + m^{1-elta}), after which each q-sample can be generated in ilde{O}(n^{1+2elta}) for any elta. Alternatively, k independent q-samples can be generated at a total cost of ilde{O}(sqrt{kmn}). We also prove a matching lower bound up to logarithmic factors, showing that our algorithm is essentially optimal. Further tradeoffs are given in the paper. In comparison, the optimal classical algorithms (Anari, Liu and Vuong [FOCS 2022]) need an ilde{O}(m) pre-processing step, after which each sample costs ilde{O}(n) operations. These results yield faster quantum walk-based algorithms for counting spanning trees or finding a marked one. Our result is obtained via quantum walk sampling over a sequence of slowly-changing Markov chains. Each chain is an isotropized up-down walk that mixes rapidly to the spanning tree distribution of the input graph. A key ingredient is an amortized data structure supporting fast implementation of the associated quantum walk operators throughout the sequence. This data structure maintains access to a spectral sparsifier and a leverage score sampler that evolve with the underlying graph.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40314) | 2026-10-01
