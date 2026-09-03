---
title: "Distributed Key Generation for NTRU"
date: "2026-09-01"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1854"
summary: "NTRU-based encryption enjoys compact keys and ciphertexts and admits non-interactive distributed decryption, making it an attractive basis for threshold encryption with applications to threshold FHE, "
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

NTRU-based encryption enjoys compact keys and ciphertexts and admits non-interactive distributed decryption, making it an attractive basis for threshold encryption with applications to threshold FHE, threshold signatures, and electronic voting. All known protocols, however, assume a secret key shared by a trusted dealer. The public NTRU key h = f^{-1}g is a nonlinear function of the secret, so distributed key generation (DKG) techniques for LWE-based schemes do not apply, and generic MPC is prohibitively expensive. We present the first dedicated DKG protocol for NTRU. Each party publishes an NTRU sample, defining a joint public key whose secret key is shared multiplicatively, and a multiplicative-to-additive (MtA) conversion yields the additive sharing required for non-interactive decryption. The protocol runs in few rounds and is actively secure with abort. At the heart of our DKG lies the MtA conversion, for which we give two efficient lattice-based certified constructions; one from additively homomorphic NTRU encryption and one from homomorphic secret sharing, both of which may be of independent interest. We demonstrate the protocol by building a threshold variant of NTRU-Encrypt, which we prove secure and instantiate with concrete parameters.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1854) | 2026-09-01
