---
title: "Quantum Fokker-Planck solvers as trainable generative models"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.31330"
summary: "arXiv:2610.31330v1 Announce Type: new Abstract: We develop and analyze generative models based on quantum solvers of stochastic differential equations. Unlike the common approach based on layered vari"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.31330v1 Announce Type: new Abstract: We develop and analyze generative models based on quantum solvers of stochastic differential equations. Unlike the common approach based on layered variational quantum circuits with parameterized rotations, we parameterize the potential of a Langevin process. The associated Fokker-Planck (FP) equations are Hermitianized and solved using a linear combination of cosine operators implemented through quantum singular value transformation. By encoding the square root of the stationary density, the model enables sampling through computational-basis measurements and is efficiently controlled by coefficients of the block-encoded diagonal potential. We train the proposed model to match empirical distributions within the family described by FP equations, demonstrating parameter recovery for multivariate probability distributions. Crucially, the model remains trainable at scale. Sample-efficient and convex optimization for in-distribution targets arises from a physics-informed inductive bias and holds regardless of the dimensionality of the problem. We provide circuit constructions and efficient block encodings of the main components of the algorithm and analyze resource requirements. Our approach frames quantum generative learning as quantum model discovery and provides a foundation for extending this framework to high-dimensional, strongly correlated scientific data.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.31330) | 2026-10-23
