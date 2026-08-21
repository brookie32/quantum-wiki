---
title: "Shadow models of a quantum model for cloud cover and the influence of finite sampling noise"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.20076"
summary: "arXiv:2608.20076v1 Announce Type: new Abstract: Quantum computing is a quickly growing field that is promising various advantages compared to conventional computing. However, currently stand-alone qua"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.20076v1 Announce Type: new Abstract: Quantum computing is a quickly growing field that is promising various advantages compared to conventional computing. However, currently stand-alone quantum applications are scarce and hybrid (quantum-classical) computing is needed, especially in quantum machine learning (QML). Due to current limitations of quantum computing hardware and the coupling between HPC and quantum devices, integrating a trained (QML) model in classical applications is challenging. In this case, it is helpful to couple so-called shadows of the QML model instead, i.e., classical models that imitate the input-output relations of QML models such that quantum resources are only needed during the training stage. Here we consider constructive shadowing processes without an explicit training or regression stage to avoid rendering the QML model redundant, and apply them to a previously developed QML model for cloud cover [1] to allow for an efficient coupling to a climate model. We compare classical interpolation methods to an approximation of the quantum Fourier model, the representation of the circuit as a partial Fourier series. The encoding strategy in [1] allows the use of the discrete Fourier transform to efficiently reconstruct the circuits classically. Truncating the partial Fourier series further reduces the size of the shadow models. Both methods have the effect of mitigating finite sampling noise under certain conditions, which yields a motivation to use shadow models also beyond the era of limited hardware availability. Further, we compute the shadow models on the quantum system Euro-Q-Exa, based on the IQM Radiance system with superconducting qubits, where error mitigating effects can also be observed, albeit it is still difficult to distinguish them from errors connected to the calibration of the system.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.20076) | 2026-08-21
