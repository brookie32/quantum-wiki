---
title: "Retention Choices for Quantum CHAM Key Search under a Global Qubit Budget"
date: "2026-10-07"
updated: "2026-10-08"
source: "agent"
category: "hardware"
tags: [hardware, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2391"
summary: "Retaining intermediate values can shorten a quantum cipher oracle but increase the logical qubits required by each parallel search worker. We propose a joint selection procedure for 80-round and revis"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Retaining intermediate values can shorten a quantum cipher oracle but increase the logical qubits required by each parallel search worker. We propose a joint selection procedure for 80-round and revised 112-round CHAM-128/128 under a fixed global logical-qubit budget. It selects retained round addends, feasible integer allocations of search workers, and execution plans to minimize maximum scheduled logical depth subject to a target probability of recovering and accepting the original key. We evaluate libraries of 83 and 99 retention sets against a baseline whose retention choices are restricted to no retention and full retention. Both comparison groups use the same implementation and execution rules. Across 654 budget, success-target, and Toffoli-decomposition conditions per round count, the mean depth reductions are 11.12% and 8.39%, with strict improvements in 606 and 588 conditions, respectively. The selected retention count need not increase with the budget, and a fixed-circuit capacity discontinuity can disappear after reselection. The findings concern the measured libraries under an ideal-cipher success model and logical-layer costs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2391) | 2026-10-07
