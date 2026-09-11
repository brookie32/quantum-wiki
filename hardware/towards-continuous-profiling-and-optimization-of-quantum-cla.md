---
title: "Towards Continuous Profiling and Optimization of Quantum-Classical Pipelines"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.05814"
summary: "arXiv:2609.05814v2 Announce Type: replace Abstract: Quantum applications increasingly execute as multi-stage quantum-classical pipelines, interleaving QPU computation with classical stages like circui"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.05814v2 Announce Type: replace Abstract: Quantum applications increasingly execute as multi-stage quantum-classical pipelines, interleaving QPU computation with classical stages like circuit generation, transpilation, layout mapping, quantum error mitigation (QEM), and post-processing. These stages have diverse resource requirements and exhibit stochastic behavior under drifting hardware noises, yet existing workflow frameworks treat them as static, isolated components. We present LLQM (Low-Level Quantum Machine), a profiling-driven meta-framework for quantum-classical pipelines. LLQM decomposes pipelines into fine-grained tasks and continuously profiles their CPU/GPU, memory, QPU, and queue dependencies alongside real-time hardware states. This unified runtime abstraction captures cross-stage resource dependencies and reveals how classical and quantum decisions interact, enabling characterization of their impact on fidelity and resource consumption. We evaluate LLQM using QEM as a representative pipeline stage, on IBM 156-qubit Heron r2 processors with circuits up to 100 qubits and 1e7 transpiled gates. Our results show that continuous profiling exposes runtime bottlenecks and enables hardware-, fidelity-, and workload-aware optimizations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.05814) | 2026-09-11
