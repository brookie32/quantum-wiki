---
title: "Reducing the Cost of Qudit State Preparation by Learning a Sparse Structure for SNAP Gates"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.21557"
summary: "arXiv:2610.21557v1 Announce Type: new Abstract: Preparing quantum states in bosonic qudits with SNAP--Displacement sequences requires both optimizing the gate parameters and deciding which Fock levels"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.21557v1 Announce Type: new Abstract: Preparing quantum states in bosonic qudits with SNAP--Displacement sequences requires both optimizing the gate parameters and deciding which Fock levels should be controlled by each SNAP gate. A fully parameterized ansatz assigns an independent phase to every Fock level in every gate, leading to a number of phases that grows steeply. This constitutes a problem for short to medium term systems as controlling many phases requires complex control pulses which are subject to increased control errors. Previous work reduced this cost by restricting the trainable phases to predefined sparse patterns, such as a diagonal or a grid, which however may not be optimal for a specific target state. In this work, we address this limitation by introducing a method that learns which phases are needed together with their values, using a differentiable mask. A sparsity penalty encourages the removal of unnecessary phases, while temperature annealing gradually turns the masks into binary decisions. We compare the proposed method with fully parameterized and predefined sparse ansatzes on Fourier and Haar-random target states. The evaluation considers both the minimum number of phases required to reach different infidelity thresholds and the overall trade-off between fidelity and phases required, measured through Pareto frontiers and hypervolume. The results show that learning the location of the phases together with their values provides competitive or improved fidelity--resource trade-offs, although the advantage depends on the target state and qudit dimension.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.21557) | 2026-10-16
