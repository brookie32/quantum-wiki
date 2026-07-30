---
title: "Hardware-Aware QUBO Reformulation of Constrained Binary Optimization via the Walsh-Fourier Transform"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.26349"
summary: "arXiv:2607.26349v1 Announce Type: new Abstract: We present a novel slack-free, penalty-based framework for reformulating constrained binary optimization as Quadratic Unconstrained Binary Optimization "
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.26349v1 Announce Type: new Abstract: We present a novel slack-free, penalty-based framework for reformulating constrained binary optimization as Quadratic Unconstrained Binary Optimization (QUBO) on near-term quantum annealing hardware. Given a user-chosen penalty function that most naturally captures a constraint---typically non-quadratic, such as a Heaviside-function surrogate---and a target probability measure over the Boolean hypercube, our method returns the weighted least-squares projection of the chosen penalty function onto the subspace spanned by linear and quadratic Walsh--Fourier characters that correspond to physically realizable couplings on the target hardware graph. Within this restricted family, the resulting quadratic surrogate is uniquely and optimally determined by the normal equations: unlike state-of-the-art approaches, it introduces no per-constraint penalty coefficients to tune and avoids dense all-pairs couplings by construction. Two practical consequences follow. First, the projected penalty respects device connectivity, reducing chain lengths and physical-qubit overhead after minor embedding. Second, we show empirically that this hardware-native surrogate can outperform denser full-pairwise projections, despite being drawn from a strictly smaller approximation space. This advantage widens once the QUBO is embedded and sampled on quantum annealers, yielding samples with the lowest worst-case and mean objective gaps compared to unbalanced penalization and a hardware-blind projection onto all quadratic terms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.26349) | 2026-07-30
