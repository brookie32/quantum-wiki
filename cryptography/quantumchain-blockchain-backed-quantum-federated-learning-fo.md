---
title: "QuantumChain: Blockchain-Backed Quantum Federated Learning for Financial Fraud Detection"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.21449"
summary: "arXiv:2607.21449v1 Announce Type: new Abstract: Financial fraud detection is challenged by decentralized data, severe class imbalance, and privacy constraints. This paper presents QuantumChain, a secu"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.21449v1 Announce Type: new Abstract: Financial fraud detection is challenged by decentralized data, severe class imbalance, and privacy constraints. This paper presents QuantumChain, a secure Quantum Federated Learning (QFL) framework that combines hybrid quantum-classical neural networks, encrypted federated aggregation, blockchain-based auditability, and quantum-secure communication. Each client trains a local hybrid model in which a variational quantum circuit is embedded between classical neural layers, while model updates are protected through homomorphic encryption, threshold secret sharing, and QKD-based keying. A permissioned blockchain records aggregation events and supports reputation-weighted trust among participants. We evaluate QuantumChain on financial transaction data using a compact, size-matched classical baseline to isolate the effect of the quantum layer. Results show that the HQNN achieves comparable accuracy while improving fraud-class recall in most settings, reaching 94.6% recall compared with 93.2% for the classical model. The Deep QLayer improves performance in full-data settings, suggesting that added circuit depth helps recover representational capacity when the shallow circuit becomes limited. Mixed-state simulations further show that the recall trend persists under non-ideal quantum evolution. In federated deployment with 10 heterogeneous clients, global accuracy increases from 97.7% to 98.8% over five rounds before stabilizing. These results show that QuantumChain can integrate depth-aware hybrid quantum models into a secure federated fraud-detection pipeline while maintaining stable global convergence.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.21449) | 2026-07-24
