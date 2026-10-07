---
title: "Post-Quantum Command Authentication for Unmanned Systems: A KpqC Feasibility Study under Real-Time and Bandwidth Constraints"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2343"
summary: "The command and authentication channels of unmanned systems (UAVs and UGVs) still rely on classical public-key cryptography, which large-scale quantum computers threaten. Migrating these channels to p"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

The command and authentication channels of unmanned systems (UAVs and UGVs) still rely on classical public-key cryptography, which large-scale quantum computers threaten. Migrating these channels to post-quantum cryptography (PQC) is therefore imperative, yet PQC keys and signatures are substantially larger, and sometimes slower, than their classical counterparts, while command links are tightly constrained in message rate, maximum transmission unit (MTU), latency deadline, and bandwidth. Whether a given PQC algorithm fits such a budget, and how to mitigate it when it does not, remains an open and practically important question. This paper studies the application of Korean PQC (KpqC: HAETAE, AIMer, SMAUG-T, NTRU+) to the authentication and key-establishment path of ROS2/DDS-Security, framed as a command-channel size-latency budget problem. We keep KpqC as the subject of study while using the NIST standards (ML-KEM, ML-DSA, SLH-DSA) as a familiar yardstick and classical ECDSA/ECDH as the migration baseline, giving a classical→NIST→KpqC three-way comparison on a single, consistent testbed. We define a feasibility envelope that maps each algorithm to the channel conditions it can meet, and we validate it with authentication-handshake measurements over emulated constrained links on a two-node testbed. Our results yield an application guideline indicating which KpqC candidate is admissible for which command-channel budget.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2343) | 2026-10-05
