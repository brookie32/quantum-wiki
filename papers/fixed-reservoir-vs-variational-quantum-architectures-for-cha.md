---
title: "Fixed-Reservoir vs Variational Quantum Architectures for Chaotic Dynamics: Benchmarking QRC and QPINN on the Lorenz System"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.23743"
summary: "arXiv:2604.23743v1 Announce Type: new Abstract: Deploying quantum machine learning on NISQ devices requires architectures where training overhead does not negate computational advantages. We systemati"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.23743v1 Announce Type: new Abstract: Deploying quantum machine learning on NISQ devices requires architectures where training overhead does not negate computational advantages. We systematically compare two quantum approaches for chaotic time-series prediction on the Lorenz system: a variational Quantum Physics-Informed Neural Network (QPINN) and a Quantum Reservoir Computing (QRC) framework utilizing a fixed transverse-field Ising Hamiltonian. Under matched resources (4--5 qubits, 2--3 layers), QRC achieves an 81% lower mean-squared error (test MSE 3.2 pm 0.6 vs. 47.9 pm 36.6 for QPINN) while training sim 52,000imes faster (0.2,s vs. sim 2.4,h per seed). Drawing on the classical delay-embedding principle, we formalize a temporal windowing technique within the QRC pipeline that improves attractor reconstruction by providing bounded, structured input history. Analysis reveals that QPINN instability stems from capacity limitations and competing loss terms rather than barren plateaus; gradient norms remained large (10^3--10^4), ruling out exponential suppression at this scale. These failure modes are absent by construction in the non-variational QRC approach. We validate robustness across three canonical systems (Lorenz, Rossler, and Lorenz-96), where QRC consistently achieves low test MSE (3.1 pm 0.6, 1.8 pm 0.1, and 12.4 pm 0.6, respectively) with sub-second training. Our findings suggest the fixed-reservoir architecture is a primary driver of QRC's advantage at these scales, warranting further investigation at larger qubit counts and on hardware where quantum-specific advantages are expected to emerge.



## Related
- [[few-shot-cross-device-transfer-for-quantum-noise-modeling-on|Few-Shot Cross-Device Transfer for Quantum Noise Modeling on Real Hardware]]
- [[encoding-strategies-for-quantum-enhanced-fluid-simulations-o|Encoding strategies for quantum enhanced fluid simulations: opportunities and challenges]]
- [[diffqec-a-versatile-diffusion-model-for-quantum-error-correc|DiffQEC: A versatile diffusion model for quantum error correction]]
- [[quantum-chaotic-systems-a-random-matrix-approach|Quantum chaotic systems: a random-matrix approach]]
- [[quantum-circuit-cutting-complexity-and-optimization|Quantum Circuit Cutting: Complexity and Optimization]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.23743) | 2026-04-28
