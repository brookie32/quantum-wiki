---
title: "Quantum Amplitude Estimation for Travel Time Estimation in Stochastic Vehicle Routing Problems"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.06145"
summary: "arXiv:2608.06145v1 Announce Type: new Abstract: Solving the Vehicle Routing Problem (VRP) in Stochastic Transportation Networks (STNs), a core task in Intelligent Transportation Systems (ITS), introdu"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.06145v1 Announce Type: new Abstract: Solving the Vehicle Routing Problem (VRP) in Stochastic Transportation Networks (STNs), a core task in Intelligent Transportation Systems (ITS), introduces estimation challenges for stochastic path travel times and the resulting VRP objective function. These challenges have typically been addressed through computationally expensive sampling-based techniques such as Monte Carlo simulation, whose performance depends on sample size, the sampling strategy, and the underlying travel time distributions. To address these issues, this study proposes and validates a quantum computing technique, Quantum Amplitude Estimation (QAE) for path-level travel time estimation in STNs. Without relying on sampling or prior assumptions of the travel time distribution, the proposed framework encodes all feasible travel time realizations into a quantum superposition, enabling a theoretical quadratic speed-up over Monte Carlo simulation. Four QAE variants are implemented in IBM's Qiskit framework, namely Canonical AE (CAE), Iterative AE (IAE), Maximum Likelihood AE (MLAE), and Faster AE (FAE), together with four rotation-angle scaling strategies for handling different discrete travel time distributions. Experiments on a small-scale STN show that the choice of scaling method and rotation-angle range significantly affects estimation accuracy, while the four QAE variants produce comparable estimates across all tested conditions, with IAE exhibiting the most stable overall performance. The results provide practical guidance on parameter selection for future hybrid quantum-classical optimization frameworks in ITS applications.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.06145) | 2026-08-07
