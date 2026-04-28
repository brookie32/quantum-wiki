---
title: "GSC-QEMit: A Telemetry-Driven Hierarchical Forecast-and-Bandit Framework for Adaptive Quantum Error Mitigation"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24551"
summary: "arXiv:2604.24551v1 Announce Type: new Abstract: Quantum error mitigation (QEM) is essential for extracting reliable results from near-term quantum devices, yet practical deployments must balance mitig"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24551v1 Announce Type: new Abstract: Quantum error mitigation (QEM) is essential for extracting reliable results from near-term quantum devices, yet practical deployments must balance mitigation strength against runtime overhead under time-varying noise. We introduce GSC-QEMit, a telemetry-driven, extbf{context--forecast--bandit} framework for adaptive mitigation that switches between lightweight suppression and heavier intervention as drift evolves. GSC-QEMit composes three coupled modules: (G) a Growing Hierarchical Self-Organizing Map (GHSOM) that clusters streaming telemetry into operating contexts; (S) an uncertainty-aware subsampled Gaussian-process forecaster that predicts short-horizon fidelity degradation; and (C) a cost-aware contextual multi-armed bandit (CMAB) that selects mitigation actions via Thompson sampling with explicit intervention cost. We evaluate GSC-QEMit on benchmark circuit families (GHZ, Quantum Fourier Transform, and Grover search) under nonstationary noise regimes simulated in Qiskit Aer, using an instrumented testbed where action labels correspond to graded mitigation intensity. Across Clifford, non-Clifford, and structured workloads, GSC-QEMit improves average logical fidelity by extbf{+9.0%} relative to unmitigated execution while reducing unnecessary heavy interventions by reserving them for inferred noise spikes. The resulting policies exhibit a favorable fidelity--cost trade-off and transfer across the evaluated workloads without circuit-specific tuning.



## Related
- [[improving-zero-noise-extrapolation-via-physically-bounded-mo|Improving Zero-Noise Extrapolation via Physically Bounded Models]]
- [[autoqresearch-llm-guided-closed-loop-policy-search-for-adapt|AutoQResearch: LLM-Guided Closed-Loop Policy Search for Adaptive Variational Quantum Optimization]]
- [[calibrating-the-role-of-entanglement-in-variational-quantum-|Calibrating the Role of Entanglement in Variational Quantum Algorithms from a Geometric Perspective]]
- [[architecture-aware-unitary-synthesis|Architecture-aware Unitary Synthesis]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24551) | 2026-04-28
