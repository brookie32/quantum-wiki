---
title: "A quantum algorithm for one-shot signatures"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.23612"
summary: "arXiv:2606.23612v2 Announce Type: replace Abstract: We provide a pre-obfuscation circuit-level implementation of an efficient one shot signature scheme, which has known applications to delegated signa"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2606.23612v2 Announce Type: replace Abstract: We provide a pre-obfuscation circuit-level implementation of an efficient one shot signature scheme, which has known applications to delegated signatures, secure token transfer, and publicly verifiable randomness. The algorithm consists of two stages: a key generation stage where a classical public key/quantum secret key pair is produced, and a signing stage where the quantum secret key is processed with a message string to produce a classical signature. There is no algorithmic error in the construction and the signed message can be efficiently checked by a classical verifier. Our scheme works by preparing a superposition over elements of a random affine coset determined by the output of a puncturable pseudorandom function, together with a circuit that tests coset membership. The logical qubit number scales like Theta( kappalog(r) + n + l) and the gate complexity scales like Theta(n^3 + nl), where r is the public key size, n+l is the signature size, l is the message size, and kappa = Omega(n) is the cryptographic security parameter. We provide explicit qubit and gate counts before obfuscation. A secure instantiation additionally requires modified key generation and a security proof for the resulting obfuscated construction.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.23612) | 2026-10-15
