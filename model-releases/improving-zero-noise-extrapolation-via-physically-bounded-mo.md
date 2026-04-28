---
title: "Improving Zero-Noise Extrapolation via Physically Bounded Models"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24475"
summary: "arXiv:2604.24475v1 Announce Type: new Abstract: Zero-noise extrapolation (ZNE) mitigates errors in near-term quantum devices by extrapolating measurements obtained at amplified noise levels to estimat"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24475v1 Announce Type: new Abstract: Zero-noise extrapolation (ZNE) mitigates errors in near-term quantum devices by extrapolating measurements obtained at amplified noise levels to estimate noise-free expectation values. In practice, commonly used extrapolation models are fitted without enforcing physical constraints, which can yield predictions outside the valid range of quantum observables. In this work, we introduce physically bounded variants of polynomial, exponential, and polynomial--exponential extrapolation models by explicitly parameterizing the zero-noise estimate and constraining it during optimization. We evaluate the approach using a large synthetic benchmark comprising 180,000 circuits and approximately 3.6 million ZNE experiments generated under realistic device noise models derived from IBM quantum backends. We also perform preliminary validation on real quantum hardware using GHZ and W-state circuits. Across the synthetic benchmark, bounded extrapolation substantially reduces unphysical predictions and improves the stability of exponential- and polynomial--exponential-family models, whereas polynomial models show little difference between bounded and unbounded variants. Hardware experiments show similar qualitative behaviour: bounded models generally avoid pathological extrapolations and often provide a more reliable balance between accuracy and usable coverage. At the same time, the results highlight practical limitations of current devices, including stronger-than-expected noise effects and variability not fully captured by simulation models. These results suggest that enforcing physical constraints during extrapolation improves the reliability of ZNE and that this approach can be incorporated into existing workflows with minimal modification.



## Related
- [[gsc-qemit-a-telemetry-driven-hierarchical-forecast-and-bandi|GSC-QEMit: A Telemetry-Driven Hierarchical Forecast-and-Bandit Framework for Adaptive Quantum Error Mitigation]]
- [[local-robust-shadows-on-a-trapped-ion-computer----a-case-stu|Local robust shadows on a trapped ion computer -- a case study]]
- [[calibrating-the-role-of-entanglement-in-variational-quantum-|Calibrating the Role of Entanglement in Variational Quantum Algorithms from a Geometric Perspective]]
- [[from-independent-to-joint-enhancing-quantum-phase-and-correl|From Independent to Joint: Enhancing Quantum Phase and Correlation Factor Estimation by Squeezed Reservoir Engineering]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24475) | 2026-04-28
