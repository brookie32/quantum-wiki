---
title: "QubiC 2.0: An Extensible Open-Source Qubit Control System Capable of Mid-Circuit Measurement and Feed-Forward"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2309.10333"
summary: "arXiv:2309.10333v2 Announce Type: replace Abstract: Researchers manipulate and measure quantum processing units via the classical electronics control system. We developed an open-source FPGA-based qua"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2309.10333v2 Announce Type: replace Abstract: Researchers manipulate and measure quantum processing units via the classical electronics control system. We developed an open-source FPGA-based quantum bit control system called QubiC for superconducting qubits. After years of qubit calibration and testing experience on QubiC 1.0, we recognized the need for mid-circuit measurement and feed-forward capabilities to implement advanced quantum algorithms, and upgraded the system to QubiC 2.0 on an AMD ZCU216 RFSoC evaluation board with all these enriched features. The system uses portable FPGA gateware with a simplified processor to handle commands on-the-fly. For design simplicity and straightforward scaling, we adopted a multi-core distributed architecture, assigning one processor core per qubit. The pulses combine the unique pulse envelope and carrier information specified in a command. Each pulse envelope is pre-stored in the FPGA's block RAMs, ensuring speed and reusability throughout the quantum circuit, while pulse parameters including amplitude, phase, and frequency can be updated from pulse to pulse. The software stack is developed in Python, running on both the FPGA's ARM core and a host computer via XML-RPC. Quantum circuits can be described in a high-level language supporting both pulse-level and native-gate-level programming with high-level control flow constructs, and are compiled into binary commands loaded into the FPGA. With QubiC 2.0, we achieved multi-FPGA synchronization and low-latency data communication, and demonstrated feed-forward experiments on conditional circuits. The system also serves as a platform for artificial intelligence and machine learning driven quantum control, such as FPGA-based real-time quantum state discrimination. The enhanced QubiC system provides researchers with powerful tools to explore and implement advanced quantum algorithms and applications.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2309.10333) | 2026-10-26
