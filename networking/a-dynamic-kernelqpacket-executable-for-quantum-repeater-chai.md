---
title: "A Dynamic-Kernel/QPacket Executable for Quantum Repeater Chains in Q2NS/ns-3"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.24152"
summary: "arXiv:2608.24152v1 Announce Type: new Abstract: The Quantum Internet operates on entanglement, a non-local, non-copyable, stateful network resource, which motivates protocol organization beyond classi"
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2608.24152v1 Announce Type: new Abstract: The Quantum Internet operates on entanglement, a non-local, non-copyable, stateful network resource, which motivates protocol organization beyond classical layering. We present a first executable specialization of the Dynamic Kernel/QPacket logic from the beyond-layering protocol suite, targeting entanglement distribution over a linear quantum repeater chain. The implementation builds on Q2NS, an ns-3-based quantum-network simulation module available through the ns-3 App Store. It realizes QPacket meta-headers with service intent and append-only action-commit stamps processed by node-local Dynamic Kernels organized as a Planner--Executor--Engine pipeline, while being deliberately scoped to an analytically verifiable service and policy. Within this scoped setting, we study node heterogeneity through a link-preparation policy that accounts for pre-distributed entanglement and uneven entanglement-generation support across nodes, including delegation via QPacket forwarding. Simulations verify analytical link-resolvability models and expose signaling load, forwarding behavior, and QPacket meta-header growth. Results show that QPacket overhead is shaped by more than just encoding, including policy choices and available network resources. Overall, this study demonstrates how the Q2NS/ns-3 substrate can support reproducible, policy-specific evaluation of quantum-native protocol-suite concepts.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.24152) | 2026-08-26
