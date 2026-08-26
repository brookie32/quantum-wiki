---
title: "End-to-end performance of quantum-accelerated large-scale linear algebra workflows"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.15515"
summary: "arXiv:2603.15515v4 Announce Type: replace Abstract: Solving large-scale sparse linear systems is a challenging computational task due to the introduction of non-zero elements, or 'fill-in'. The Graph "
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2603.15515v4 Announce Type: replace Abstract: Solving large-scale sparse linear systems is a challenging computational task due to the introduction of non-zero elements, or "fill-in". The Graph Partitioning Problem (GPP) arises naturally when minimizing fill-in and accelerating solvers. In this paper, we measure the end-to-end performance of a hybrid quantum-classical framework designed to accelerate Finite Element Analysis (FEA) by integrating a quantum solver for GPP into Synopsys/Ansys' LS-DYNA multiphysics simulation software. The quantum solver we use is based on Iterative-QAOA, a scalable, non-variational quantum approach for optimization. We focus on two specific classes of FEA problems, namely vibrational (eigenmode) analysis and transient simulation. We report numerical simulations on up to 150 qubits done on NVIDIA's CUDA-Q/cuTensorNet and implementation on IonQ's Forte quantum hardware. The potential impact on LS-DYNA workflows is quantified by measuring the wall-clock time-to-solution for complex problem instances, including vibrational analysis of large finite element models of a sedan car and a Rolls-Royce jet engine, as well as transient simulations of a drill and an impeller. We performed end-to-end performance measurements on meshes comprising up to 35 million elements. Measurements were conducted using LS-DYNA in distributed-memory mode via Message Passing Interface (MPI) on AWS and Synopsys compute clusters. Our findings indicate that with a quantum computer in the loop, amortized LS-DYNA wall-clock time can be improved by up to 14.6% for specific cases and by at least 5.9% for all models considered. These results highlight the significant potential of quantum computing to reduce time-to-solution for large-scale FEA simulations within the Noisy Intermediate-Scale Quantum (NISQ) era, offering an approach that is scalable and extendable into the fault-tolerant quantum computing regime.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.15515) | 2026-08-26
