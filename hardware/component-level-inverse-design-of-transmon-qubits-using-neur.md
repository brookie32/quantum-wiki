---
title: "Component-Level Inverse Design of Transmon Qubits Using Neural Networks"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.20795"
summary: "arXiv:2607.20795v1 Announce Type: new Abstract: Designing a superconducting qubit to realize specific Hamiltonian parameters typically requires iterating through a time and compute-intensive forward l"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.20795v1 Announce Type: new Abstract: Designing a superconducting qubit to realize specific Hamiltonian parameters typically requires iterating through a time and compute-intensive forward loop in which the designer chooses a layout geometry, simulates it, extracts circuit parameters such as capacitances, and refines the geometry. We study the inverse version of this task using a neural-network workflow that maps target Hamiltonian parameters directly to component-level layout parameters, which we subsequently demonstrate on a planar transmon layout. During training, we pair the inverse model with a frozen forward surrogate model and evaluate the loss in Hamiltonian space rather than in layout-parameter space. In validation against a conventional EM solver, 97% of generated designs produce usable geometries, and the inverse-plus-surrogate pipeline reaches mean percent errors of 0.73% for qubit frequency and 1.58% for anharmonicity, comparable to or below the fabrication and simulation-to-measurement uncertainty expected for academic-process transmon devices of this type. A single pipeline query takes approximately 56 ms on CPU, versus approximately 2 min for a conventional EM capacitance extraction on the same hardware, a speedup of more than 2,100 times. Batching minimizes the AI model inference overhead, reducing the runtime to 0.24 ms per sample on CPU and 2.5 microseconds per sample on GPU, resulting in speedups of 5.0 x 10^5 and 4.8 x 10^7, respectively, relative to a single conventional CPU EM extraction. Our results indicate that component-level inverse design usefully extends and complements conventional EM simulation, including for small datasets on the order of 1,000 samples.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.20795) | 2026-07-24
