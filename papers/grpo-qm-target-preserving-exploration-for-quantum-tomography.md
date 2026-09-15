---
title: "GRPO-QM: Target Preserving Exploration for Quantum Tomography"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.14711"
summary: "arXiv:2609.14711v1 Announce Type: cross Abstract: Reward-based learning can alter the very posterior distribution that scientific inference aims to estimate. GRPO-QM sidesteps this by learning only an"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.14711v1 Announce Type: cross Abstract: Reward-based learning can alter the very posterior distribution that scientific inference aims to estimate. GRPO-QM sidesteps this by learning only an exploration strategy for a stated quantum-tomography posterior: a group-relative policy chooses among reversible physical moves, and an exact Metropolis correction ensures the posterior remains stationary once the policy is fixed. We then examine what learning contributes beyond physical proposal mechanisms and prior knowledge. Reconstruction comparisons suggest that most of the gains over the tested flows come from those two components rather than from learning itself, and a closed-form counterexample explains why: a reward tied to accepted motion can increase even when a physical observable remains highly correlated. Reward comparisons that control for initialization also show that aggregating across posteriors can invert the ranking that a reward implies within any single posterior. Lastly, on 45 enumerated posteriors with three training seeds each, exact and sampled gradients of the same trajectory objective reduce mean physical estimation variance by 12.63% and 6.32% relative to a tuned mixture, while averaging the trajectory score without rescaling its penalty yields only 0.43%. This indicates that objective scaling accounts for part of the disparity between sampled and exact training. The regained benefit is concentrated at four shots and flips sign at sixteen, so these exact, visible-bank diagnostics identify a concrete, reproducible failure mode in sampled training, the objective-scaling fix that addresses part of it, and the remaining gap.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.14711) | 2026-09-15
