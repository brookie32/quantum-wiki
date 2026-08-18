---
title: "FedQML-Edge: Compact Quantum Feature Sketches for Communication-Constrained Roadside Federated Learning"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.28799"
summary: "arXiv:2607.28799v1 Announce Type: new Abstract: Roadside units (RSUs) supporting connected and autonomous vehicle corridors need compact models to decide when cooperative maneuvers should be rewarded,"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2607.28799v1 Announce Type: new Abstract: Roadside units (RSUs) supporting connected and autonomous vehicle corridors need compact models to decide when cooperative maneuvers should be rewarded, deferred, or disabled. Raw sensor streams and neural network weight checkpoints are poorly suited to bandwidth-limited, privacy-sensitive roadside learning. This paper presents exttt{FedQML-Edge}, a federated quantum feature-sketching pipeline for traffic-stability gating. Each RSU constructs a traffic-state summary and sends circuit inputs to a quantum computer; Pauli expectations form a nonlinear sketch processed by a logistic classifier. Only classifier updates are shared with an aggregator, whose head supports reward gating. Raw observations, vehicle records, event traces, and quantum sketches remain private. We evaluate the method using NGSIM trajectories, SUMO predictive gating with sensing noise, and IBM Quantum hardware. On NGSIM, the Pauli sketch reduces test log loss by 14.4% relative to the strongest matched classical sketch. On SUMO, it approaches larger MLPs in stable-window recall while using 7-28 times less communication per round.



## Related
- [[hybrid-quantum-inspired-kolmogorov-arnold-networks-for-priva|Hybrid Quantum-inspired Kolmogorov-Arnold Networks for Privacy-Aware Federated Biosignal Learning]]
- [[pas-qfl-personalized-ansatz-selection-for-quantum-federated-|PAS-QFL: Personalized Ansatz Selection for Quantum Federated Learning under Client Data Heterogeneity]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.28799) | 2026-08-03
