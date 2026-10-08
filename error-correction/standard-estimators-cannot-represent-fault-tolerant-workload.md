---
title: "Standard estimators cannot represent fault-tolerant workloads at measured error rates: evaluated, evidence-based uncertainty for quantum resource estimation"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.10490"
summary: "arXiv:2610.10490v1 Announce Type: new Abstract: Estimates of the quantum resources needed to run fault-tolerant algorithms are almost always reported as single numbers, even though they rest on uncert"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.10490v1 Announce Type: new Abstract: Estimates of the quantum resources needed to run fault-tolerant algorithms are almost always reported as single numbers, even though they rest on uncertain hardware parameters and on cost models that disagree. We present an open, tool-agnostic framework that propagates evidence-based priors over fault-tolerant hardware parameters through five surface-code cost models, adds correlated-input sensitivity analysis, and evaluates the resulting intervals with a pre-registered three-layer protocol. Applied to RSA-2048, ECC-256, AES-256, and a Hubbard-model simulation on a superconducting surface-code architecture, it produces three coupled findings that together undermine the single-number convention. Propagating the error rates hardware has actually demonstrated, whose median across five large-array devices is about 4 x 10^-3 rather than the conventional 10^-3, widens the 90% physical-qubit interval to roughly forty times and lifts its median about 4.6 times above the conventional point estimate. Against the same inputs, five independently structured cost models, including two third-party estimators (the Azure Quantum Resource Estimator and Qualtran) that agree with each other to within about ten percent, disagree by a stable factor of two, a structural uncertainty that no single tool reveals. Most consequentially, both third-party estimators exceed their representable envelope for 80 to 100 percent of the evidence-based parameter space, and the AES-256 gate count overflows one tool's counter outright, so these workloads cannot be represented at measured error rates at all. The optimistic convention conceals every one of these effects. The uncertainty machinery we use is standard. The contribution is its evidence-based application, the pre-registered evaluation, and the finding that standard tools break down precisely where hardware operates.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.10490) | 2026-10-08
