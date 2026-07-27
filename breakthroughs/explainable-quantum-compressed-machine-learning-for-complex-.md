---
title: "Explainable quantum-compressed machine learning for complex fluid flows"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.21688"
summary: "arXiv:2607.21688v1 Announce Type: cross Abstract: Machine-learning surrogates of physical systems face a paradox: explainable models facing the challenge of expressivity to capture complex nonlinear f"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.21688v1 Announce Type: cross Abstract: Machine-learning surrogates of physical systems face a paradox: explainable models facing the challenge of expressivity to capture complex nonlinear flows, whereas expressive deep surrogates match high-fidelity simulations only through massive parameterisations that turn the learned dynamics into a black box. Here, we introduce quantum-compressed machine learning (QCML), which resolves this tension by compressing the latent propagator of a flow surrogate from 524{,}288 trainable parameters to no more than 8. This parameter reduction brings the learned dynamical law to the parameter scale of a physical constitutive relation rather than a black-box neural network, making the surrogate directly interpretable and controllable without sacrificing expressivity. The compression is realised by a structured quantum circuit whose unitary propagator constrains the latent spectrum to the unit circle exactly and by construction, replacing exponential error growth with linear accumulation over autoregressive rollouts. Classical regularisation only approximates this constraint: even a quantum-inspired classical baseline penalised towards unitarity collapses within one Lyapunov time on turbulent channel flow, whereas QCML remains stable over the full rollout. Shared phase and coupling angles parameterising the circuit correspond directly to modal frequencies and inter-mode interactions, giving the learned dynamics a physical interpretation in spectral space. On two patient-specific cardiovascular benchmarks, the structured QCML propagator matches the predictive accuracy of its classical counterpart on surface pressure spectra, pressure drop, and wall shear stress. These results establish QCML as a working component of scientific machine learning and a concrete contribution towards practical quantum advantage in real-world prediction.



## Related
- [[quantum-reservoir-computing-recent-advances-and-future-direc|Quantum Reservoir Computing: Recent Advances and Future Directions]]
- [[local-tensor-train-surrogates-for-quantum-learning-models|Local tensor-train surrogates for quantum learning models]]
- [[iterative-quantum-feature-maps|Iterative Quantum Feature Maps]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.21688) | 2026-07-27
