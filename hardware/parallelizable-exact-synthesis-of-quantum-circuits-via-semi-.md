---
title: "Parallelizable Exact Synthesis of Quantum Circuits via Semi-Tensor Product"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.24195"
summary: "arXiv:2607.24195v2 Announce Type: replace Abstract: Exact synthesis is a key infrastructure in quantum circuit synthesis and optimization, which provides optimal implementations of small circuit shard"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2607.24195v2 Announce Type: replace Abstract: Exact synthesis is a key infrastructure in quantum circuit synthesis and optimization, which provides optimal implementations of small circuit shards and is widely used as a circuit re-synthesis optimization kernel. However, existing quantum exact synthesis methods suffer from encoding overhead, memory bottlenecks, and poor parallel scalability. In this work, we introduce a parallel exact synthesis framework for CNOT and phase polynomial circuits based on the semi-tensor product (STP) theory of matrices that avoids these issues. The algorithm contains two stages: it first enumerates candidate circuit topologies, and then instantiates each topology by determining the control and target qubit of its partial gates via a STP-based circuit solver. In the second stage, circuit topologies are encoded as canonical STP expressions, and the CNOT gates are synthesized through right-to-left STP matrix factorization that progressively eliminates infeasible gate decisions. In the framework, topology enumeration and the subsequent solving process are independent across different topologies, and can be naturally parallelized. Despite the NP-hardness of the problem, our algorithm yields up to 12.8imes parallel speedup with 32 workers, whereas the parallel speedups of existing SAT-based methods remain below 5imes with the same worker budget. On randomly generated synthesis targets, the proposed algorithm is typically 100-1000imes faster than the SAT-based approach on small and moderately difficult instances, and remains competitive for more difficult instances. When integrated in a real-world circuit optimization workflow, our algorithm achieves a median speedup of 3.41imes on the QASMBench benchmark.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.24195) | 2026-08-18
