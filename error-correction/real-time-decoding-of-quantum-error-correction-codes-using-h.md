---
title: "Real-time decoding of quantum error correction codes using high-performance computing"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.03948"
summary: "arXiv:2608.03948v1 Announce Type: new Abstract: Quantum error correction (QEC) is indispensable for building scalable fault-tolerant quantum computers. Effective QEC demands stringent real-time decodi"
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2608.03948v1 Announce Type: new Abstract: Quantum error correction (QEC) is indispensable for building scalable fault-tolerant quantum computers. Effective QEC demands stringent real-time decoding: the decoder must process syndrome measurements and determine corrections within a time scale--typically on the order of microseconds, to avoid data backlog. Scaling to large number of logical qubits further necessitates significant computational resources. In this work, we propose an architecture, called THQLink, for real-time decoding of quantum error correction codes using high-performance computing (HPC) resources. The network connecting the HPC and the control system of quantum processing unit (QPU) is built on TH-Express and can be adapted to different quantum technologies and their associated control stacks. We report a round-trip latency of 2.944 mus on average, with an incremental overhead of 130 ns per additional hop. Using a parallel window strategy, we demonstrate real-time decoding (1 mus per QEC round) of the surface code up to distance 19 using a matching-based decoder on CPUs. Our work presents a scalable framework for real-time decoding in fault-tolerant quantum computing. It can be readily applied to quantum-centric supercomputers that feature tight integration between QPU and HPC resources, thereby enabling efficient support for hybrid quantum-classical algorithms and computation-intensive workloads offloaded from the QPU.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.03948) | 2026-08-05
