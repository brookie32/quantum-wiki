---
title: "DIME: Query-Efficient Framework for Membership Inference on Diffusion Models"
date: "2026-08-24"
updated: "2026-08-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1791"
summary: "Membership inference attacks expose whether individual records were used to train a model, yet existing attacks on diffusion models are largely heuristic and can require substantial query budgets. We "
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

Membership inference attacks expose whether individual records were used to train a model, yet existing attacks on diffusion models are largely heuristic and can require substantial query budgets. We introduce extbf{DIME} (extbf{D}enoiser extbf{I}deal extbf{M}embership extbf{E}rror), a theoretically grounded and query-efficient framework for membership inference on diffusion models. Our starting point is an exact characterization of the optimal diffusion denoiser for a finite training set, which reveals that membership leakage is governed by the denoiser's implicit reconstruction error. This error decomposes into two complementary signals: a extit{bias term}, capturing reconstruction accuracy, and a previously unexplored extit{local crowding term}, capturing the geometry of nearby training examples. Both admit efficient estimators using only model queries, yielding a practical attack with as few as two queries. Across CIFAR-10/100, STL10-U, CelebA, and ImageNet, extbf{DIME} consistently outperforms prior attacks at comparable or substantially lower query cost, improving TPR at 1% FPR by up to 3imes; remarkably, its two-query variant can outperform existing 30-query baselines. Finally, we suggest, discuss, and evaluate specific defenses to counteract such powerful membership tests.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1791) | 2026-08-24
