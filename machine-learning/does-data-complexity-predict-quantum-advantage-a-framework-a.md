---
title: "Does Data Complexity Predict Quantum Advantage? A framework, a pre-specified test, and an attribution of the measured edge"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.16410"
summary: "arXiv:2509.16410v2 Announce Type: replace Abstract: Quantum machine learning (QML) holds promise for pattern recognition, optimization, and data analysis, but the conditions under which it can outperf"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2509.16410v2 Announce Type: replace Abstract: Quantum machine learning (QML) holds promise for pattern recognition, optimization, and data analysis, but the conditions under which it can outperform classical methods remain unclear. We propose data complexity--the structural, statistical, algorithmic, and topological richness of a dataset--as a central axis for stating such conditions, and test the resulting framework under a pre-specified benchmark. The central predictive claim fails. A composite complexity measure does not predict the budget-matched quantum edge across 27 datasets in leave-one-dataset-out validation (pooled R^2=-0.32, versus a pre-specified threshold of 0.4). The failure is strongly coupled to the classical baseline: against logistic regression, the selector reaches R^2=+0.13 and the parity family wins 17% of cells, whereas against the best of six standard classical models performance falls to R^2=-0.94, with parity winning only 1%. The apparent signal therefore tracks classical model error rather than a robust quantum contribution. The tested encoding and reduction procedures further leave little nonlinear headroom for the downstream model to exploit; gradient boosting matches a linear probe across the tested widths. The null is also constrained by the regime: quantum performance is at chance in 81.5% of cells. Yet a deliberately constructed quantum-signature control produces a +0.42 edge under a structure-aware measurement, while generic models required to learn that structure remain near chance. Thus the null result is not evidence that quantum-sensitive structure cannot exist. Rather, in the tested regime, data complexity alone does not predict quantum advantage: the observable edge depends jointly on the classical baseline, accessible data structure, representation and model headroom, and whether quantum-sensitive structure is accessible to the measurement.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.16410) | 2026-10-09
