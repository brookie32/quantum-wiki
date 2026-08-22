---
title: "CAKE-HI - Compact Authenticated Key Exchange Hiding Identities"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1749"
summary: "Modern public-key cryptography is threatened by advances in quantum computing. As a result, there has been a shift towards cryptographic algorithms that can resist attacks by a quantum computer. Howev"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

Modern public-key cryptography is threatened by advances in quantum computing. As a result, there has been a shift towards cryptographic algorithms that can resist attacks by a quantum computer. However, these algorithms use significantly longer keys, and produce larger ciphertexts and digital signatures than their classical counterparts. These bigger sizes pose problems for devices that are bandwidth- and/or power-limited, and wish to establish a secure, quantum resistant communication channel with another device. In order to reduce the overhead of using these algorithms in challenging environments while maintaining security posture, we present Compact Authenticated Key Exchange – Hiding Identities (CAKE-HI). To evaluate our protocol, we compare the key exchange handshake size and computational efficiency of mutual authenticated TLS and CAKE-HI. Measurements show that CAKE-HI significantly reduces the handshake size and the computational overhead of establishing a quantum-secure link. In addition, we formalize and prove security properties about CAKE-HI in the symbolic and computational model using the protocol analysis frameworks Verifpal and CryptoVerif.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1749) | 2026-08-20
