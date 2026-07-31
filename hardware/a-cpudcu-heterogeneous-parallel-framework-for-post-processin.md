---
title: "A CPU+DCU Heterogeneous Parallel Framework for Post-Processing Reconstruction in Quantum Circuit Cutting"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.27947"
summary: "arXiv:2607.27947v1 Announce Type: new Abstract: In the NISQ era, limited qubit resources make it difficult to execute large quantum circuits directly on real hardware. Quantum circuit cutting mitigate"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.27947v1 Announce Type: new Abstract: In the NISQ era, limited qubit resources make it difficult to execute large quantum circuits directly on real hardware. Quantum circuit cutting mitigates this limitation by decomposing a large circuit into smaller subcircuits, but it shifts substantial overhead to classical post-processing. As circuit size, complexity, and cut count increase, reconstruction becomes a major computational and storage bottleneck. This paper presents a CPU+DCU heterogeneous parallel framework for circuit-cutting post-processing reconstruction. Instead of constructing a dense 2^n-dimensional probability vector or returning only high-probability states, the framework reconstructs the nonzero-probability states in the original output distribution from subcircuit measurement results. It combines heterogeneous CPU+DCU execution with a high/low-word integer representation for global basis-state indices beyond 64 bits and a three-level cooperative storage mechanism spanning device memory, host memory, and out-of-core storage. Experiments on the Songshan supercomputer show that the framework maintains high reconstruction fidelity while achieving up to 259imes speedup over an optimized serial baseline on linear-cluster states and up to 4imes speedup over a homogeneous CPU-parallel method on random circuits. The framework can also complete reconstruction tasks at the hundred-qubit scale. These results demonstrate that HPC-oriented heterogeneous reconstruction can effectively alleviate the classical post-processing bottleneck and improve reconstruction scalability.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.27947) | 2026-07-31
