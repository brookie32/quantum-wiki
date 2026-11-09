---
title: "Neutral-atom quantum features as complementary structural encodings for graph learning"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08821"
summary: "arXiv:2611.08821v1 Announce Type: new Abstract: Structural descriptors provide graph neural networks (GNNs) with positional and topological inductive biases. However, widely used classical encodings b"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2611.08821v1 Announce Type: new Abstract: Structural descriptors provide graph neural networks (GNNs) with positional and topological inductive biases. However, widely used classical encodings based on random walks or Laplacian spectra emphasize specific structural statistics of a graph, leaving room for alternative descriptors. Neutral-atom quantum processing units (QPUs) can realize graph-dependent Rydberg Hamiltonians, allowing graph topology to be probed through dynamical correlation measurements. In this work, we use these measurements as quantum graph features (QGFs), providing a complementary, hardware-derived family of structural encoding that is not accurately described by classical features derived from Laplacian and adjacency matrices, even when supplemented with an extended set of random-walk, geometric descriptors and classical physical models. By appropriately selecting the quench parameters of the Hamiltonian, we access two characteristic correlation regimes with distinct structural signatures: antiferromagnetic-like and ferromagnetic-like. On an intrinsic information benchmark of 15 topological and spectral probing tasks, quantum and hybrid quantum-classical features match or surpass classical descriptors on local topological properties. When supplied to message-passing, attention, and graph-transformer backbones, hybrid quantum-classical features yield improvements that are within cross-fold noise on most cells but sign-consistent across architectures. When comparing noiseless, shot-sampled emulation-derived quantum features with a neutral-atom QPU implementation, the downstream hybrid results with compressed hardware features match their emulated counterparts within 0.01 F_1 on all backbones. On a synthetic family of ladder graphs, QGFs distinguish two specific classes, outperforming the strongest classical structural descriptors by a margin exceeding cross-fold variability.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08821) | 2026-11-09
