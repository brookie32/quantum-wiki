---
title: "Fault-tolerant distributed quantum computing with a single nucleus per node"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.24907"
summary: "arXiv:2607.24907v2 Announce Type: replace Abstract: Distributed quantum computing interconnects small, high-quality nodes through optical links, but this architecture carries a pronounced asymmetry: i"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.24907v2 Announce Type: replace Abstract: Distributed quantum computing interconnects small, high-quality nodes through optical links, but this architecture carries a pronounced asymmetry: in-node gates and measurements are cheap and high-fidelity, whereas inter-node communication relies on a low-coherence communication qubit and faulty photonics. Previous approaches overcame the noisy link by placing several high-quality data qubits in each node and consuming them for Bell pair and GHZ state distillation. Here we show that distillation can be avoided altogether. The key observation is that we can engineer a communication error bias, where photonic Bell pairs suffer frequent phase errors but only rare bit-flip errors. We design the syndrome-extraction circuits so that this phase noise appears solely as a measurement error that does not propagate to the data qubits, and is therefore suppressed by simply repeating the measurement; letting the error-correcting code itself, rather than a dedicated distillation subroutine, to purify the link. This dramatically reduces the need for ancillary nuclei: Floquet codes require only a single data qubit per node, while general stabilizer codes require just one additional ancilla. We demonstrate high error-correction thresholds throughout this regime, and we identify lattice surgery as inherently robust for this setting, enabling logical operations at a threshold close to that of quantum memory. As a result, the performance of the quantum computer is limited by the high-quality data qubits, while the requirements on photon indistinguishability and coherence of the communication qubit are substantially relaxed.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.24907) | 2026-07-30
