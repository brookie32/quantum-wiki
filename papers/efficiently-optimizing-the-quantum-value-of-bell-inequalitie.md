---
title: "Efficiently Optimizing the Quantum Value of Bell Inequalities using Batched Gradient Descent"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01699"
summary: "arXiv:2610.01699v1 Announce Type: new Abstract: Exploring the world of Bell inequalities requires numerical methods that scale effectively with the number of parties, inputs, and outputs. Such methods"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01699v1 Announce Type: new Abstract: Exploring the world of Bell inequalities requires numerical methods that scale effectively with the number of parties, inputs, and outputs. Such methods can be used to study large-scale Bell inequalities beyond the reach of analytic methods, to design experiments for violating more complicated Bell inequalities, and to enable applications of Bell inequality violation. Such applications include randomness generation and multi-agent coordination with restricted communication. However, current general purpose optimizers such as the see-saw method struggle to handle Bell inequalities with only a dozen inputs and outputs. We introduce an optimizer for the quantum value of a Bell inequality based on batched gradient descent (BGD). More precisely, our BGD optimizer is a differentiable search over feasible quantum strategies in which states and projective measurements are generated from unconstrained variables. The Bell expression is evaluated by a direct tensor contraction without forming the prohibitively large Bell operator. This formulation makes parallel random restarts inexpensive and is thus naturally implemented by a GPU. We evaluate our optimizer against the see-saw method and find a significant speedup for a wide variety of Bell inequality families. Implemented on a GPU, our BGD optimizer can optimize Bell inequalities in our numerical experiments with more than a thousand inputs or outputs within minutes. For these large-scale Bell inequalities, we also efficiently compute the classical value by enumerating possible strategies using a GPU or expressing the optimization as a mixed-integer linear program. Our optimizers can serve as numerical evaluation tools for Bell experiments and multi-agent coordination problems modeled by Bell inequalities with many inputs and outputs, a common feature of real-world scenarios such as high frequency trading and distributed systems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01699) | 2026-10-02
