---
title: "Quantum-Seeded Distributed Post-Quantum Group Signatures for 5G V2X Communications"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.27316"
summary: "arXiv:2610.27316v1 Announce Type: cross Abstract: Vehicle-to-Everything (V2X) communications rely on elliptic-curve signatures that a quantum adversary breaks and on pseudonym certificates whose anony"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.27316v1 Announce Type: cross Abstract: Vehicle-to-Everything (V2X) communications rely on elliptic-curve signatures that a quantum adversary breaks and on pseudonym certificates whose anonymity rests on rotation rate, not cryptography. This work presents qDGSP, a post-quantum V2X infrastructure: a hash-based dynamic group signature scheme (DGSP, over SPHINCS+ and WOTS+) distributed between a central controller and roadside verifiers. Group keys derive deterministically from quantum key distribution (QKD) seeds served over the ETSI GS QKD 014 interface, so no group-signature secret crosses the classical channel. qDGSP-EA (Ephemeral Association) binds an ephemeral ML-DSA-65 key to one group signature per 5G cell: messages remain unlinkable across cells, linkable within one. On a testbed with emulated 5G links, median end-to-end latency stayed within the 100ms ETSI budget for every variant. The qDGSP-EA intra-cell DENM matched the NIST ML-DSA-65 baseline on the wire, and under load EA mode raised delivery from roughly 78% to 93%.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.27316) | 2026-10-21
