---
title: "BRIDGE: Lazy-Move Compilation for Dual-Species Neutral-Atom Quantum Computers"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.31833"
summary: "arXiv:2606.31833v2 Announce Type: replace Abstract: Neutral-atom quantum computers commonly connect distant qubits by transporting atoms, incurring trap-handover errors, heating, and atom loss. We pre"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2606.31833v2 Announce Type: replace Abstract: Neutral-atom quantum computers commonly connect distant qubits by transporting atoms, incurring trap-handover errors, heating, and atom loss. We present BRIDGE (Buffer-Relay Interconnect for Data-stable Gate Execution), a hardware--software co-design that connects stationary data atoms through a fixed, second-species buffer network. Short buffer chains mediate remote controlled-Z gates and return to their initial states after each operation. BRIDGE-F combines relay routing with buffer-mediated SWAPs to relocate quantum states without transporting atoms. BRIDGE-H additionally permits data-atom transport when its full modeled cost is offset by higher survival-weighted fidelity. Across 21 circuits, BRIDGE-F exceeds ZAP and Enola in modeled survival-weighted fidelity, with geometric-mean ratios of 2.1imes and 38imes and medians of 1.3imes and 3.7imes. Modeled execution latency is lower by factors of approximately 500 and 1{,}350, respectively, with circuit single-qubit costs excluded and relay/SWAP Hadamards included. On the same fabric, BRIDGE-F matches or exceeds SABRE-based routing on 17 circuits. Rescoring nominal plans with relay-module error equal to direct-CZ error preserves the advantage over ZAP across all 21 circuits, although recompilation can underperform on QFT. These results identify stationary buffer-mediated connectivity as a promising alternative to repeated atom transport under the stated physical assumptions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.31833) | 2026-11-06
