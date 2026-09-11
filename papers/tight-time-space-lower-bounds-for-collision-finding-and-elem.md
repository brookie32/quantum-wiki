---
title: "Tight Time-Space Lower Bounds for Collision Finding and Element Distinctness under Label Symmetry"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.10808"
summary: "arXiv:2609.10808v1 Announce Type: new Abstract: How much memory is needed to retain the quantum speedup for collision finding? For a uniformly random function f:[N]o [N], the BHT algorithm finds a col"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.10808v1 Announce Type: new Abstract: How much memory is needed to retain the quantum speedup for collision finding? For a uniformly random function f:[N]o [N], the BHT algorithm finds a collision using O(N^{1/3}) queries and a quantumly accessible classical table containing O(N^{1/3}) input-output pairs, whereas a logarithmic-space Grover search uses O(sqrt N) queries. Determining the optimal query-space tradeoff between these extremes remains a major open problem. We resolve this equation within the class of label-symmetric algorithms, which treat the function f's output labels as interchangeable. We prove that such algorithm that makes T queries, uses S qubits, and finds a collision in a uniformly random function f:[M]o [N] with constant probability satisfies $T=Omega(N^{1/3}) qquadext{and}qquad T^2S=Omega(Nlog N). For the setting where M=N, these bounds are matched by a space-efficient implementation of the BHT algorithm. As a consequence of our tradeoff, any label-symmetric algorithm for the search version of Element Distinctness on f: [n] o [n^2] must satisfy T=Omega(n^{2/3}) qquadext{and}qquad T^2S=Omega(n^2log n), matching Ambainis's quantum walk. Thus, both tradeoffs are optimal within the class of label-symmetric algorithms. To prove these results, we develop a space-sensitive version of the compressed oracle technique. The compressed oracle records the information learned by the algorithm in an evolving superposition of databases. Using label symmetry and representation theory, we show that an algorithm using S qubits can effectively retain information about only O(S/log N)$ collision-free database entries. Substituting this estimate into the compressed oracle technique yields the stated tradeoffs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.10808) | 2026-09-11
