---
title: "Scalable Unitary State-Encoding for Generic Large Data"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.09760"
summary: "arXiv:2611.09760v1 Announce Type: new Abstract: Efficient encoding of data into quantum states remains a fundamental bottleneck in many quantum computing protocols, which would otherwise offer advanta"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2611.09760v1 Announce Type: new Abstract: Efficient encoding of data into quantum states remains a fundamental bottleneck in many quantum computing protocols, which would otherwise offer advantages over their classical counterparts. Here, we introduce deterministic and scalable amplitude-encoding methods with low two-qubit gate costs and tunable trade-offs between circuit depth and encoding fidelity. Our approaches require no amplitude amplification or mid-circuit measurement and are capable of encoding arbitrary complex data or queryable functions by using tensor-networks to go beyond what can be held in classical memory. Our principle contributions are two complementary algorithms for simplifying fully controlled multiplexer circuits to one- and two-qubit gates. In the first, we formally map the elimination of redundant gate controls to a Boolean logic minimization problem, while in the second we utilize a single ancilla qubit to map the multi-controlled rotation gates to a sequence of one- and two-qubit operations via the Walsh-Hadamard spectrum of the gate angles. We benchmark these methods across a broad range of function classes, characterizing their total depth in an all-to-all connectivity graph against system size and target fidelity. Hybridizing our methods gives up to orders of magnitude improvement in circuit depth at equivalent state fidelity compared to the default state-preparation method in the Qiskit package. We furthermore demonstrate our method on IQM hardware with a square lattice connectivity, finding excellent fidelity, even with minimal noise mitigation. By significantly reducing gate depth for encoding, this work enables the experimental execution of applications on current and near-term hardware which would otherwise be reduced to noise before the first calculation step, shortening the time horizon to robust quantum utility.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.09760) | 2026-11-09
