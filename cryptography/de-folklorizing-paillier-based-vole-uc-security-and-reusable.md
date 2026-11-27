---
title: "De-Folklorizing Paillier-Based VOLE: UC Security and Reusable Keys"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3029"
summary: "Vector Oblivious Linear Evaluation (VOLE) is a fundamental building block underlying secure computation protocols. Protocols for threshold ECDSA and related applications commonly employ 'folkloric' or"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Vector Oblivious Linear Evaluation (VOLE) is a fundamental building block underlying secure computation protocols. Protocols for threshold ECDSA and related applications commonly employ "folkloric" or implicit OLE-like constructions based on Paillier encryption. Although these embedded techniques are used to secure substantial value in the blockchain ecosystem, they lack standalone, context-independent security proofs, preventing their principled use as general-purpose composable building blocks. The practical risk of relying on such components without standalone analyses is illustrated by key-extraction vulnerabilities discovered in more than ten deployed wallets and libraries. In this work, we "de-folklorize" this common approach. We present a two-message Paillier-based VOLE protocol that achieves two central goals: -- We prove its security within the UC framework based on standard cryptographic assumptions. Although the core of Paillier-based OLE follows readily from additive homomorphism, obtaining a standalone UC-secure realization requires resolving nontrivial challenges arising from maliciously generated long-lived keys, the mismatch between Paillier plaintext arithmetic and VOLE's field arithmetic, and the concurrent reuse of shared setup state. -- We address a critical deployment challenge by introducing explicit support for key reusability. We separate the protocol and its ideal functionality into an initialization phase and a subsequent repeatable execution phase. A single Paillier key can then be securely reused across any polynomial number of concurrent executions and across multiple clients, each of which receives and verifies a one-message, client-specific setup. Consequently, a server supporting M clients maintains just one persistent Paillier secret-key state. Finally, we validate our protocol through an experimental evaluation. Although our protocol has lower computational throughput than the state-of-the-art OT-based approach, it remains bandwidth-competitive and offers a significant deployment advantage: whereas the OT-based approach requires pairwise initialization and management of M independent dynamic states for M clients, our protocol requires only one persistent server key state, substantially simplifying state management in modern client-server architectures.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3029) | 2026-11-24
