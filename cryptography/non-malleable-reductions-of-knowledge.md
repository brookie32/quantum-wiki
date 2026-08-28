---
title: "Non-Malleable Reductions of Knowledge"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1822"
summary: "Non-malleability for non-interactive zero-knowledge proofs requires that, given a proof for a statement, it is infeasible to derive a valid proof for a related statement without knowing a correspondin"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Non-malleability for non-interactive zero-knowledge proofs requires that, given a proof for a statement, it is infeasible to derive a valid proof for a related statement without knowing a corresponding witness. We introduce a modular framework for analyzing non-malleable reductions of knowledge (RoKs). A reduction of knowledge transforms the task of proving knowledge for a source relation into proving knowledge for a target relation, often simpler or more structured. RoKs are an extremely useful tools for compositions. We identify different settings in which the composition of two RoKs, and in particular two non-interactive RoKs obtained via the Fiat-Shamir transform, preserves simulation extractability, and thus non-malleability. Our framework isolates simple and concrete properties required from each component, including novel forms of zero knowledge and new security notions that are easier to verify than full simulation extractability. This yields a systematic toolbox for establishing non malleability in modular proof systems. Finally, we illustrate the power of our approach by analyzing LaBRADOR (Beullens and Seiler, CRYPTO’23), a lattice based proof system for R1CS. We provide the first analysis of its simulation extractability and, since LaBRADOR is not zero knowledge, we design a zero knowledge variant that preserves its practical efficiency and sublinear proof size. Our results show that non-malleability for advanced proof systems can be achieved modularly, significantly simplifying the security analysis.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1822) | 2026-08-27
