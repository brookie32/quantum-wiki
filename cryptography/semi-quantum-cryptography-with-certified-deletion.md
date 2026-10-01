---
title: "Semi-Quantum Cryptography with Certified Deletion"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38915"
summary: "arXiv:2609.38915v1 Announce Type: cross Abstract: Certified deletion allows a client to upload encrypted data to a server as a quantum state, then later request that the server delete their data and d"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38915v1 Announce Type: cross Abstract: Certified deletion allows a client to upload encrypted data to a server as a quantum state, then later request that the server delete their data and detect whether the server complies. If verification passes, then the data on the server will remain hidden even if the decryption key is later leaked. In publicly verifiable certified deletion, the verification key is published so that anyone may check for deletion compliance. In this work, we give a general compiler to publicly verifiable certified deletion that allows the client to initially upload the *quantum* ciphertext using purely *classical* communication, assuming the post-quantum hardness of LWE in the plain model. Our approach can be applied to a wide variety of primitives, including commitments and public-key, attribute-based, identity-based, and fully-homomorphic encryption. Moreover, our constructions allow the client to classically manage the encrypted data beyond just verifying its deletion. The classical client may non-destructively audit the ciphertext via a Proof of No Intrusion to check whether it has been leaked to a third party. The classical client may also retrieve the data while simultaneously verifying its deletion from the server. Thus, they do not have to choose between retrieving the data and protecting it against future key leakage. As our core technical contribution, we give a classical-communication protocol and simulation technique that allows adapting purification-based security arguments for BB84-style states which are prepared through classical interaction. It makes the required purification available in a hybrid experiment, despite the classical transcript uniquely determining the prepared state in a real execution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38915) | 2026-10-01
