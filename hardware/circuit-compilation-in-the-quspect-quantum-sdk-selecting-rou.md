---
title: "Circuit compilation in the quspect quantum SDK: selecting routings after coupling-constrained resynthesis"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.22315"
summary: "arXiv:2611.22315v1 Announce Type: new Abstract: quspect is an open-source quantum computing SDK that provides circuit construction, C++ state-vector simulation with adjoint gradients, support for vari"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.22315v1 Announce Type: new Abstract: quspect is an open-source quantum computing SDK that provides circuit construction, C++ state-vector simulation with adjoint gradients, support for variational and combinatorial-optimization algorithms, Hamiltonian simulation, control-pulse envelopes and backends for several cloud quantum processors. Here we describe and evaluate its circuit compiler. Routing and synthesis interact: inserting a SWAP can change the circuit structure that later optimization exploits. At its highest optimization level, the compiler evaluates a screened set of routing candidates by their cost after coupling-constrained resynthesis. The pipeline combines parity-state A* search for small CNOT-phase regions, heuristic synthesis for larger regions, and numerical three-qubit instantiation with a per-block 10^-9 check. For a fixed phase polynomial, A* certifies the minimum CX count when it reaches a goal within budget. On an evaluation set of 55 circuits from 41 arXiv papers on five topologies, the compiler uses 0.616 times as many two-qubit gates as Qiskit O3 (95% circuit-cluster bootstrap interval 0.555-0.679) at 0.592 times its depth. BQSKit level 2 reaches 0.853 and tket 0.930. On a 17-qubit superconducting processor, the compiled circuits had the fewest CZ gates in all six scenarios of the main run. Ablations assess the contributions within the integrated pipeline.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.22315) | 2026-11-18
