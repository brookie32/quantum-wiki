---
title: "An Algorithm for Reversible Logic Circuit Synthesis Based on Tensor Decomposition"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2107.04298"
summary: "arXiv:2107.04298v5 Announce Type: replace-cross Abstract: An algorithm for reversible logic synthesis is proposed. The task is, for a given n-bit substitution map P_n: {0,1}^n rightarrow {0,1}^n, to f"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2107.04298v5 Announce Type: replace-cross Abstract: An algorithm for reversible logic synthesis is proposed. The task is, for a given n-bit substitution map P_n: {0,1}^n rightarrow {0,1}^n, to find a sequence of reversible logic gates that implements the map. The gate library adopted in this work consists of multiple-controlled Toffoli gates denoted by C^m!X, where m is the number of control bits that ranges from 0 to n-1. Controlled gates with large m ,,(>2) are then further decomposed into C^0!X, C^1!X, and C^2!X gates. A primary concern in designing the algorithm is to reduce the use of C^2!X gate (also known as Toffoli gate) which is known to be universal. The main idea is to view an n-bit substitution map as a rank-2n tensor and to transform it such that the resulting map can be written as a tensor product of a rank-(2n-2) tensor and the 2imes 2 identity matrix. Let P_n be a set of all n-bit substitution maps. What we try to find is a size reduction map A_{rm red}: P_n rightarrow {P_n: P_n = P_{n-1} otimes I_2}. %, where I_m is the mimes m identity matrix. One can see that the output P_{n-1} otimes I_2 acts nontrivially on n-1 bits only, meaning that the map to be synthesized becomes P_{n-1}. The size reduction process is iteratively applied until it reaches tensor product of only 2 imes 2 matrices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2107.04298) | 2026-07-31
