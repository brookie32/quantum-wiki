---
title: "NoisePQC++: A Unified NIST-Compliant PQC and Hybrid-PQC Implementation of the Noise Protocol"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.00954"
summary: "arXiv:2608.00954v1 Announce Type: cross Abstract: The threat of quantum computers to classical public-key cryptography has created an urgent need to evolve secure communication protocols with post-qua"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.00954v1 Announce Type: cross Abstract: The threat of quantum computers to classical public-key cryptography has created an urgent need to evolve secure communication protocols with post-quantum cryptographic (PQC) primitives. The Noise Protocol Framework, widely used in systems such as WireGuard and WhatsApp, traditionally relies on the Elliptic Curve Diffie-Hellman (ECDH) public-key exchange scheme, which is vulnerable to quantum threats. In this paper, we present NoisePQC++, a unified C++23 implementation of the Noise Protocol framework augmented with post-quantum Key Encapsulation Mechanisms and Hybrid Forward Secrecy. Our design integrates the National Institute of Standards and Technology (NIST) standardized ML-KEM algorithm alongside classical ECDH, enabling full PQC, hybrid ECDH+PQC handshakes, and unified support for all 57 classical Noise handshake pattern variants, 13 post-quantum Noise handshakes, and their hybrid variants. Compared with prior work, NoisePQC++ offers broader protocol coverage, more complete implementation support, and greater flexibility. Our evaluation shows minimal overhead under normal network conditions and acceptable overhead in adverse cases, while significantly improving resistance against quantum adversaries. These results indicate that NIST-standardized post-quantum and hybrid Noise handshakes are practical and provide a credible basis for future deployment.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.00954) | 2026-08-04
