---
title: "Orchestrating Key Scarcity: Global Capacity Allocation in Hybrid QKD-PQC Networks"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.27332"
summary: "arXiv:2610.27332v1 Announce Type: cross Abstract: This article presents a Distributed Key Management System (DKMS) that provisions quantum-safe symmetric encryption keys to applications across a netwo"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.27332v1 Announce Type: cross Abstract: This article presents a Distributed Key Management System (DKMS) that provisions quantum-safe symmetric encryption keys to applications across a network. To overcome the distance and rate limitations inherent to Quantum Key Distribution (QKD), the architecture adopts a hybrid design: it utilizes multi-hop trusted relays for physical key transport, while applying an end-to-end Post-Quantum Cryptography (PQC) layer to ensure the relayed key material remains strictly protected from intermediate nodes. Because QKD transforms key generation into a scarce physical resource, managing unpredictable application demands poses a critical capacity allocation problem. The core contribution of this work is an SDN-driven control plane that globally orchestrates the network. Rather than relying on vulnerable hop-by-hop capacity reservations, a central controller simultaneously computes optimal filling rates and multipath routing for all per-peer key buffers. This global orchestration ensures that no application is starved and that all key buffers synchronize their filling processes. Evaluated on a Kubernetes-based digital twin across five distinct network topologies, the controller successfully filled all key buffers to capacity in under six minutes. Furthermore, under deliberately excessive demand, the network demonstrated graceful degradation, safely rejecting excess requests through controlled rate-limiting rather than experiencing catastrophic failure.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.27332) | 2026-10-21
