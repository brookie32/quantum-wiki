---
title: "Pareto-optimal quantum kernel selection for unsupervised anomaly detection on real malware beaconing data"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.09717"
summary: "arXiv:2610.09717v1 Announce Type: new Abstract: Quantum kernel methods are leading candidates for a practical quantum advantage in machine learning, but assessing that potential requires two quantitie"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.09717v1 Announce Type: new Abstract: Quantum kernel methods are leading candidates for a practical quantum advantage in machine learning, but assessing that potential requires two quantities usually reported separately: how well a kernel performs on the task, and how far its geometry departs from the classical kernels available for the same problem. We introduce a fully unsupervised, multi-objective protocol that optimises simultaneously the normalised pseudo discrepancy (NPD), a label-free proxy for anomaly detection quality, and the geometric difference (GD) to a tuned classical reference kernel, selecting models from the resulting Pareto front. We apply it to malware beaconing detection in real network traffic, using a one-class support vector machine with fidelity and projected quantum kernels over four data encodings, on simulators and on IQM's 20-qubit Garnet processor. NPD-guided selection alone finds a fidelity kernel that beats the tuned classical baseline, but with a geometric difference too small to certify the gain as quantum. Projected kernels reach far larger geometric differences; the Pareto-selected one only marginally exceeds the baseline (AUC 0.782 versus 0.765, g_{Co Q}approx 89>sqrt{N} relative to that reference kernel), still below the NPD-selected fidelity kernel (0.840).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.09717) | 2026-10-08
