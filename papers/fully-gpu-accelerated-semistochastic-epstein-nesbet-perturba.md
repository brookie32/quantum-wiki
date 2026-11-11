---
title: "Fully GPU-accelerated semistochastic Epstein-Nesbet perturbation theory"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13522"
summary: "arXiv:2611.13522v1 Announce Type: cross Abstract: Second-order Epstein-Nesbet perturbation theory (EN-PT2) is an important tool for improving selected configuration interaction (SCI) energies, but the"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13522v1 Announce Type: cross Abstract: Second-order Epstein-Nesbet perturbation theory (EN-PT2) is an important tool for improving selected configuration interaction (SCI) energies, but the large external determinant space creates substantial memory and communication costs on GPU clusters. We develop a fully GPU-accelerated implementation of distributed semistochastic EN-PT2, fusing excitation generation, screening, and PT2 weighting in a single kernel traversal. Fixed-size random-phase CountSketch arrays limit memory use and replace large external determinant exchange with bounded collective summation. The implementation on one A100 completes EN-PT2 calculations 8.21-37.53 times faster than Arrow on 64 CPU cores at the same requested statistical standard error, and fixed-workload strong-scaling tests achieve 93.5% parallel efficiency on 16 GPUs across two nodes. Applications to an iron-oxo complex in a (60e, 187o) active space, iron-porphyrin references containing 200 million determinants per state, and neural-network quantum states establish the method's efficiency for perturbative corrections to large reference wave functions in the GPU era.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13522) | 2026-11-11
