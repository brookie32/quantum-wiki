---
title: "Testing and Diagnosing Parameter Miscalibration in Probabilistic Error Cancellation via Direct Fidelity Estimation"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.12802"
summary: "arXiv:2609.12802v1 Announce Type: new Abstract: Probabilistic Error Cancellation (PEC) is a standard technique for mitigating noise in quantum computations, but its unbiasedness relies on accurate kno"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.12802v1 Announce Type: new Abstract: Probabilistic Error Cancellation (PEC) is a standard technique for mitigating noise in quantum computations, but its unbiasedness relies on accurate knowledge of the underlying noise parameters. In practice, these parameters are inferred from experimental data and may be inaccurate. We introduce a protocol that tests PEC parameter consistency on hardware by applying Direct Fidelity Estimation (DFE) to the effective mitigated state. The resulting DFE overlap serves not only as a witness of parameter miscalibration but, under appropriate conditions, also reveals whether the PEC parameters have been overestimated or underestimated. We establish this behavior for arbitrary circuits under global depolarizing noise and for Clifford circuits under general Pauli-stochastic noise. For arbitrary circuits subject to Pauli-stochastic noise, the underestimation result holds generally, while the corresponding overestimation result is established perturbatively for sufficiently small consistent miscalibrations under an additional nondegeneracy condition. We further show that the purity of the effective mitigated operator provides a more general diagnostic, allowing the miscalibration direction to be identified for arbitrary circuits and arbitrary parameter deviations. Finally, we describe a two-copy PEC procedure for measuring this quantity and show that, together with the DFE overlap, it determines the Hilbert-Schmidt distance from the ideal state. The sampling overhead incurred by our protocol is the same as that of PEC, and we discuss strategies to improve it.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.12802) | 2026-09-14
