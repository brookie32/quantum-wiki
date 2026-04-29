---
title: "Sample- and Hardware-Efficient Fidelity Estimation by Stripping Phase-Dominated Magic"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.09710"
summary: "arXiv:2602.09710v2 Announce Type: replace Abstract: Direct fidelity estimation (DFE) is a famous tool for estimating the fidelity with a target pure state. However, such a method generally requires ex"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2602.09710v2 Announce Type: replace Abstract: Direct fidelity estimation (DFE) is a famous tool for estimating the fidelity with a target pure state. However, such a method generally requires exponentially many sampling copies due to the large magic of the target state. This work proposes a sample- and gate-efficient fidelity estimation algorithm that is affordable within feasible quantum devices. We show that the fidelity estimation with pure states close to the structure of phase states, for which sample-efficient DFE is limited by their strong entanglement and magic, can be done by using O({rm poly}(n)) sampling copies, with a single n-qubit fan-out gate. As the target state becomes a phase state, the sampling complexity reaches O(1). Such a drastic improvement stems from a crucial step in our scheme, the so-called phase stripping, which can significantly reduce the target-state magic. Furthermore, we convert a complex diagonal gate resource, which is needed to design a phase-stripping-adapted algorithm, into nonlinear classical post-processing of Pauli measurements so that we only require a single fan-out gate. Additionally, as another variant using the nonlinear post-processing, we propose a nonlinear extension of the conventional DFE scheme. Here, the sampling reduction compared to DFE is also guaranteed, while preserving the Pauli measurement as the only circuit resource. We expect our work to contribute to establishing noise-resilient quantum algorithms by enabling a significant reduction in sampling overhead for fidelity estimation under the restricted gate resources, and ultimately to clarifying a fundamental gap between the resource overhead required to understand complex physical properties and that required to generate them.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.09710) | 2026-04-29
