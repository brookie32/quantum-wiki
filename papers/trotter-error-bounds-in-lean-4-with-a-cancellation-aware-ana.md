---
title: "Trotter Error Bounds in Lean 4 with a Cancellation-Aware Analysis of the Fourth-Order Suzuki Formula"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.27359"
summary: "arXiv:2611.27359v1 Announce Type: new Abstract: We formalize the commutator-scaling bound of Childs et al. in Lean 4. For skew-adjoint generators, the local order condition gives an explicit integer s"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.27359v1 Announce Type: new Abstract: We formalize the commutator-scaling bound of Childs et al. in Lean 4. For skew-adjoint generators, the local order condition gives an explicit integer step count sufficient to meet a prescribed error tolerance. We apply the theorem in Lean to the binary fourth-order Suzuki formula. For this formula we can also account for cancellation within and between steps. Using local remainder estimates of Casas and Murua, we sum the signed quintic and centered seventh-degree error terms after conjugating each to the interaction picture. For every positive integer step count, we bound the difference between this sum and the global error operator. At fixed time the explicit remainder is eighth order in the step size, and the integral of the conjugated quintic term gives the exact leading error coefficient. The Lean proofs cover the two-generator finite-sum estimates, including the spectral norm for complex matrices. On five ten-site nearest-neighbor Heisenberg instances at time 10 and tolerance 10^{-3}, the transported sum meets the tolerance at a mean of 129.4 steps. Taking a separate norm at each step with the same polynomial and remainder gives a mean first crossing between 184.6 and 185.2 steps. The accumulated Casas--Murua local bound at q=8 gives a mean of 184.8 steps.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.27359) | 2026-11-23
