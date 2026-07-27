---
title: "Exact Neural-Network Representations of the Motzkin States"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.22522"
summary: "arXiv:2607.22522v1 Announce Type: cross Abstract: Motzkin spin chains are paradigmatic frustration-free one-dimensional quantum systems whose ground states feature exactly solvable combinatorial struc"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.22522v1 Announce Type: cross Abstract: Motzkin spin chains are paradigmatic frustration-free one-dimensional quantum systems whose ground states feature exactly solvable combinatorial structures and exotic, area-law-violating entanglement scaling. Specifically, colorless Motzkin states exhibit critical logarithmic entanglement divergence (log N) with system size (N), while their colorful counterparts host supercritical sublinear (sqrt{N}) entanglement growth. Such unconventional entanglement behaviors place these states well beyond the expressive capability of standard matrix product states, which are fundamentally constrained by the entanglement area law. Here, we systematically construct exact, training-free neural-network representations for both colorless and colorful Motzkin states across four mainstream architectures, including recurrent, feedforward, convolutional, and transformer networks. Our core design leverages a causal prefix-sum module, implementable via recurrent updates, feedforward mappings, or masked attention layers, combined with position-selective rectified linear gates that enforce the Motzkin height constraints. For the colorful states, we further introduce a dedicated causal stack module that explicitly encodes the last-in-first-out color-matching rule. Our results demonstrate that neural architectures can accurately capture highly non-trivial entanglement features inaccessible to conventional tensor networks, providing prototypic examples for benchmarking and a constructive design framework for future neural-network quantum state developments targeting strongly entangled quantum systems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.22522) | 2026-07-27
