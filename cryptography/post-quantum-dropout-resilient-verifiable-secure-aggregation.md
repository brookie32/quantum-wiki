---
title: "Post-Quantum Dropout-Resilient Verifiable Secure Aggregation for Federated Learning"
date: "2026-10-07"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2394"
summary: "Secure weighted aggregation is essential for privacy preserving federated learning, yet existing schemes do not simultaneously provide post-quantum security, resilience to client dropouts, verifiabili"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

Secure weighted aggregation is essential for privacy preserving federated learning, yet existing schemes do not simultaneously provide post-quantum security, resilience to client dropouts, verifiability against malicious servers, and resistance to bounded collusion between the server and clients. This paper presents PQ-DVSA, a verifiable secure aggregation scheme that provides post-quantum security and resilience to client dropouts. PQ-DVSA protects both clients’ updated local models and aggregation weights, enables reconstruction of the aggregate mask for the active set after client dropouts, and allows clients to verify the server’s aggregation result under bounded collusion. Experimental results show that PQ-DVSA achieves learning performance comparable to exact weighted aggregation and reduces the runtime for encrypted submission at each client by up to 96% compared with SWAS, the closest existing scheme to PQ-DVSA.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2394) | 2026-10-07
