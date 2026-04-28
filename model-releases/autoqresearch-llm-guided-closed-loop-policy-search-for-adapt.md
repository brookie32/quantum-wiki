---
title: "AutoQResearch: LLM-Guided Closed-Loop Policy Search for Adaptive Variational Quantum Optimization"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24283"
summary: "arXiv:2604.24283v1 Announce Type: new Abstract: Configuring variational quantum algorithms for combinatorial optimization remains a difficult, expert-driven process requiring coordinated choices over "
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24283v1 Announce Type: new Abstract: Configuring variational quantum algorithms for combinatorial optimization remains a difficult, expert-driven process requiring coordinated choices over solver family, ansatz, objective, and optimizer. We present AutoQResearch, an LLM-guided closed-loop experimentation framework that casts this task as sequential policy search over a curated design space. Instead of a single static configuration, the framework searches for adaptive solver-control policies that condition future decisions on diagnostics such as feasibility, optimality gap, and convergence stagnation. The system operates through a structured workflow: an LLM agent edits a small policy surface under a fixed evaluation harness, candidate policies are screened using cheap scout evaluations, and only the strongest candidates are promoted to full confirmation. This enables controlled autonomous exploration while guarding against proxy overfitting and unstable selection. We evaluate the framework on Maximum Independent Set (MIS) and the Capacitated Vehicle Routing Problem (CVRP). On MIS instances (16--64 vertices), discovered policies substantially outperform static baselines and reveal scale-dependent behavior: CVaR objectives are effective at small scale, while QRAO-based qubit compression provides the most effective explored scaling path. On CVRP curricula (8--12 customers) and a held-out E-n13-k4 benchmark, the framework discovers adaptations involving sampling budget, penalty design, and hybrid repair protocols, yielding high-quality solutions. Methodologically, we find that staged confirmation is essential: cheap proxy evaluations can materially misestimate policy quality and even invert candidate rankings. Overall, the paper positions AutoQResearch as a benchmarked quantum--GenAI co-design workflow for autonomous solver discovery in variational quantum optimization.



## Related
- [[calibrating-the-role-of-entanglement-in-variational-quantum-|Calibrating the Role of Entanglement in Variational Quantum Algorithms from a Geometric Perspective]]
- [[a-spectral-gap-informed-parameter-schedule-for-qaoa|A Spectral Gap Informed Parameter Schedule for QAOA]]
- [[do-quantum-transformers-help-a-systematic-vqc-architecture-c|Do Quantum Transformers Help? A Systematic VQC Architecture Comparison on Tabular Benchmarks]]
- [[exhaustive-and-feasible-parametrisation-with-applications-to|Exhaustive and feasible parametrisation with applications to the travelling salesperson problem]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24283) | 2026-04-28
