---
title: "Tightly Secure and Modular Post-Quantum TLS Handshakes"
date: "2026-11-11"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2864"
summary: "In the post-quantum (PQ) migration of the TLS~1.3 handshake, the classical Diffie--Hellman key exchange is replaced with a post-quantum key encapsulation mechanism (KEM). Furthermore, KEMTLS builds up"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

In the post-quantum (PQ) migration of the TLS~1.3 handshake, the classical Diffie--Hellman key exchange is replaced with a post-quantum key encapsulation mechanism (KEM). Furthermore, KEMTLS builds upon PQ TLS~1.3 by replacing signature-based authentication with KEM-based authentication. However, all existing analyses of PQ TLS~1.3 and KEMTLS incur at least quadratic reduction losses in the number of sessions, and achieving a tightly secure construction remains an open problem. To address this gap, we present the first unified, tight, and modular reduction framework for PQ TLS~1.3 in the standard model and KEMTLS in the random oracle model (ROM). Our framework tightly reduces the security of these protocols to the security of three core components: (i) the MUC-IND-1RCCA or MUC-IND-1CCA security of the underlying ephemeral KEM, (ii) the MU-(dual)-PRF security of HKDF (for PQ~TLS~1.3), and (iii) the MU-EUF-CMA^c security of the signature scheme (for PQ TLS~1.3) or the MUC-OW-ChCCA^* security of the static KEM (for KEMTLS). Furthermore, we establish the first concrete MU-(dual)-PRF bounds for HMAC and HKDF in the quantum-accessible random oracle model (QROM). Instantiating this framework with tightly secure LWE-based KEM and signature schemes yields the first (almost) tightly secure constructions of PQ TLS~1.3 and KEMTLS under the LWE assumption. Moreover, our framework demonstrates that the weaker IND-1RCCA security notion for the ephemeral KEM already suffices to achieve security for both PQ TLS~1.3 and KEMTLS, thereby enabling simpler instantiations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2864) | 2026-11-11
