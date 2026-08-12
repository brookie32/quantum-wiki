---
title: "RF-Budgeted Frame Compilation for Frequency-Multiplexed Superconducting-Qubit Control Using Qubit-Control Identity Records and a Circuit-Informed RFSoC Model"
date: "2026-08-12"
updated: "2026-08-12"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.10013"
summary: "arXiv:2608.10013v1 Announce Type: new Abstract: Frequency-multiplexed superconducting-qubit control requires more than carrier assignment: the RF budget of a shared source can perturb multi-qubit rota"
last_verified: "2026-08-12"
review_by: "2026-11-10"
stale: false
---

arXiv:2608.10013v1 Announce Type: new Abstract: Frequency-multiplexed superconducting-qubit control requires more than carrier assignment: the RF budget of a shared source can perturb multi-qubit rotations through finite bandwidth, crest factor, clipping, quantization, jitter, spurs, compression, crosstalk, and leakage. We present an RF-budgeted frame-compilation and validation workflow that combines qubit-control identity (QID) records, a MATLAB/Simulink-based circuit-informed RFSoC source-chain model, QuTiP qutrit dynamics, and Qiskit-derived algorithm workloads. QID records encode qubit-specific computational and leakage transition frequencies, pulse parameters, and drive-scale calibration, while the RF-chain profile and effective crosstalk-coupling matrix are provided as separate compiler inputs. Candidate multitone RF frames are scheduled under RF-budget constraints, propagated through the RFSoC model, decoded into computational and leakage transition frames, and evaluated in QuTiP for rotation error, leakage-aware fidelity, computational-subspace survival, and transient leakage. The studies progress from single-qutrit pulse closure to pairwise coexistence, multitone RF-frame capacity, and Bernstein-Vazirani (BV) and QAOA microwave layers extracted from Qiskit circuits. The simulations show that longer pulses improve per-frame aggregation but do not necessarily minimize time-normalized layer cost; clustered frequency maps, larger rotations, and multitone leakage stacking tighten closure. Under the nominal RF budget, a Qiskit-derived 12-qubit BV -Y90 layer closes in three validated four-tone frames at 240 ns, while QAOA mixer partitions vary with rotation angle and pulse duration. All reported results are model-based, decoherence-free simulation diagnostics rather than measured hardware fidelities or wiring-reduction claims.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.10013) | 2026-08-12
