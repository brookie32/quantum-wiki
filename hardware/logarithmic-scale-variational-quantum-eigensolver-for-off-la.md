---
title: "Logarithmic-scale variational quantum eigensolver for off-lattice protein structure prediction in continuous torsional angle space"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.02113"
summary: "arXiv:2609.02113v1 Announce Type: new Abstract: Classical and current quantum approaches to protein structure prediction (QPSP) face limitations, notably massive qubit requirements restricting near-te"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02113v1 Announce Type: new Abstract: Classical and current quantum approaches to protein structure prediction (QPSP) face limitations, notably massive qubit requirements restricting near-term models to simplistic on-lattice simulations. We propose a logarithmic-scale variational quantum eigensolver (VQE) that reduces qubit requirements for N torsional degrees of freedom to O(log2N), enabling off-lattice, all-atom simulations. Our architecture extracts molecular torsions from relative phases in statevector simulations. On quantum hardware, a decoder maps the empirical cumulative distribution function (CDF) from basis-state probabilities to bounded torsional variables. These feed a classical algorithm to build heavy-atom coordinates. We use an EfficientSU2 ansatz and multi-stage relaxation to mitigate barren plateaus. Structures are evaluated via a custom hybrid quantum-classical Hamiltonian, alongside Rosetta and OpenMM benchmarks. Evaluation on chignolin and Trp-cage yielded native-like conformations. Chignolin reached a 0.623 {AA} C{alpha} RMSD in retained snapshots and 1.199 {AA} in final models; Trp-cage achieved a 2.501 {AA} RMSD among snapshots (3.512 {AA} in final models). Execution on IBM processors (ibm_cleveland, ibm_miami) successfully recovered native-like structures with a best RMSD of 1.758 {AA}. The custom energy function performed best overall, though energy-ranking imbalances persisted across sampled landscapes for all functions. This introduces the first all-atom, continuous-space quantum algorithm for QPSP. By converting physical qubit constraints into circuit depth constraints, it proves high-resolution prediction is feasible with exponentially fewer qubits. Despite current limits like computational overhead and energy function sensitivity, it establishes a scalable foundation for hybrid quantum biophysics.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.02113) | 2026-09-03
