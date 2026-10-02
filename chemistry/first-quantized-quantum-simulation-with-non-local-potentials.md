---
title: "First-quantized quantum simulation with non-local potentials by matrix-product-state encoding"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00521"
summary: "arXiv:2610.00521v1 Announce Type: new Abstract: Quantum simulations based on first-quantized approaches can offer lower space and gate complexities than second-quantized approaches. The gate requireme"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00521v1 Announce Type: new Abstract: Quantum simulations based on first-quantized approaches can offer lower space and gate complexities than second-quantized approaches. The gate requirements for these simulations can be further reduced by employing pseudopotentials, a technique widely used in classical quantum chemistry calculations to decrease the number of simulated electrons. However, implementing pseudopotentials in quantum circuits remains challenging due to their non-local nature. In this study, we proposed a method to efficiently implement non-local potentials using matrix product state (MPS) encoding. MPS encoding allows us to efficiently implement a Trotter step operator with a circuit depth of O(deg(V_{loc}) n^{deg(V_{loc})} + 8Lnn_{atom}hi^2 + 2n^2), where deg(V_{loc}) is the degree of the polynomial local potential, n_{atom} is the number of atoms in the system, L is the maximum number of projector functions across all atoms, and n is the number of qubits used to represent the binary-encoded wave function in one-dimensional space. We demonstrated the effectiveness of this approach by applying it to a model of the ionization of a one-dimensional hydrogen atom driven by an ultrashort laser pulse. Our results showed that MPS encoding significantly reduces the required circuit depth compared to a direct unitary decomposition, providing a pathway for practical first-quantized simulations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00521) | 2026-10-02
