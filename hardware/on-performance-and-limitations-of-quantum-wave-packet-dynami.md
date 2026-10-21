---
title: "On Performance and Limitations of Quantum Wave Packet Dynamics Simulated using NISQ Hardware"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.20078"
summary: "arXiv:2605.20078v2 Announce Type: replace Abstract: We investigate one-dimensional quantum wave-packet dynamics using a grid-based encoding of the wave function onto qubit registers. Time evolution is"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2605.20078v2 Announce Type: replace Abstract: We investigate one-dimensional quantum wave-packet dynamics using a grid-based encoding of the wave function onto qubit registers. Time evolution is implemented using a split operator approach, with the kinetic energy operator realized via the Quantum Fourier Transform (QFT) and arbitrary discretized potentials represented by commuting Pauli-Z gates. The algorithm is benchmarked against classical grid-based simulations and validated using a noiseless Qiskit Statevector simulator before being implemented on current quantum hardware (IBM Quantum and IonQ) for qubit counts ranging from two to five. Good agreement with benchmark calculations is obtained for two- and three-qubit implementations, while deviations increase at larger qubit counts due to hardware noise and increased circuit depth. Among the devices examined, the algorithm maintains closer agreement with the benchmark on the trapped-ion IonQ Forte processor as the number of qubits increases.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.20078) | 2026-10-21
