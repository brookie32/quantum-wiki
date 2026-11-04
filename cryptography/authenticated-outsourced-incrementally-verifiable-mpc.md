---
title: "Authenticated Outsourced Incrementally Verifiable MPC"
date: "2026-11-02"
updated: "2026-11-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2721"
summary: "Many privacy-preserving applications such as iterative machine learning training require executing ongoing computations over a secret state for long periods of time. While MPC enables secure computati"
last_verified: "2026-11-04"
review_by: "2027-02-02"
stale: false
---

Many privacy-preserving applications such as iterative machine learning training require executing ongoing computations over a secret state for long periods of time. While MPC enables secure computation, long-lived secret state is vulnerable to adaptive corruptions, requiring periodic share refreshes and committee rotation. In many settings, it is desirable for external parties to be able to verify that these state updates and rotations are performed correctly, but existing approaches for such public verifiability incur high overhead as they require MPC nodes to generate expensive proofs over secret-shared data. We propose Authenticated Outsourced Incrementally Verifiable MPC (IV-MPC), a framework for efficient public verification of long-running MPC computation. Our approach decouples private proof computation (run by MPC nodes) from public tasks within the proof generation that can be delegated to a single external prover P^*. To realize this architecture, we introduce three main components: (1) a Private-opening Polynomial Commitment Scheme (PoPCS) that lets an incoming committee prove they received the correct state shares without revealing the underlying data; (2) an efficient distributed proof system based on the sumcheck protocol and compressed Sigma-protocols to verify state updates; and (3) a stateless handover technique that anchors committee transfers to a fixed state commitment, preventing proof sizes from growing over time. Combined with an incrementally verifiable computation (IVC) proof run by the external prover P^*, IV-MPC enables external auditors to verify correctness of MPC computation at every round with verification time asymptotically independent of the total number of epochs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2721) | 2026-11-02
