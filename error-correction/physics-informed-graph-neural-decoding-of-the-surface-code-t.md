---
title: "Physics-Informed Graph-Neural Decoding of the Surface Code: the Logical Signal as an Exact Topological Pairing"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.20060"
summary: "arXiv:2607.20060v2 Announce Type: replace Abstract: We develop a physics-informed graph neural network (GNN) decoder for the surface code that solves a discrete Poisson equation on the syndrome graph,"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.20060v2 Announce Type: replace Abstract: We develop a physics-informed graph neural network (GNN) decoder for the surface code that solves a discrete Poisson equation on the syndrome graph, with the syndrome as the charge source. We compare four readout architectures for extracting the logical-error probability: a potential-based readout that maps the Poisson field through a multilayer perceptron, two current-based readouts under single- and two-sink Dirichlet boundary conditions, and a diffusion-based variant. Comparing these, we show that the solver's edge current is a pure gradient flow whose harmonic (circulating) part vanishes identically. The logical signal therefore cannot be read as a component of the current itself; it is instead a topological pairing between the syndrome and a boundary-fixed harmonic coordinate that distinguishes the two code boundaries linked by the logical operator. We prove that this pairing is evaluated exactly and in closed form, with no learned readout parameters, as the net current drained between the two boundary sinks. On the rotated surface code under circuit-level depolarising noise, this single closed-form scalar matches the best full-field readout and, at larger code distance, significantly exceeds the single-sink current pool, so that isolating the pairing helps more, not less, as the field grows larger and sparser. The decoder is not intended to surpass minimum-weight perfect matching, near-optimal for this noise model; its contribution is an interpretable characterisation of the logical signal itself.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.20060) | 2026-07-30
