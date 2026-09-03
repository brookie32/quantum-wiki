---
title: "Jacobian Diagnostics for Under-Constrained Zero-Knowledge Circuits"
date: "2026-09-01"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1852"
summary: "Under-constrained arithmetic circuits are a recurring source of soundness failures in zero-knowledge applications: after fixing the public statement, a malicious prover may be able to assign a securit"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

Under-constrained arithmetic circuits are a recurring source of soundness failures in zero-knowledge applications: after fixing the public statement, a malicious prover may be able to assign a security-relevant wire in more than one way while still satisfying the circuit. Existing tools attack this uniqueness question with solver-based checking, direct polynomial solving, abstract interpretation, or fuzzing. We study a complementary algebraic diagnostic based on exact Jacobian linear algebra. The method separates three notions that are often conflated: first-order rigidity at a sampled witness, finite algebraic dependence on an irreducible component, and uniqueness over the circuit field. At a satisfying assignment, the kernel of the constraint Jacobian augmented with rows fixing the statement coordinates is the Zariski tangent space of the corresponding fibre scheme, so motion of a target coordinate in this kernel certifies infinitesimal freedom at that witness. Under suitable separability hypotheses, the associated differential representation also recovers component-wise algebraic dependence, while a certified triangular degree calculus provides multiplicity bounds for locally rigid targets. An exact sparse implementation handles exttt{gnark} R1CS instances in the 6k--60k-constraint range in preliminary measurements, and a checkable degree budget (m<log_2 p quadratic constraints) discharges the separability hypothesis at gadget scale. The principal limitation is witness locality: a circuit may appear rigid at an honest witness while becoming under-constrained on a prover-reachable degenerate branch. In a measured 2{,}396-constraint exttt{gnark}~0.14.0 scalar-multiplication gadget, an honest witness exposed no free target wires while a degenerate adversarial witness exposed five. We therefore position Jacobian analysis as a scalable candidate detector and localisation tool, to be combined with adversarial witness generation and solver- or certificate-based confirmation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1852) | 2026-09-01
