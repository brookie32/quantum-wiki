---
title: "LatticeMind: A Validation-Gated Agentic Framework for Density Functional Theory Workflows"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.26869"
summary: "arXiv:2610.26869v1 Announce Type: cross Abstract: First-principles calculations are rarely single solver calls: they are multistage workflows in which structures, settings, and saved densities must pa"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.26869v1 Announce Type: cross Abstract: First-principles calculations are rarely single solver calls: they are multistage workflows in which structures, settings, and saved densities must pass correctly between dependent stages. Language models can write a valid single input, but reliability collapses once stages are chained: a dropped dependency, wrong file handoff, or hallucinated keyword can invalidate results even when the solver runs, and such errors surface only after costly execution. We introduce LatticeMind, a validation-gated agentic framework that converts natural-language requests into executable, checkable density functional theory (DFT) projects. A workflow contract specifies required stages, files, and dependencies; deterministic validators inspect the project before any solver launch; failed checks trigger bounded repair; and reports remain traceable to project files. On a 44-case RESCU benchmark spanning total-energy, density-of-states, band-structure, magnetic, phonon workflows, three non-flagship LLM backends reproduced every reference value; 119 of 132 runs passed on the first validated plan and the rest after one repair cycle. Ablations identify the workflow contract and pre-execution validation as the principal reliability mechanisms; a conventional trial-and-repair baseline reaches 71% at twice the token cost per success. The same architecture reproduces every reference value on a 19-case VASP benchmark, demonstrating transfer across solvers. Beyond these task families, LatticeMind generated and validated the 23 inputs of a multistage study of Rh-induced electronic responses at a Rh_6/In_xGa_{1-x}N photocatalyst interface. These results establish workflow contracts, deterministic validation, bounded repair, and traceable records as a practical foundation for reliable AI-assisted scientific computing, where preventable errors are caught before execution and the solver is never the first validator.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.26869) | 2026-10-21
