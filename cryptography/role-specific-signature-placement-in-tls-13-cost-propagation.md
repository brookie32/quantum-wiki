---
title: "Role-Specific Signature Placement in TLS 1.3: Cost Propagation and PQC Migration"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2344"
summary: "Certificate issuance and per-connection signing impose different costs in TLS 1.3, and authentication cost can change depending on how signature algorithms are assigned to Root, Intermediate, and Leaf"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Certificate issuance and per-connection signing impose different costs in TLS 1.3, and authentication cost can change depending on how signature algorithms are assigned to Root, Intermediate, and Leaf roles. PQC migration should therefore consider not only algorithm performance, but also role placement, certificate structure, network conditions, and server load. We evaluate all 13³ role placements formed by 13 signature parameter sets while holding the algorithm composition fixed and changing only the role order. The evaluation covers cryptographic operations, certificate issuance, path validation, TLS authentication, mixed traditional–PQC chains, network profiles, session resumption, and concurrent load. Across 286 groups containing three distinct algorithms, the median maximum/minimum ratios are 2.085 for TLS latency, 4.310 for Certificate body size, and 4.551 for path validation. Thus, role placement alone can produce about a two-fold difference in TLS latency and more than four-fold differences in certificate size and path-validation cost. Direct Root–Intermediate swaps yield a median TLS ratio of 1.003, whereas swaps involving the Leaf yield 1.775–1.788, indicating a stronger influence of Leaf placement. In eight ML-DSA-65/SLH-DSA-SHAKE-192s placements, two candidates remain nondominated when only the Certificate message is considered, but only one remains when the Leaf signature in CertificateVerify is included. This shows that certificate size alone may not represent the transmission cost of the full TLS authentication path. PQC certificate-chain design should therefore consider role-specific computation and transmission costs under the intended network and load conditions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2344) | 2026-10-05
