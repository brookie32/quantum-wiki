---
title: "Identify Post-Quantum Cryptographic Algorithms for Automotive Security: Performance-Driven Guidance for Secure Boot, OTA, and V2X Communication"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2149"
summary: "The rapid expansion of quantum computing threatens the security foundations of classical public-key cryptography, including RSA and ECC, both vulnerable to Shor's algorithm. For the automotive industr"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

The rapid expansion of quantum computing threatens the security foundations of classical public-key cryptography, including RSA and ECC, both vulnerable to Shor's algorithm. For the automotive industry, where secure communication underpins critical functions such as over-the-air (OTA) updates, secure boot, firmware signing, PKI validation, and vehicle-to-everything (V2X) connectivity, this threat demands early and informed migration planning. This paper presents a cross-platform performance evaluation of NIST-selected and candidate Post-Quantum Cryptography (PQC) algorithms integrated into the Transport Layer Security (TLS) protocol, in both standalone and hybrid (classical + PQC) configurations. Signature schemes CROSS, MAYO, SPHINCS+ (SHA and SHAKE variants), ML-DSA, and FALCON are evaluated alongside key encapsulation mechanisms including FrodoKEM, BIKE, and ML-KEM. Testing spans two representative platforms: a resource-constrained Raspberry Pi 4B (Broadcom BCM2711, 4GB RAM) representing embedded automotive ECUs, and an Ubuntu-based Intel Core i5 system representing backend or gateway infrastructure. Execution time, memory consumption, and CPU core utilization are measured across algorithm-KEM combinations to characterize real-world feasibility. Results indicate lattice-based schemes offer a strong balance of performance, interoperability, and long-term assurance suited to V2X and PKI-heavy communication, while compact signature schemes such as MAYO and FALCON better serve resource-constrained operations like secure boot and firmware signing, where verification speed and low memory footprint are prioritized over frequent key exchange. The study further identifies a critical dependency of PQC feasibility on 64-bit architecture, highlighting the limitations of legacy 32-bit automotive chipsets that lack dedicated cryptographic accelerators. These findings offer practical, use-case-specific guidance for automotive OEMs and suppliers navigating the transition from classical to quantum-resistant cryptography, supporting risk-informed decisions across onboard and offboard vehicle communication architectures.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2149) | 2026-09-22
