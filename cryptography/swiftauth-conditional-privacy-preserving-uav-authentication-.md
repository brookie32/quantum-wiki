---
title: "SwiftAuth: Conditional Privacy-Preserving UAV Authentication with Multi-Source Credential Aggregation and Non-Interactive Authorization"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2503"
summary: "To address the challenges of interactive credential issuance and conditional privacy-preserving authentication for dynamic terminals accessing multiple third-party services, we propose an traceable an"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

To address the challenges of interactive credential issuance and conditional privacy-preserving authentication for dynamic terminals accessing multiple third-party services, we propose an traceable and aggregatable tagged witness signature (TA-TWS). Building upon this scheme, we design an efficient and privacy-preserving anonymous authentication framework, termed SwiftAuth. SwiftAuth decouples the issuer’s authorization phase from the user’s credential acquisition process in traditional anonymous authentication systems by introducing an asynchronous credential distribution mechanism. This allows issuers to generate authorization components even when users are offline, while ensuring that only the designated user can derive the complete access credential. Furthermore, during the authentication phase, SwiftAuth reduces communication and verification overhead in concurrent multi-service access by compressing multiple credentials into a constant-size representation, and supports verifier-side batch verification across users. In addition, it provides conditional privacy by integrating a regulatory trapdoor, ensuring default anonymity for legitimate users while enabling authorities to trace malicious actors upon protocol violations. Finally, we formally prove that the proposed TA-TWS achieves unforgeability and witness hiding. Extensive experiments were conducted on multiple resource-constrained devices, and Aliyun servers, using the MIRACL Core cryptographic library, demonstrate the practicality and efficiency of our approach.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2503) | 2026-10-16
