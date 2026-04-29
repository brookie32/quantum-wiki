---
title: "Experimental Workflows for Combinatorial Optimization: Towards Quantum Advantage"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25162"
summary: "arXiv:2604.25162v1 Announce Type: new Abstract: Demonstrating quantum advantage for combinatorial optimization requires more than standalone algorithmic results; it calls for end-to-end case studies t"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25162v1 Announce Type: new Abstract: Demonstrating quantum advantage for combinatorial optimization requires more than standalone algorithmic results; it calls for end-to-end case studies that integrate problem modelling, quantum execution, and classical refinement into practical workflows. This paper presents a sandbox platform for experimenting with hybrid quantum-classical workflows in graph optimization, enabling the systematic study of end-to-end optimization pipelines. Using our platform, we investigate three classically intractable and mutually reducible graph problems -- Minimum Vertex Cover, Maximum Independent Set, and Maximum Clique -- by transforming them into an unconstrained problem and solving the resulting instances with QAOA on IBM platforms. Our workflow combines classical pre-processing to reduce instance size, quantum optimization on the reduced problem, and classical postprocessing to map quantum outputs to high-quality feasible solutions, thereby avoiding direct constraint encoding in the quantum circuit. We evaluate the approach on synthetic graphs, benchmark instances, and real-world networks, and report hardware experiments on IBM Quantum System One at PINQ2 in Bromont, Quebec, powered by IBM's 156-qubit Heron r2 processor on graphs up to 128 vertices, with circuits involving up to 128 qubits and 13,555 two-qubit gates. The results illustrate how sandbox-style end-to-end experimentation can expose bottlenecks, clarify the role of classical-quantum workload partitioning, and provide domain experts and practitioners with a practical guide for interpreting quantum optimization outputs and assessing quantum utility on the road to quantum advantage in combinatorial optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25162) | 2026-04-29
