---
title: "What a Reporting Convention Hides: A Matched-Budget Audit of Quantum Natural Gradient with an Exactly Computed Metric"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.09425"
summary: "arXiv:2610.09425v1 Announce Type: cross Abstract: Several published comparisons of variational quantum optimizers time only runs that reach a target loss, or read the verdict at a single target. Eithe"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.09425v1 Announce Type: cross Abstract: Several published comparisons of variational quantum optimizers time only runs that reach a target loss, or read the verdict at a single target. Either convention could decide whether an optimizer's costlier steps pay off. We measure how much each convention changes verdicts among Adam, simultaneous perturbation stochastic approximation (SPSA) and quantum natural gradient (QNG), on initializations held out from the selection of settings. We compute the exact metric that preconditions QNG, price every step in circuit evaluations and give every method the same budget. In a median pooled over circuit widths, cost families and a sweep of settings with common misses, SPSA needs more than twice Adam's evaluations to reach a loose target. Dropping the censored runs that miss the target hides this gap. On the global-cost family we hold fixed the settings selected for a strict target. QNG then usually reaches the loose target after Adam but the strict target first. QNG's strict-target lead disappears when the metric's simulator price, linear in the number of parameters, is replaced by an assumed hardware count quadratic in that number. We recommend charging every miss the budget and reporting verdicts across targets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.09425) | 2026-10-08
