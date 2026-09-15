---
title: "Can Autonomous LLM Agents Execute Multireference Quantum Chemistry Calculations?"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.13357"
summary: "arXiv:2609.13357v1 Announce Type: new Abstract: Multireference electronic-structure calculations remain difficult to automate because critical workflow decisions, including active-space selection, sta"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.13357v1 Announce Type: new Abstract: Multireference electronic-structure calculations remain difficult to automate because critical workflow decisions, including active-space selection, state averaging, convergence recovery, and state identification, traditionally rely on expert judgment. Here, we investigate whether an autonomous large language model (LLM) agent can perform these tasks without human intervention. The agent selects active spaces using literature-grounded analogies or explicitly documented chemical reasoning, generates and submits ORCA calculations, analyzes outputs, and records all decisions in an auditable reasoning log. Benchmarking against 558 vertical transition energies (VTEs) from QUESTDB shows that an unguided baseline agent achieves 24.9% coverage with a mean absolute error (MAE) of 0.373 eV. Introducing a structured decision ladder increases coverage to 44.1% while reducing the MAE to 0.339 eV. The largest gains are observed for double and Rydberg excitations, demonstrating that expert-informed procedural guidance substantially improves active-space construction and state identification. When provided with complete workflow information, the agent successfully reproduces published QUEST calculations with an MAE of only 23 meV, resolving 75% of target configurations within seven attempts. These results demonstrate that contemporary LLM agents can autonomously execute and reproduce complex multireference quantum-chemical workflows, while highlighting the importance of structured reasoning frameworks for achieving reliable high-throughput and high-fidelity electronic-structure calculations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.13357) | 2026-09-15
