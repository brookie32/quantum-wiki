---
title: "Quantum Optimisation for Protein-Protein Interaction Network Alignment"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.05238"
summary: "arXiv:2609.05238v1 Announce Type: new Abstract: Protein-protein interaction (PPI) network alignment combines topological and sequence information to identify conserved modules across species, but glob"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.05238v1 Announce Type: new Abstract: Protein-protein interaction (PPI) network alignment combines topological and sequence information to identify conserved modules across species, but global alignment remains challenging: heuristics sacrifice optimality, while exact methods lack scalability. We model the alignment as a weighted maximum common induced subgraph problem and reformulate it through the modular product graph to a minimum-weight vertex cover on the complement, with node weights carrying sequence similarity. To solve this problem, we develop a hybrid framework combining kernelisation, branch-and-bound, and seven Quantum Approximate Optimisation Algorithm (QAOA) formulations. These formulations differ in how the cover constraints are enforced, from penalty terms in the cost Hamiltonian to mixers confined to the feasible subspace. For single round QAOA, we derive closed-form expressions for the expected cost of four circulant mixer variants, enabling performance characterisation without circuit simulation. Applied to synthetic and real-world networks reduced to KEGG pathways, the QAOA formulations achieve high topological conservation on the aligned core while at least maintaining biological conservation comparable to leading classical aligners, at the cost of reduced node coverage. Across selected KEGG pathways, the aligned subnetworks retain disease-associated proteins, preserving biologically relevant information. Cheaper formulations leave more edges uncovered, while enforcing feasibility in the mixer raises circuit depth by one to two orders of magnitude. Together, these results highlight the potential of quantum optimisation for PPI network alignment and the resource trade-offs that will shape its scalability as quantum hardware matures.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.05238) | 2026-09-07
