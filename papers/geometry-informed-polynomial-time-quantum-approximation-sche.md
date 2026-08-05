---
title: "Geometry-Informed Polynomial Time Quantum Approximation Schemes for Constrained Optimisation"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.01121"
summary: "arXiv:2608.01121v1 Announce Type: new Abstract: When does a noisy quantum sampler yield an end-to-end polynomial-time optimization algorithm with performance guarantees? Building on finite-depth and f"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.01121v1 Announce Type: new Abstract: When does a noisy quantum sampler yield an end-to-end polynomial-time optimization algorithm with performance guarantees? Building on finite-depth and finite-shot guarantees for Constraint-Enhanced QAOA, we show that inverse-polynomial ideal probability on the optimal set, together with independent sampling, polynomial-time feasibility repair, and scoring, produces an exact-hit fully polynomial randomized approximation scheme, which we call an FPRASq. This guarantee survives device noise within an instance-dependent window. For effective circuit depth linear in the product of layer count and problem size, preserving an inverse-depth fraction of the ideal optimal mass increases the required shot complexity by one power of the problem size. Beyond this window, deterministic repair guarantees feasibility and provides an instance-dependent approximation guarantee whenever the induced objective inflation is controlled. The resulting NP-HQ algorithm fits the Chen-Cotler-Huang-Li oracle model. On any NP-hard kernel-admissible promise family, reproducing its inverse-polynomial optimal overlap with a polynomial-time classical sampler would imply that NP is contained in BPP, even with identical repair and perfect access to the constraint structure. Thus, the separation lies in generating the sampling distribution. We further introduce Heavy-Hitter QAOA, which preserves these conditional guarantees while reducing the retained candidate set and classical post-processing cost by one power of the problem size. Hardware experiments on IBM Eagle r3 processors cover instances with up to one hundred logical variables and match or improve every tested QOptlib reference tour.



## Related
- [[a-swap-free-framework-for-qaoa|A SWAP-free Framework for QAOA]]
- [[reductions-of-qaoa-induced-by-classical-symmetries-theoretic|Reductions of QAOA Induced by Classical Symmetries: Theoretical Insights and Practical Implications]]
- [[query-efficient-quantum-approximate-optimization-via-graph-c|Query-Efficient Quantum Approximate Optimization via Graph-Conditioned Trust Regions]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.01121) | 2026-08-04
