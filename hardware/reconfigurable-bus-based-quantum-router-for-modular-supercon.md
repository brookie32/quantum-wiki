---
title: "Reconfigurable bus-based quantum router for modular superconducting processors"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.28881"
summary: "arXiv:2609.28881v1 Announce Type: new Abstract: Scaling superconducting quantum processors requires interconnects that provide both non-local connectivity and parallel entangling operations. Nearest-n"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.28881v1 Announce Type: new Abstract: Scaling superconducting quantum processors requires interconnects that provide both non-local connectivity and parallel entangling operations. Nearest-neighbour couplings require distant interactions to be routed through SWAP networks, increasing the native two-qubit-gate count and potentially extending the circuit critical path. Here we introduce a bus-based reconfigurable quantum router for modular superconducting processors. Flux-tunable SQUID couplers selectively connect interface qubits to two shared buses, allowing destructive interference to suppress idle interactions while supporting two disjoint controlled-Z (CZ) gates in parallel. Full-system Hamiltonian simulations yield parallel-gate errors at the level of 10^{-3}, and open-system analysis identifies the coherence requirements for high-fidelity operation. We further assess the circuit-level consequences using hardware-aware compilation and resource-constrained scheduling. For 36-qubit quantum Fourier transform (QFT), QAOA-MaxCut and random-pairing circuits, the router reduces the median SWAP count by up to 34% and the native CZ count by up to 20% relative to a matched two-dimensional grid. End-to-end depth reduction is circuit dependent, reaching 20% for QAOA-MaxCut but remaining negligible for the QFT despite its lower gate count. These results show that enhanced connectivity and schedulable parallelism provide distinct benefits, establishing the router as a compiler-visible hardware resource for modular superconducting quantum processors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.28881) | 2026-09-25
