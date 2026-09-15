---
title: "When is global evolutionary search useful for variational quantum algorithms? A landscape-first study"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.14594"
summary: "arXiv:2609.14594v1 Announce Type: new Abstract: Variational quantum algorithms recast state preparation as classical nonconvex optimization, but it is often unclear when multistart local search suffic"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.14594v1 Announce Type: new Abstract: Variational quantum algorithms recast state preparation as classical nonconvex optimization, but it is often unclear when multistart local search suffices and when population-based global search justifies its evaluation cost. Using a landscape-first design, controlled QAOA experiments identify two mechanisms making local search unreliable: parameter reuse across circuit layers and competition between 2-local and 3-local cost terms. Increasing QAOA depth alone does not replicate this effect. We test these mechanisms across eight unseen spin glasses, fresh N=10 and N=12 instances, and standard MaxCut, transverse-field Ising, and Heisenberg models. On all eight unseen spin glasses, adaptive differential evolution (DE) achieves lower median error than both multistart BFGS and multistart Powell on the two difficult constructions, whereas the independent-depth control does not. The parameter-reuse effect transfers to MaxCut at both sizes, while standard VQE models remain favorable to local search. A pre-benchmark landscape score combining random-start local outcomes and 1D parameter slices is fixed from confirmation data before evaluating new optimizers. It predicts whether adaptive DE outperforms multistart BFGS by over one spectral-range percentage point on 50 new quantum objectives with 80--86% condition-level accuracy. The clearest indicator of global-search utility is that local search frequently traps in inferior basins, rather than circuit depth or curvature anisotropy. The findings motivate whether quantum circuit complexity can be traded for harder classical optimization when robust global search is available.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.14594) | 2026-09-15
