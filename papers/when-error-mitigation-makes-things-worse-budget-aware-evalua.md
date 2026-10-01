---
title: "When Error Mitigation Makes Things Worse: Budget-Aware Evaluation, Extrapolation Failure, and the Calibration Trust Boundary"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38713"
summary: "arXiv:2609.38713v1 Announce Type: new Abstract: Error mitigation is expected to turn noisy quantum measurements into more useful estimates. We show that it can instead amplify error. Under control-off"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38713v1 Announce Type: new Abstract: Error mitigation is expected to turn noisy quantum measurements into more useful estimates. We show that it can instead amplify error. Under control-offset miscalibration, the evaluated unconstrained zero-noise extrapolation (ZNE) estimators are worse than no mitigation on 38-63% of simulated instances and produce extreme tail errors. A small IBM Heron study finds worsening on 80-88% of 18 instances across two depths, with mean error 3.0-4.1 times the raw error. In simulation, the median changes little, so median-only monitoring misses the failures. We then compare methods at the same online shot budget per evaluation and report offline training cost separately. After that cost is amortized, a budget-conditioned neural corrector occupies the low-budget end of the simulated accuracy-cost frontier and falls back to the raw estimate when an ensemble disagrees; its hardware transfer remains unsuccessful. Finally, we treat provider-reported calibration as an input that is not bound to the execution-time device state. A white-box projected-gradient stress test on this metadata increases the corrector's error 8.1 times within the feature ranges used for training and evades the disagreement monitor on half of the worsened cases. Together, the results connect budget-aware evaluation, tail risk, and calibration integrity in near-term quantum learning pipelines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38713) | 2026-10-01
