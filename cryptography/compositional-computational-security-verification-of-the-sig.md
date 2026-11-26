---
title: "Compositional, Computational Security Verification of the Signal Implementation Under Fine-Grained Compromise with Owl"
date: "2026-11-24"
updated: "2026-11-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3014"
summary: "Key-ratchet protocols, exemplified by the Signal protocol suite, are at the core of widely deployed end-to-end encrypted messaging applications. These protocols rely on long-running chains of key deri"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

Key-ratchet protocols, exemplified by the Signal protocol suite, are at the core of widely deployed end-to-end encrypted messaging applications. These protocols rely on long-running chains of key derivation, in which fresh keys are continuously derived from prior state to encrypt messages. Their security goals include fine-grained secrecy properties, particularly forward secrecy (current messages remain secret under future compromises) and post-compromise security (the protocol can recover secrecy after a compromise), which can be difficult to reason about in formal protocol-verification tools. We extend the Owl protocol-verification framework to provide computational guarantees of fine-grained secrecy properties for models that compile to practical implementations. Our extensions comprise a new type-based model of key derivation chains and a novel technique for reasoning about fine-grained secrecy properties via logical queries over the protocol's key hierarchy. Leveraging these extensions, we apply Owl to Signal's entire two-party messaging protocol suite, developing high-fidelity models and proving its core security properties, including fine-grained secrecy. Owl's type-based methodology allows us to reason compositionally across Signal's sub-protocols, but still yields a full-strength end-to-end security guarantee. Owl's compilation pipeline translates our models into Rust libraries that interoperate with, and match the performance of, Signal's open-source implementations. We also extend Owl's methodology by directly verifying Signal's existing Rust implementation against Owl-generated specifications.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3014) | 2026-11-24
