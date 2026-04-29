---
title: "Query-Efficient Quantum Approximate Optimization via Graph-Conditioned Trust Regions"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24803"
summary: "arXiv:2604.24803v1 Announce Type: cross Abstract: In low-depth implementations of the Quantum Approximate Optimization Algorithm (QAOA), the dominant cost is often the number of objective evaluations "
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.24803v1 Announce Type: cross Abstract: In low-depth implementations of the Quantum Approximate Optimization Algorithm (QAOA), the dominant cost is often the number of objective evaluations rather than circuit depth. We introduce a graph-conditioned trust-region method for reducing this query cost. A graph neural network predicts a Gaussian distribution N(mu, Sigma) over QAOA angles. The mean initializes a local optimizer, the covariance defines an ellipsoidal trust region that constrains the search, and the predicted uncertainty determines an instance-dependent evaluation budget. Thus the learned distribution defines a search policy rather than only an initial parameter estimate. Under explicit assumptions on local smoothness, curvature, calibration, and noise, we derive bounds on objective degradation within the trust region, lower bounds on gradient variance, preservation of expected objective ordering under depolarizing noise, and finite-sample coverage guarantees. We evaluate the method for MaxCut at depth p = 2 on Erdos-Renyi, 3-regular, Barabasi-Albert, and Watts-Strogatz graphs with n = 8-16 vertices. Relative to random restarts and the strongest learned point-prediction baseline, the method reduces the mean number of circuit evaluations from 343 and 85 to 45 +/- 7, while maintaining sampled approximation ratios within 3 percentage points of concentration-based heuristics. The method does not improve absolute approximation ratios; its advantage is reduced query cost at comparable solution quality. The predictive uncertainty is calibrated in the experiments, with ECE = 0.052 and Spearman correlation rho = 0.770, and the learned trust regions transfer to graph sizes not used during training. The results identify a low-depth, query-dominated regime in which graph-conditioned trust regions reduce the query cost of QAOA without modifying the ansatz.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24803) | 2026-04-29
