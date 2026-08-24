---
title: "Granthi: Higher-Order Quantum Programming via Unitary Wiring"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.20443"
summary: "arXiv:2608.20443v1 Announce Type: new Abstract: Existing quantum programming languages confine higher order structure to a classical host while restricting the quantum layer to first order operations "
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2608.20443v1 Announce Type: new Abstract: Existing quantum programming languages confine higher order structure to a classical host while restricting the quantum layer to first order operations on qubits. This paper presents Granthi, a purely unitary higher-order quantum programming language built on three design commitments: quantum programs are first class values that may be passed, returned, and coherently composed; additive structure is tag-preserving routing rather than observational branching, so control may remain in superposition; and programmer-facing finite label types with named reversible operations provide domain-level control spaces without exposing tag management. Every well-typed term, including at function type, denotes a unitary on its boundary interface, and the compiler realizes exactly its wiring as a quantum circuit on the physical qubit layout (assuming correctness of the pytket backend). Granthi is implemented end-to-end: an OCaml DSL elaborates surface programs through a binder-free core IR to executable quantum circuits via pytket. The language directly supports the quantum switch, compiled to a static circuit, as well as interference on control-flow history and structured finite control, all within the purely unitary fragment.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.20443) | 2026-08-24
