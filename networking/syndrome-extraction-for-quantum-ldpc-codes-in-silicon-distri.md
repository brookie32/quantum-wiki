---
title: "Syndrome extraction for quantum LDPC codes in silicon: Distributed entanglement and mobile ancillas"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13371"
summary: "arXiv:2611.13371v1 Announce Type: new Abstract: Quantum low-density parity-check (qLDPC) codes can reduce the number of data qubits required per logical qubit, but their checks require long-range inte"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13371v1 Announce Type: new Abstract: Quantum low-density parity-check (qLDPC) codes can reduce the number of data qubits required per logical qubit, but their checks require long-range interactions on a planar device. We develop a singlet fabric for bivariate-bicycle codes on a silicon node network. Spin singlets are generated on shuttling lanes and distributed between nodes, where local operations consume them to measure non-local stabilizers. We construct two syndrome-extraction circuits, based on distributed GHZ states and ancilla teleportation, and evaluate them using hardware-constrained schedules and circuit-level memory simulations. We compare these circuits with CAbLECAR, which transports a mobile ancilla between the data qubits of each check. Teleportation can outperform CAbLECAR on its original layout when transport includes spin flips as well as dephasing. Placing the mobile ancilla on our node lattice, however, shortens the mean scheduled route for the [[144,12,12]] Gross code from 350 to 153 mum and lowers its logical error rate up to 50-fold in the sampled bit-flip regime. Direct transport then achieves a lower logical error rate than either singlet circuit at every sampled Gross-code point. With frequent transport bit flips, the GHZ circuit overtakes direct transport once two-qubit gate and readout errors fall below about 4-5imes10^{-4}, roughly half the value assumed here. Fixing the ancilla's data-visit order reveals a trade-off between shorter routes and the correlated errors produced by ancilla faults. Source heralding improves both singlet circuits, whereas phase purification helps the GHZ circuit only above a noise-dependent crossover and worsens teleportation throughout. These results show that the physical layout and interaction order can be as consequential as the choice of extraction circuit, and that cleaner entangled resources do not necessarily produce a more reliable logical memory.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13371) | 2026-11-11
