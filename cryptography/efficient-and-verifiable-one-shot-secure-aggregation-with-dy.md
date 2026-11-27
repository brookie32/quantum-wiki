---
title: "Efficient and Verifiable One-Shot Secure Aggregation with Dynamic Client Participation"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3021"
summary: "Privacy-preserving federated learning (PPFL) often relies on multi-round secure aggregation, which increases communication overhead and the risk of client dropout. Recent one-shot secure aggregation p"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Privacy-preserving federated learning (PPFL) often relies on multi-round secure aggregation, which increases communication overhead and the risk of client dropout. Recent one-shot secure aggregation protocols, including Willow (CRYPTO 2025), OPA (CRYPTO 2025), and TACITA (CCS 2026), successfully eliminate multi-round client interactions. However, they still incur substantial computation and communication overhead due to heavy cryptographic primitives. More critically, none of them provides public verifiability against a malicious server, meaning the server can forge or omit inputs without detection. We present OSA, a committee-assisted one-shot secure aggregation protocol that supports dynamic client participation. OSA securely realizes the summation functionality against a malicious server with abort under the ring learning with errors (RLWE) assumption. We further present VOSA, a verifiable extension of OSA that enables an independent verifier to check the correctness of the server’s reported aggregate. We evaluate OSA against state-of-the-art one-shot protocols (Willow, OPA, and TACITA), and VOSA against the state-of-the-art aggregate signature scheme, mPVAS (USENIX Security 2026). Under the default experimental setting, OSA achieves speedups of approximately 11.41imes--761.96imes for client-side computation, 2.43imes--106.21imes for server-side computation, and 1.28imes--11.35imes for committee-member computation, while reducing communication overhead by approximately 76.83%--94.01% for clients, 64.47%--89.40% for the server, and 0.30%--78.78% for committee members. Compared with mPVAS, VOSA achieves speedups of approximately 2.78imes, 11.10imes, and 54.78imes for client-side, server-side, and verifier-side computation, respectively, while reducing the server communication overhead by approximately 92%. These results establish a new efficiency and verifiability baseline for one-shot secure aggregation in dynamic FL deployments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3021) | 2026-11-24
