---
title: "Noise-Directed Adaptive Remapping for Integer Optimization: from qubits to (encoded) qudits"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.28234"
summary: "arXiv:2606.28234v2 Announce Type: replace Abstract: We extend Noise-Directed Adaptive Remapping (NDAR), a recently proposed heuristic meta-algorithm that leverages device noise as a computational reso"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2606.28234v2 Announce Type: replace Abstract: We extend Noise-Directed Adaptive Remapping (NDAR), a recently proposed heuristic meta-algorithm that leverages device noise as a computational resource, to optimization problems over discrete (integer) domains. While originally introduced for unconstrained binary optimization, the proposed generalization introduces additional gauge degrees of freedom at the logical level, such that the gauge transformation applied at each iteration is no longer unique, allowing tailoring to particular encodings or quantum hardware. We identify encoding-dependent requirements for NDAR beyond binary domains: feasibility of the noise attractor, existence of compatible gauge transformations that preserve an efficiently implementable circuit family, and a systematic way to select the transform to apply at each step. We analyze these criteria for qudit-native and for binary, one-hot, and domain-wall qubit encodings, using the Max-k-colorable subgraph problem as a running example. We demonstrate that these encodings can exhibit distinct advantages and tradeoffs when integrated within the NDAR framework, particularly in how noise-induced dynamics interact with the solution landscape and choice of encoding. Our results indicate that NDAR-guided noise considerations provide a new criterion for comparing device-level encoding choices for quantum optimization. Finally, we outline directions toward experimental realization in superconducting qudit devices and further algorithmic improvements.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.28234) | 2026-08-04
