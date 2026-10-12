---
title: "Lie Algebra-Based Quantum Optimal Controls Interpolation"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.02014"
summary: "arXiv:2606.02014v2 Announce Type: replace Abstract: We present a framework combining Lie group theory and feed-forward neural networks to efficiently generate quantum optimal control pulses for arbitr"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2606.02014v2 Announce Type: replace Abstract: We present a framework combining Lie group theory and feed-forward neural networks to efficiently generate quantum optimal control pulses for arbitrary unitary operations in superconducting qubit systems, bypassing the need for explicit optimization at inference time. The exponential scaling of the Hilbert space dimension with qubit number makes standard optimization approaches computationally prohibitive when large ensembles of distinct propagators must be processed, a bottleneck that is particularly acute in Trotterized quantum simulation. Our method addresses this limitation by pre-computing a representative set of control pulses via Lie group theory and training neural networks to map target propagators to their corresponding pulses. We demonstrate the approach on superconducting qubit systems of 2, 3, and 4 qubits, finding high reconstruction fidelity for specific combinations of Lie algebra parameters. As a physically motivated benchmark, we apply the methodology to reconstruct control pulses for the Trotter propagators of a neutrino system undergoing collective flavor oscillations. The successful generalization across system types demonstrates that a single model -- trained once on hardware-specific random propagators -- can serve as a universal control-pulse generator for any target quantum system of compatible Hilbert space dimension, offering a promising route toward scalable quantum simulation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.02014) | 2026-10-12
