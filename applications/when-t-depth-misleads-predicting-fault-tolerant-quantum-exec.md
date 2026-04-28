---
title: "When T-Depth Misleads: Predicting Fault-Tolerant Quantum Execution Slowdown under Magic-State Delivery Constraints"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "applications"
tags: [applications, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.11409"
summary: "arXiv:2604.11409v2 Announce Type: replace Abstract: The efficient execution of fault-tolerant quantum algorithms is fundamentally limited by the production rate of magic states required for non-Cliffo"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.11409v2 Announce Type: replace Abstract: The efficient execution of fault-tolerant quantum algorithms is fundamentally limited by the production rate of magic states required for non-Clifford operations. While circuit optimization typically targets T-depth, static T-depth does not reliably predict executable performance under bounded T-state delivery. We introduce a model that captures demand-supply imbalance using two key quantities: slack ratio, a structural indicator of scheduling flexibility, and Delta_max, a measure of cumulative demand surplus. We show that Delta_max is a strong schedule-level indicator of execution slowdown and yields a provable lower bound on executable makespan for a fixed schedule. Empirical evaluation on constructed directed acyclic graph (DAG) families, with arithmetic circuits and exact quantum Fourier transform (QFT) traces providing additional grounding, shows that slack ratio is a stronger structural predictor than T-depth for stall and inversion risk, while Delta_max is the strongest predictor of slowdown. Across 4,904 instances, the lower bound shows zero violations, with 88.9% of cases within one cycle. These results highlight the importance of explicitly modeling delivery constraints in fault-tolerant quantum compilation.



## Related
- [[taming-rydberg-decay-with-measurement-based-quantum-computat|Taming Rydberg Decay with Measurement-based Quantum Computation]]
- [[locating-rydberg-decay-error-in-swap-leakage-reduction-circu|Locating Rydberg Decay Error in SWAP-Leakage Reduction Circuit Protocol]]
- [[understanding-quantum-instruments|Understanding Quantum Instruments]]
- [[refining-quantum-phase-estimation-precision-conditions-on-un|Refining Quantum Phase Estimation Precision Conditions on Unitaries for Many-Electron Systems]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.11409) | 2026-04-28
