---
title: "Scalable Quantum Key Distribution via GHZ Entanglement and Qubit Reuse"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.21667"
summary: "arXiv:2608.21667v1 Announce Type: new Abstract: Conventional Quantum Key Distribution (QKD) requires the transmission of qubits proportional to or exceeding the length of the key, as protocols such as"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.21667v1 Announce Type: new Abstract: Conventional Quantum Key Distribution (QKD) requires the transmission of qubits proportional to or exceeding the length of the key, as protocols such as BB84 transmit more qubits than the final key size due to basis sifting and privacy amplification. Since quantum networks are still in their infancy and have limited capacity, this overhead puts significant pressure on network resources. To address this issue, we propose a Multi-Qubit Greenberger--Horne--Zeilinger (GHZ) State-based QKD scheme that reduces the number of qubits transmitted over the quantum channel. The proposed method transmits one GHZ qubit between endpoints and reuses the resulting entanglement to convey multiple classical key bits with the help of Quantum Non-Demolition (QND) measurements. Under the stated assumptions on authenticated classical communication, local reset verification, and bounded-error QND discrimination, one can transfer L classical bits by generating an (L+1)-qubit GHZ state and transferring one qubit to the remote party. We verify correctness using the NetSquid quantum network simulator: the protocol achieves 100% raw-key fidelity for keys of length up to 12 bits under both ideal conditions and depolarizing noise up to p = 0.005 per round. We further show that the proposed QKD algorithm can be extended to multi-party QKD and server-client deployment. The proposed scheme offers a transmitted-qubit-efficient, noise-tolerant alternative for bandwidth-limited quantum networks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.21667) | 2026-08-25
