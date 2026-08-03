---
title: "A Systematic Literature Review on Optimising CRYSTALS-Dilithium (ML-DSA) Performance for IoT Devices via Lightweight Hashing"
date: "2026-08-01"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1576"
summary: "Background: The migration to post-quantum cryptography confronts resource-constrained Internet of Things (IoT) devices with a material performance cost. CRYSTALS-Dilithium, standardised as the Module-"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

Background: The migration to post-quantum cryptography confronts resource-constrained Internet of Things (IoT) devices with a material performance cost. CRYSTALS-Dilithium, standardised as the Module-Lattice-Based Digital Signature Algorithm (ML-DSA) in FIPS 204, fixes the Keccak-based SHAKE functions as its only symmetric primitives, and profiling on embedded platforms identifies hashing as the largest single contributor to the scheme’s software cost. This review synthesises the performance evidence for ML-DSA on constrained platforms, classifies the optimisation strategies pursued in the literature, and tests whether any published work substitutes a standardised lightweight extendable-output function for SHAKE within the scheme. Methods: Following Kitchenham’s guidelines and the PRISMA 2020 statement, we searched IEEE Xplore, the ACM Digital Library, Scopus, and SpringerLink for peer-reviewed studies published from January 2020 onwards, complemented by backward and forward snowballing and by targeted update searches through July 2026. A protocol was prepared in advance of the search. From 115 database records and 22 records identified through other methods, 40 primary studies met the inclusion criteria. Results: On the ARM Cortex-M4, optimised software implementations of Dilithium3 require 10,667 kilocycles on average for signing and 2,321 kilocycles for verification; on the Cortex-M7, Dilithium-2 verification averages 1,429 kilocycles (6.6ms at 216MHz), with signing spanning 1,835 to 16,440 kilocycles due to rejection sampling. Optimisation efforts fall into four categories: hardware acceleration, platform-specific software optimisation, protocol-level adaptation, and optimisation of the incumbent Keccak primitive itself. Architecture-specific Keccak optimisation reduces hashing’s share of Dilithium’s runtime on the Cortex-M4 by only 2.46 to 5.03 percentage points, indicating that the bottleneck largely survives direct attack. Replacing Keccak with Ascon inside the sibling scheme Kyber yields a 24 to 25% cycle reduction and a 2 to 8% memory reduction on the Cortex-M4. No peer-reviewed study applies this substitution to ML-DSA. Conclusions: With FIPS 204 and NIST SP 800-232 both final, the cost of ML-DSA’s primitive choice on constrained platforms is a well-posed and unanswered question on both sides. We specify a per-call-site Dilithium–Ascon evaluation, including its security constraints and non conformance status, as the priority direction for software-only optimisation of post-quantum signatures on IoT devices. Keywords: post-quantum cryptography; ML-DSA; CRYSTALS-Dilithium; Ascon; lightweight cryptography; Internet of Things; systematic literature review

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1576) | 2026-08-01
