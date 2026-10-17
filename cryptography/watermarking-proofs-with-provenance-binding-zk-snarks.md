---
title: "Watermarking Proofs with Provenance-Binding ZK-SNARKs"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2516"
summary: "The emerging ecosystem of outsourced proving services, decentralized prover networks, and prover marketplaces raises a new requirement for ZK-SNARKs: the need to watermark proofs with provenance infor"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

The emerging ecosystem of outsourced proving services, decentralized prover networks, and prover marketplaces raises a new requirement for ZK-SNARKs: the need to watermark proofs with provenance information, such as the prover identity and a fresh request-time nonce. The prover identity records who should receive credit for the proof, while the nonce binds the proof to a particular request and is intended to prevent the prover from reusing work performed before that request was created. The key security requirement is that a prover must perform fresh work—comparable to computing the proof from scratch—when generating a proof for a fresh provenance, even if the attacker may have generated the same proofs before or performed precomputation. Prior attempts, such as Succinct Network, proposed embedding provenance information in the Fiat-Shamir challenges, though without a rigorous security definition or analysis. We show that this approach is not secure and is vulnerable to preprocessing attacks, in which an adversary can precompute provenance-independent information that can later be used to reduce the effort required to generate proofs for a fresh provenance. We instantiate these attacks against KZG-PLONK. To arrive at a secure construction, we propose the first formal definition for provenance-binding ZK-SNARKs to capture the above desired property. We present a generic construction that augments code-based polynomial commitments, such as BaseFold and FRI, with provenance binding. Compiling them with Poly-IOPs yields provenance-binding ZK-SNARKs. Our construction incurs minimal overhead.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2516) | 2026-10-16
