---
title: "Variational Perturbation Theory in Open Quantum Systems for Efficient Steady State Computation"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2504.00085"
summary: "arXiv:2504.00085v4 Announce Type: replace Abstract: Determining the steady state of an open quantum system is crucial for characterizing quantum devices and studying various physical phenomena. Often,"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2504.00085v4 Announce Type: replace Abstract: Determining the steady state of an open quantum system is crucial for characterizing quantum devices and studying various physical phenomena. Often, computing a single steady state is insufficient, and it is necessary to explore its dependence on multiple external parameters. In such cases, calculating the steady state independently for each combination of parameters quickly becomes intractable. Perturbation theory (PT) can mitigate this challenge by expanding steady states around reference parameters, minimizing redundant computations across neighboring parameter values. However, PT has two significant limitations: it relies on the pseudo-inverse -- a numerically costly operation -- and has a limited radius of convergence. In this work, we remove both of these roadblocks. First, we introduce a variational perturbation theory (VPT) and its multipoint generalization that significantly extends the radius of convergence even in the presence of non-analytic effects such as dissipative phase transitions. Then, we develop two numerical strategies that eliminate the need to compute pseudo-inverses. The first relies on a single LU decomposition to efficiently construct the steady state within the convergence region, while the second reformulates VPT as a Krylov space recycling problem and uses preconditioned iterative methods. We benchmark these approaches across various models, demonstrating their broad applicability and significant improvements over standard PT.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2504.00085) | 2026-10-21
