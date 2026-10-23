---
title: "FVQKD: A Formal Verification of Quantum Key Distribution Security in Rocq"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.30645"
summary: "arXiv:2610.30645v1 Announce Type: new Abstract: Quantum key distribution (QKD), whose security is derived from quantum mechanics rather than computational assumptions, is moving into standardization a"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.30645v1 Announce Type: new Abstract: Quantum key distribution (QKD), whose security is derived from quantum mechanics rather than computational assumptions, is moving into standardization and commercial deployment. Yet its security guarantees rest on technically delicate proofs checked by hand. Formal verification closes this gap, establishing a two-factor assurance: unconditional security from physical principles, and machine-checked proofs against reasoning errors. We present FVQKD, a Rocq library for machine-checking QKD security proofs. Its first result is a complete, end-to-end machine-checked proof of composable, finite-key security for BB84. The mechanization reconstructs the complete proof infrastructure from first principles, including the smooth entropy framework, the entropic uncertainty relation, and the Quantum Leftover Hash Lemma. It uncovers necessary side conditions that the published argument leaves unstated, one of which reveals a missing proof branch, and it grounds the information-theoretic bound in a formal semantics of protocol execution, which the pen-and-paper analysis lacks. The proof is entirely admit-free, relying only on the Rocq kernel and standard foundational axioms. To our knowledge, this is the first end-to-end formal verification of a QKD security proof. Built on MathComp, MathComp-Analysis, and CoqQ, the development provides quantum-information infrastructure designed for reuse across broader QKD variants and quantum cryptography applications.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.30645) | 2026-10-23
