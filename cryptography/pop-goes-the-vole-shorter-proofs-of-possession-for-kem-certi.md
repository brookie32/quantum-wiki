---
title: "PoP! Goes the VOLE: Shorter Proofs of Possession for KEM Certificates"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2375"
summary: "The shift to Post-Quantum Cryptography (PQC, a.k.a. quantum-resistant cryptography) is considered the immediate solution to the threat posed to public key cryptography/PKI by quantum computers. Due to"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

The shift to Post-Quantum Cryptography (PQC, a.k.a. quantum-resistant cryptography) is considered the immediate solution to the threat posed to public key cryptography/PKI by quantum computers. Due to the variety of PQC algorithms (and their characteristics), researchers have proposed different PQC migration strategies. For example, KEMTLS (Schwabe, Stebila, and Wiggers, CCS '20) replaces TLS handshake signing operations by Key Encapsulation Mechanisms (KEMs). However, KEMTLS requires KEM-based certificates (i.e., a certificate with a KEM public key), and the question of issuing KEM certificates on a large scale has received limited attention from the community. We address this research gap by comparing the performance of different Proof of Possession (PoP) approaches for KEMs and assessing their viability for practical adoption. To this end, we first propose and implement a non-interactive PoP for Hamming Quasi-Cyclic (HQC), a code-based post-quantum KEM selected by NIST for standardization. Our PoP is instantiated via the VOLE-in-the-Head (VOLEitH) paradigm. %VOLEitH is based on Vector Oblivious Linear Evaluation (VOLE). Setting, reproducibility, and practicality as design goals, we integrate and benchmark our approach against PoPs for Kyber and FrodoKEM (from Güneysu et al., CCS '22) in the ACME protocol for automatic certificate issuance. Our results show that, in general, Kyber allows faster issuance of KEM certificates but at a cost of losing either compatibility with the protocol (necessitating significant alterations to proposed internet standards) or breaking compatibility/compliance with NIST standards. Notably, our PoP for HQC holds compliance, compatibility, and achieves smaller proof sizes. We also report integration choices and considerations, as well as network traffic analysis stemming from larger (KEM-based) Certificate Signing Requests (CSRs). Our testbed demonstrates the impact of large CSRs by simulating an unstable network. It shows that HQC-PoP's performance is competitive with the fastest options, thanks to its smaller proof sizes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2375) | 2026-10-06
