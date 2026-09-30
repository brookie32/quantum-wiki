---
title: "Matrix-product-state-assisted variational Gibbs-state preparation"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.23546"
summary: "arXiv:2510.23546v3 Announce Type: replace Abstract: Evaluating the von Neumann entropy is a central challenge in variational Gibbs-state preparation. We introduce and benchmark matrix-product-state (M"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2510.23546v3 Announce Type: replace Abstract: Evaluating the von Neumann entropy is a central challenge in variational Gibbs-state preparation. We introduce and benchmark matrix-product-state (MPS) assistance for classically evaluating and optimizing the purification circuits without full-statevector storage, examining how circuit architecture affects both thermal-state accuracy and the computational resources required. Comparisons on four- and six-spin transverse-field Ising and XXZ chains reveal complementary strengths: a thermofield-double ansatz performs better at high temperature, whereas a contiguous hardware-efficient ansatz (HEA) performs better on cooling. We identify a layer-dependent entropy ceiling in the contiguous HEA and compare it with an interleaved architecture whose entropy capacity is set solely by the ancilla qubit count. MPS-based benchmarks on 10 x 1, 20 x 1, 3 x 3, and 4 x 4 transverse-field Ising systems show that the tested interleaved circuits generally lower the free-energy errors and improve thermal observables. However, greater entropy capacity and lower free energy do not guarantee improvement in every observable. The architectures also differ in classical cost: contiguous registers permit entropy evaluation at a single MPS bond, whereas the interleaved arrangement requires a dense entropy calculation that scales exponentially with the number of ancillas. These benchmarks connect the accuracy of MPS-assisted Gibbs-state preparation to circuit capacity, optimization, and the tractability of energy and entropy evaluation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.23546) | 2026-09-30
