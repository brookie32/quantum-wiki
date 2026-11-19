---
title: "xTBloom: GPU Batching for High-Throughput GFN-xTB Calculations"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.24807"
summary: "arXiv:2611.24807v1 Announce Type: new Abstract: Conformational searches and multiwindow free-energy sampling require large numbers of GFN-xTB energy and force evaluations across molecular conformation"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24807v1 Announce Type: new Abstract: Conformational searches and multiwindow free-energy sampling require large numbers of GFN-xTB energy and force evaluations across molecular conformations and sampling windows. Processing each system separately on a GPU makes it difficult to amortize memory management, host-device data transfer, and kernel-launch overhead. Here, we present xTBloom, a GPU batching library for GFN-xTB energy and force evaluations. xTBloom sorts evaluation queues by atomic orbital (AO) count before forming batches, accommodates size differences through a native ragged layout, maintains independent self-consistent charge (SCC) and failure states for each system, and selects execution paths according to data residency. We focus the quantitative evaluation on GFN2-xTB through cross-program comparisons on QM9 and OMol25, CPU-CUDA comparisons, finite-difference force checks, and controlled failure tests. On a near-size OMol25 workload, GPU execution achieved a 2.9-fold speedup over xTBloom's single-core CPU backend. A companion LAMMPS plugin integrates cross-window batching with periodic quantum mechanical/molecular mechanical (QM/MM) simulation. In a short synchronized test with 48 windows on one GPU, the complete coupled workflow achieved an aggregate speedup of approximately 14 over sequential execution of the same windows. These results demonstrate the throughput benefits of batched GFN-xTB evaluation for repeated electronic-structure calculations and multiwindow sampling.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.24807) | 2026-11-19
