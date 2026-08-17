---
title: "Quantum Multi-Armed Bandits and Linear Bandits: Lower Bounds and Algorithms"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.14319"
summary: "arXiv:2608.14319v1 Announce Type: cross Abstract: We study quantum multi-armed bandits (QMAB) and quantum linear bandits (QLB) in the model of Wan et al. [2023], where the learner queries each arm or "
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2608.14319v1 Announce Type: cross Abstract: We study quantum multi-armed bandits (QMAB) and quantum linear bandits (QLB) in the model of Wan et al. [2023], where the learner queries each arm or action through a quantum reward oracle or its inverse. Prior work gives algorithms over horizon T with regret O(Klog T) for QMAB with K arms and O(d^2operatorname{polylog} T) for d-dimensional QLB. This leaves open whether the Klog T scale is unavoidable and whether the d^2 dependence can be improved. We prove the first minimax lower bounds of Omega(Klog(T/K)) for QMAB and Omega(dlog(T/d)) for finite-action QLB, resolving the question raised by Wan et al. [2023] of whether regret independent of T is achievable. At the heart of our argument is a high-confidence single-arm quantum testing lower bound for distinguishing a fixed reward mean from an interval of alternatives, proved by the polynomial method and a Remez-type inequality for trigonometric polynomials. A bandit-to-testing reduction then lifts it to the QMAB lower bound, while a linear embedding gives the finite-action QLB lower bound. Complementing the lower bounds, we give a design-based elimination algorithm for finite-action QLB. When the action set has size operatorname{poly}(d), its regret is linear in d, improving the prior d^2 dependence and matching our lower bound up to polylogarithmic factors. The algorithm couples a low-bias low-variance quantum mean estimator with a small-support G-optimal design through a query allocation matched to the design weights. The design-based elimination reduces the dimension dependence from d^2 to d^{3/2} when using Quantum Monte Carlo estimates. The low-variance estimator then makes reconstruction error aggregate through variance rather than worst-case absolute error, removing the remaining sqrt d factor.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.14319) | 2026-08-17
