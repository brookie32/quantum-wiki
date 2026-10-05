---
title: "When Normalization Selects the Sign: Auditing Robustness Ablations in Quantum Attention"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02641"
summary: "arXiv:2610.02641v1 Announce Type: new Abstract: Removing an input-scaling module changes both a classifier and the perturbations reaching its encoder. A robustness difference can therefore reflect the"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.02641v1 Announce Type: new Abstract: Removing an input-scaling module changes both a classifier and the perturbations reaching its encoder. A robustness difference can therefore reflect the comparison rule as well as the module. We demonstrate this problem in a four-qubit quantum-attention detector on generated power-grid trajectories. A learned scaling module appears beneficial at a fixed physical attack budget, but matching an upper bound on perturbations at the encoder reverses the ordering. Neither comparison alone establishes a robustness benefit caused by the module. The initial test also perturbs clean examples into attacked examples while retaining their original labels; tests restricted to already attacked examples do not establish a benefit. Replacing a trained model's input scales disrupts detection. Retraining its linear classification layer restores the detection rate, but changes individual predictions, leaving the comparison descriptive rather than causal. Two further design checks explain why the input quantum Fisher information regularizer cannot train this model's query parameters, and why removing confidence bounds does not establish a larger certified radius. The evidence is limited to ten seeds, exact simulation, synthetic data, and a restricted set of attacks; classical baselines achieve better clean prediction. The practical lesson is to specify which perturbation budget is fixed, check that attacks preserve labels and interventions preserve predictions, and distinguish exploratory controls from confirmatory evidence.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02641) | 2026-10-05
