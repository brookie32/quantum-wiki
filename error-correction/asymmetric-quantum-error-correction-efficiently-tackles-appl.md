---
title: "Asymmetric quantum error correction efficiently tackles application-specific noise effects"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.07235"
summary: "arXiv:2609.07235v2 Announce Type: replace Abstract: Noise is a major challenge for current quantum computers. It can be broadly categorized into bit-flip and phase-flip errors. These two types do not "
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2609.07235v2 Announce Type: replace Abstract: Noise is a major challenge for current quantum computers. It can be broadly categorized into bit-flip and phase-flip errors. These two types do not necessarily affect the executed algorithm, thus also the application, in the same way. We illustrate this general effect for the example of the quantum approximate optimization algorithm (QAOA) applied to a small instance of the flight-gate assignment (FGA) problem. We compare bit-flip and phase-flip Pauli noise under both layer-level and gate-level noise models, using two circuit decompositions of the same ideal QAOA unitary: a CNOT-based decomposition and a native-RZZ decomposition. For the six-qubit FGA instance considered here, bit-flip noise produces a larger degradation in the optimized QAOA performance across the investigated circuit depths and noise models. The asymmetry is most pronounced in the layer-level and native-RZZ simulations. We explain this behavior through the commutation and propagation properties of the errors and their effects on the final computational-basis measurements. Since these mechanisms are not specific to the considered FGA instance, we expect similar noise asymmetries to arise in other Ising-based QAOA applications, although this remains to be investigated. We then exploit these insights to tackle noise particularly efficiently using asymmetric error-correcting codes. As an illustration, we use the quantum parity code (QPC), a generalization of the 9-qubit Shor code, and show that a smaller asymmetric code can achieve nearly the same improvement as a larger symmetric choice. This suggests that allocating error-correction resources according to algorithmic noise sensitivity, rather than physical error rates alone, can be beneficial even when the physical noise is symmetric. Finally, we discuss how information about the noise obtained through calibration can be exploited in our approach.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.07235) | 2026-11-11
