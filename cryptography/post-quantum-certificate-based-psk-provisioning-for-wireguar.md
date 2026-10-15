---
title: "Post-Quantum Certificate-Based PSK Provisioning for WireGuard via Mutual TLS, DTLS, and QUIC: Design and Performance Study"
date: "2026-10-14"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2480"
summary: "We present an architecture that provides WireGuard’s resistance against future quantum adversaries. By preserving the core protocol, our approach minimizes deployment effort and adds certificate-based"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

We present an architecture that provides WireGuard’s resistance against future quantum adversaries. By preserving the core protocol, our approach minimizes deployment effort and adds certificate-based identities to WireGuard peers. To achieve Post-Quantum (PQ) resistance, we establish an external mutually authenticated control channel built on the TLS 1.3 handshake and layered on top of TCP, UDP, or QUIC. Its key establishment includes Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM). An auxiliary shared secret is derived from the exported keying material of the resulting session and injected into WireGuard’s native Pre-Shared Key (PSK) interface; this derivation is identical for all three transports. To support scalable deployment, the control channel is authenticated with X.509 certificates issued by a Public Key Infrastructure (PKI), using the Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for PQ certificate signing. We develop a Tamarin model of the composition layer and symbolically analyze the secrecy, binding, and provisioning-order properties of the interface between TLS 1.3 handshake and WireGuard, identifying the critical conditions necessary for secure deployment. Finally, we evaluate the design to quantify handshake latency and CPU time for classical, pure PQ and hybrid key establishment, classical and ML-DSA certificates, and the three transports, comparing it against an existing PQ WireGuard baseline achieving state-of-the-art results.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2480) | 2026-10-14
