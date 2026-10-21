---
title: "Fundamental Limitations of QAOA on Constrained Problems and a Route to Exponential Enhancement"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.17259"
summary: "arXiv:2511.17259v5 Announce Type: replace Abstract: We study the feasibility limitations of generic QAOA for permutation-constrained optimization, where valid configurations occupy an exponentially sm"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2511.17259v5 Announce Type: replace Abstract: We study the feasibility limitations of generic QAOA for permutation-constrained optimization, where valid configurations occupy an exponentially small fraction of the Boolean hypercube. Using random edge-cost TSP/ATSP ensembles, we establish high-probability bounds showing that optimized generic QAOA retains exponentially small feasible probability over specified parameter domains. At depth one, the bound holds uniformly over all mixer angles and a cost-angle grid that may be exponentially large in n^2. The analysis combines Walsh-Fourier/Krawtchouk estimates, which suppress low- and high-degree contributions, with transition-feature collision bounds controlling objective-dependent interference. Complementary cost-angle averaging, fourth-moment estimates, and light-cone analysis characterize energy-fibre coherence, typical-angle concentration, and constraint-correlation geometry. We compare generic QAOA with a constraint-enhanced kernel (CE-QAOA) initialized in a product one-hot subspace and evolved with a block-local XY mixer. For N = n^2 binary variables, CE-QAOA attains feasible probability at least n!/n^n at every depth, yielding an exp[Omega(n^2)] advantage over optimized generic QAOA at depth one with high probability. For linked cost-angle schedules with independently optimized mixer angles, the generic feasibility obstruction and exponential CE-QAOA separation extend throughout linear-depth windows p 0. These parameter-uniform bounds also imply exponential raw-sample requirements for adaptive feasible sampling within the prescribed domains.



## Related
- [[landscape-compression-in-constrained-qaoa-tracks-feasibility|Landscape Compression in Constrained QAOA Tracks Feasibility Loss on IBM Heron Hardware]]
- [[convergence-guarantee-for-linearly-constrained-combinatorial|Convergence guarantee for linearly-constrained combinatorial optimization with a quantum alternating operator ansatz]]
- [[separating-geometry-from-interference-in-constrained-quantum|Separating Geometry From Interference in Constrained Quantum Optimization]]
- [[the-expressive-power-of-constrained-qaoa-what-you-might-have|The Expressive Power of Constrained QAOA: What You Might Have MISsed]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.17259) | 2026-10-15
