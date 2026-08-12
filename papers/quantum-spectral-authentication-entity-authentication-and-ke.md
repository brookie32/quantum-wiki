---
title: "Quantum Spectral Authentication: Entity Authentication and Key Derivation from a Hidden Eigenstate of a Public Unitary Challenge"
date: "2026-08-12"
updated: "2026-08-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.24868"
summary: "arXiv:2603.24868v2 Announce Type: replace Abstract: We introduce Quantum Spectral Authentication (QSA), a symmetric-key entity-authentication and key-derivation protocol in which a remote endpoint pro"
last_verified: "2026-08-12"
review_by: "2026-11-10"
stale: false
---

arXiv:2603.24868v2 Announce Type: replace Abstract: We introduce Quantum Spectral Authentication (QSA), a symmetric-key entity-authentication and key-derivation protocol in which a remote endpoint proves it still holds a hidden planted state, an eigenstate of the challenge it can prepare, without revealing it. Each round issues a fresh public unitary challenge with its own planted state, and the endpoint returns an eigenphase feature from which both parties derive transcript-bound session material. QSA runs in two provisioning modes with materially different security: a seed mode, storing a classical seed that regenerates the planted state, and a state mode, holding only the physical register carrying it, non-copyable and consumed on use. We give a formal security model in which QSA is an identification scheme, prove mutual authentication under a single label-hiding assumption, and prove unconditionally that the published spectrum is near-uniform at the readout resolution, leaving at least m-1 bits of min-entropy per instance; state mode satisfies the assumption by construction. We develop a symmetric verifier-driven compiler compatible with low-depth quantum phase estimation, which also admits a fast path that recovers the label by an inverse-compiler measurement. Simulations show it is more noise-tolerant than an asymmetric alternative, and experiments on IBM ibm_fez provide a hardware sanity check.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.24868) | 2026-08-12
