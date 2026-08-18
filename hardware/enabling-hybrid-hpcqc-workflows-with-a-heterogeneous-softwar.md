---
title: "Enabling Hybrid HPCQC Workflows with a Heterogeneous Software Stack"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.14827"
summary: "arXiv:2608.14827v1 Announce Type: new Abstract: In this work, we demonstrate hybrid High Performance Computing-Quantum Computing (HPCQC) workflows on a production petascale system. The demonstration c"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.14827v1 Announce Type: new Abstract: In this work, we demonstrate hybrid High Performance Computing-Quantum Computing (HPCQC) workflows on a production petascale system. The demonstration combines three components: the SuperMUC-NG supercomputer at the Leibniz Supercomputing Centre (LRZ), a 20-qubit superconducting quantum processor provided by IQM Quantum Computers (IQM), and Munich Quantum Valley (MQV)'s Munich Quantum Software Stack (MQSS). Integrating quantum processors into High Performance Computing (HPC) systems requires a heterogeneous software stack capable of orchestrating classical and quantum resources within established supercomputing workflows. MQSS treats Quantum Processing Units (QPUs) as scheduler-managed accelerators and it performs resource coordination following a two-level scheduling scheme. Slurm performs system-level allocation by exposing QPUs as Generic RESources (GRES), while the MQSS Quantum Resource Manager & Compiler Infrastructure (QRM&CI) performs just-in-time compilation and subsequent dispatch of quantum circuits. To integrate with existing HPC operations without modifying the scheduler core, MQSS introduces an open-source SLURM Plugin Suite based on Prolog/Epilog scripts and SPANK modules. Experimental results show that hybrid HPCQC workflows can be executed without significant latency overhead compared to conventional workloads. The presented architecture provides a portable integration model for quantum accelerators on large-scale HPC systems and is directly applicable to next-generation Hewlett Packard Enterprise (HPE) Cray platforms, including LRZ's upcoming 'Blue Lion' supercomputer.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.14827) | 2026-08-18
