---
title: "eigenkit: A Provider-Neutral Quantum Computing Library"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.02979"
summary: "arXiv:2611.02979v2 Announce Type: replace Abstract: Quantum software ecosystems provide increasingly capable tools for simulation and hardware execution, but differences in programming models, support"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.02979v2 Announce Type: replace Abstract: Quantum software ecosystems provide increasingly capable tools for simulation and hardware execution, but differences in programming models, supported features, and backend capabilities can make it difficult to move and systematically compare the same quantum algorithm across execution environments. We introduce eigenkit, a provider-neutral quantum computing library that separates algorithm definition from backend execution through a common circuit representation and provider interface. The library currently supports 12 execution providers spanning simulators and quantum hardware, provides backend-independent gradient computation, and integrates with standard scientific-computing and machine-learning workflows through NumPy, PyTorch, and scikit-learn interfaces. We evaluate the practical relevance of this abstraction across both simulation and quantum hardware. Simulator performance varies substantially with circuit size, structure, batching, and application workload, showing that no single backend is consistently preferable. On quantum hardware, experiments on IBM Heron and IQM Emerald show that which processor is better suited to a given algorithm depends not only on hardware constraints, but also on how well the topology of the quantum algorithm matches the physical connectivity of the processor. These results demonstrate that backend portability is not only a software-design convenience, but can be important for both computational efficiency and quantum execution quality.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.02979) | 2026-11-06
