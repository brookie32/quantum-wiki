---
title: "Vanilla Exact Synthesis of CNOT Circuits is NP-hard"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.04160"
summary: "arXiv:2609.04160v1 Announce Type: new Abstract: Exact CNOT synthesis asks for a minimum-size CNOT circuit implementing an invertible linear transformation. Although several related synthesis models ha"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.04160v1 Announce Type: new Abstract: Exact CNOT synthesis asks for a minimum-size CNOT circuit implementing an invertible linear transformation. Although several related synthesis models have been shown to be computationally hard, their hardness proofs rely on additional structure such as restricted qubit connectivity, encoded inputs, or unrestricted intermediate variables. The complexity of the most basic setting---identity input, a fixed number of labelled qubits, no ancillas, and all-to-all CNOT connectivity---had remained unresolved. In this work, we prove that the decision version of this vanilla exact CNOT synthesis problem is NP-complete, and consequently that its optimization version is NP-hard. Our proof gives a polynomial-time reduction from the Hamiltonian-path problem on grid graphs in two steps. First, we isometrically embed the grid graph into a hypercube via a unary encoding map. We then encode this hypercube Hamiltonian path problem into vanilla exact CNOT synthesis. The main challenge is that CNOT synthesis specifies only the final parity matrix and cannot directly enforce the intermediate vertex visits required by a Hamiltonian path. To overcome this difficulty, we introduce extra recorder qubits that encode the required intermediate vertex visits into the final transformation, forcing any CNOT circuit implementation to realize the intended path structure. Beyond CNOT synthesis, our result directly implies hardness for several related problems, including the shortest word problem over GL(n,2), distance computation on Cayley graphs over GL(n,2), minimization of sequential XOR programs, and exact synthesis of phase polynomial circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.04160) | 2026-09-04
