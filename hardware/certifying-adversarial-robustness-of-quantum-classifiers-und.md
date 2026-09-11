---
title: "Certifying Adversarial Robustness of Quantum Classifiers under Known-Readout Query Access"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.11637"
summary: "arXiv:2609.11637v1 Announce Type: new Abstract: A quantum classifier assigns labels by evolving an input quantum state and measuring the output, so repeated executions reveal only a distribution over "
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.11637v1 Announce Type: new Abstract: A quantum classifier assigns labels by evolving an input quantum state and measuring the output, so repeated executions reveal only a distribution over labels. We study certified adversarial robustness for such classifiers under known-readout query access (KRQA), where an evaluator can prepare inputs, knows the quantum measurement, and observes finite-shot outcomes but cannot inspect the internal evolution, parameters, or gradients. We give a measurement-only framework that returns two complementary guarantees for each input: a lower bound ruling out untargeted errors within a radius, and an attack-independent upper bound witnessing an adversarial state within a radius. Both are estimable from the known readout measurement and sampled outcomes, require no tomography or circuit description, and admit finite-sample guarantees. The upper bound uses gap operators induced by the quantum measurement; the lower bound relaxes state-space search to an efficient optimization over outcome distributions with operator-spectrum constraints, yielding certificates that are never weaker than prior probability-only certificates and can be strictly stronger when the spectral constraints are active. Evaluations on multiple quantum classifiers show that the lower bound tracks exact optima on tractable instances, while the upper bound remains informative when standard attacks fail. We further demonstrate real-device feasibility on IBM Quantum hardware: from 40 executions of two 8-qubit quantum neural networks, our method computes both certificates, with the expected ordering between the lower and upper bounds on every tested input. Taken together, these results show that robustness claims for quantum classifiers can be audited directly from observable statistics under KRQA.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.11637) | 2026-09-11
