---
title: "Hybrid Quantum-Classical Optimization Workflows for the Shipment Selection Problem"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.11758"
summary: "arXiv:2604.11758v3 Announce Type: replace Abstract: We present a quantum optimization framework for the Shipment Selection Problem (SSP) in electric freight logistics, developed jointly by IonQ and Ei"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2604.11758v3 Announce Type: replace Abstract: We present a quantum optimization framework for the Shipment Selection Problem (SSP) in electric freight logistics, developed jointly by IonQ and Einride. Idle gaps arising from stochastic shipment cancellations reduce fleet utilization and revenue; filling them optimally requires solving a combinatorial assignment problem with quadratic inter-gap dependencies. We formulate the SSP as a Mixed-Integer Quadratic Program, map it to an Ising cost Hamiltonian, and solve it using Iterative-QAOA, a non-variational warm-start extension of the Quantum Approximate Optimization Algorithm (QAOA) with a fixed linear-ramp parameter schedule. An end-to-end hybrid workflow integrates Einride's vehicle routing problem (VRP) solver with IonQ's quantum simulations, enabling evaluation on real, anonymized logistics data spanning up to 130 qubits. We assess solution quality through application-level performance metrics, including Shipments Delivered (SD), Schedule Compatibility Score (SCS), and Total Drive Distance (TDD). When the quantum assignment is passed to the classical solver as a warm start, the resulting hybrid workflow achieves improvements of up to 12% in SD and a reduction of up to 6% in total drive distance per shipment for specific instances, while total operational cost remains effectively unchanged. For the subset of instances within reach of current devices (20-35 qubits), the workflow is additionally executed on IonQ trapped-ion quantum hardware, where the hardware results closely reproduce the noiseless simulations. These results show that Iterative-QAOA can generate compatibility-aware assignments that become operationally valuable when embedded in a hybrid logistics optimization workflow.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.11758) | 2026-08-21
