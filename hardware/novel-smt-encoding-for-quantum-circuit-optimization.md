---
title: "Novel SMT Encoding for Quantum Circuit Optimization"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "hardware"
tags: [hardware, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1815"
summary: "In recent years, quantum circuit optimization has become an important research topic. Motivated by the fact that quantum gates act on fixed physical wires and modify only their target wires, we propos"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

In recent years, quantum circuit optimization has become an important research topic. Motivated by the fact that quantum gates act on fixed physical wires and modify only their target wires, we propose two SMT encodings: an exact-G encoding and an at-most-G encoding with null gates. Our method speeds up most tested 4-bit S-box instances, achieving up to approximately 130x speedup on the ELEPHANT S-box. Importantly, our method enables automated synthesis of practical 5-bit S-box quantum circuits, such as KECCAK and ASCON. For the KECCAK S-box, in the no-ancilla setting, our model obtains concrete implementations with 17 NCT gates and full depth 51, and with 16 NCT gates and full depth 52, improving the EUROCRYPT 2025 result of Huang et al. It further finds a 13-gate implementation with full depth 55, which is gate-count optimal in the no-ancilla setting under the NCT gate set. In addition, when one ancilla qubit is allowed, our model obtains KECCAK implementations with Toffoli count 5, matching the theoretical lower bound. Finally, our model can also be applied to small-scale linear-layer implementation; for example, it finds a 24-CNOT implementation with depth 3 for the 16x16 linear matrix of MIDORI.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1815) | 2026-08-27
