---
title: "PCC: Proof-Carrying Credentials for Enhanced Anonymity and Post-Quantum Delegation"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2992"
summary: "Delegatable Anonymous Credentials (DACs) let an authority be delegated through a chain of intermediaries and later exercised anonymously, as in DeFi credit delegation. Because presentation is the oper"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Delegatable Anonymous Credentials (DACs) let an authority be delegated through a chain of intermediaries and later exercised anonymously, as in DeFi credit delegation. Because presentation is the operation a holder repeats at every use, its cost is what matters in practice; yet existing DACs build this presentation from the delegation chain itself. We call this limitation prover awareness: to present, a holder must possess and process delegation-lineage material whose shape mirrors the chain. It has two faces: its size makes the presentation cost grow with the delegation depth, and its content exposes the holder to delegation-topology metadata that, in incentive-driven and compliance-aware settings, enables lineage-based policy vetoes, strategic disintermediation, and de facto censorship in otherwise permissionless networks. We formalize the privacy face as Enhanced Delegation Anonymity (EDA), a leakage-parametrized two-observer notion combining verifier-side anonymity with holder-side topology obliviousness, the latter given both as a simulation definition and as an indistinguishability game over paths with identical allowed holder leakage. Because both faces share one cause, the chain-structured credential, a single change of representation removes them together: our framework Proof-Carrying Credentials (PCC) replaces the explicit chain with a single recursively updated proof-carrying state via Non-Uniform Incrementally Verifiable Computation (NIVC), making the presentation independent of the delegation depth and hiding the topology at once, while preserving restricted delegation and expressive presentation. Unlike prior constant-size DACs tied to bilinear pairings, PCC is hardness-agnostic and admits an explicit post-quantum-compatible instantiation in the QROM from transparent FRI-based recursion and hash-based signatures. On consumer-grade hardware, the Halo2 (non-post-quantum) instantiation keeps the verifier-facing proof constant at 7.344KB with 35-36ms verification across all tested depths, and a 128-bit Plonky2 (post-quantum) instantiation keeps a constant 157.9KB proof and 3.8ms verification across depths Lin{1,2,4,8,16}, at 1.03s per delegation step. Holder-side topology hiding and depth-independent presentation are thus achievable at practical recursive-proving cost.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2992) | 2026-11-23
