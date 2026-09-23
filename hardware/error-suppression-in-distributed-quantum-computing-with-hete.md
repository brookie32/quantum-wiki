---
title: "Error Suppression in Distributed Quantum Computing with Heterogeneous-Distance Lattice Surgery"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.26784"
summary: "arXiv:2609.26784v1 Announce Type: new Abstract: Distributed quantum computing requires fault-tolerant operations across inter-QPU links that can be substantially noisier than local gates. Uniformly in"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.26784v1 Announce Type: new Abstract: Distributed quantum computing requires fault-tolerant operations across inter-QPU links that can be substantially noisier than local gates. Uniformly increasing code distance provides additional protection but also enlarges data patches used for local storage and computation. Here, we introduce distributed heterogeneous-distance lattice surgery using an eight-data-patch ancilla-mediated (8-DAM) architecture, which will be useful for near-term quantum devices with less qubit overhead. In this architecture, the central ancilla spanning the inter-QPU boundary is enlarged while the data patches retain distance d. The protocol uses traveling stabilizers to suppress hook errors during merge and split operations between these unequal-distance patches. Circuit-level simulations of rotated surface codes at fixed local depolarizing noise show that logical-readout error rates depend only weakly on link noise. The resulting advantage over conventional lattice surgery grows as link errors increase. Comparisons with uniform distance implementations demonstrate comparable logical error suppression with reduced physical-qubit overhead. We also demonstrate how 8-DAM layouts support two simultaneous distributed logical CNOT operations between four logical data qubits using a single enlarged ancilla. At higher link noise, this construction yields lower logical error rates and more stability than two independent distributed logical CNOTs. These results support selective ancilla enlargement as a resource-efficient approach to fault-tolerant distributed quantum computing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.26784) | 2026-09-23
