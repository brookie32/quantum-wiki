---
title: "Singlet flags: using native entanglement to restore the circuit distance of shuttled qLDPC codes in silicon"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.23528"
summary: "arXiv:2611.23528v1 Announce Type: new Abstract: High-rate quantum low-density parity-check (qLDPC) codes could greatly reduce the qubit count of silicon spin-qubit processors, but their checks are lon"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23528v1 Announce Type: new Abstract: High-rate quantum low-density parity-check (qLDPC) codes could greatly reduce the qubit count of silicon spin-qubit processors, but their checks are long-range and of high weight. Shuttling one ancilla electron through every data qubit of a check measures such checks, but a single fault on the ancilla spreads to several data qubits, so the circuit distance can fall far below the code distance. We make the mobile ancilla one half of a spin singlet whose partner stays at home; a Bell measurement at the end of the check provides a flag for isolated bit-flip faults acquired during the walk. Using new distance-6 codes with check weights 8, 10 and 12, and exact circuit distances from two independent solvers, we show that without the flag the circuit distance falls as check weight grows, to 1 at weight 12, while with it every weight-8 and weight-10 code recovers circuit distance 5 or 6 and corrects as many faults as the code. For codes of distance 8 to 12 the flag raises the circuit distance by one to four, and the Gross code [[144,12,12]] rises from 7 to 10. In circuit-level simulations of shuttled spin qubits, the flag lowers logical error rates by typically 2-10x across bivariate-bicycle, circulant-permutation and surface codes, and the gain survives percent-level flag-readout errors and bit flips on the singlet's electrons. BP+OSD does not reach the full circuit distance of the flagged circuits, so our flagged logical error rates are upper bounds: decoding the same shots exactly raises the flag's gain on the distance-6 codes from 3-7x to 5-17x for the weight-6 BB code, and from 1-12x to 5-90x at weights 8 and 10 for p >= 2.5x10^-4.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.23528) | 2026-11-19
