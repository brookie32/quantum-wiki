---
title: "Quantum Data Processing Unit for Neutral-Atom Quantum Computers"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.17652"
summary: "arXiv:2611.17652v1 Announce Type: new Abstract: Quantum computers need real-time classical processing to convert measurement data into feedback within device-specific timing constraints. We introduce "
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.17652v1 Announce Type: new Abstract: Quantum computers need real-time classical processing to convert measurement data into feedback within device-specific timing constraints. We introduce the quantum data processing unit (QDPU), an architecture between a quantum device and its controller. Its core is a machine-learned quantum data model (QDM), adapted to the measurement response and noise characteristics of the device. We implement an FPGA pipeline for neutral-atom array assembly that performs occupancy detection and rearrangement scheduling in FPGA logic. One calibrated matched-filter lane classifies a 50imes50 array in 12.5 mus. An atom-loss model using a software reference planner evaluates a 35imes35 target with a 60 s trap lifetime and 0.1% loss per moved atom. Removing an assumed 150 ms host round trip raises the predicted assembly success from 8% to 85% and reduces the wall-clock time per successful assembly from 19 s to 0.16 s. A GPU-based outer loop is proposed for refitting model parameters between runs. Its NVQLink transport is measured on the board: over 10 GbE to an NVIDIA DGX Spark, the median FPGA-to-host-to-FPGA round trip is 2.74 mus for 128-byte messages forwarded by a CPU core. A separate 12-bit learned qLDPC kernel is placed and routed for the same FPGA target, with a derived latency of 0.84 ms per round for a [[1122,148]] lifted-product code under code-capacity noise. A quantised GraphMP ranking kernel for the same code runs on the board with a median host-to-FPGA-to-host latency of 50.5 mus with one shot in flight, excluding host-side BP+OSD post-processing. Together, these implementations illustrate a shared architecture with workload-specific models and timing requirements.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.17652) | 2026-11-16
