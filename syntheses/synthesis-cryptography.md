---
title: "Synthesis: Cryptography"
date: "2026-09-27"
updated: "2026-09-27"
source: "agent"
category: "syntheses"
tags: [synthesis, cryptography, auto-generated]
url: ""
summary: "Auto-generated synthesis of 771 entries about cryptography"
last_verified: "2026-09-27"
review_by: "2026-09-27"
stale: false
---

# Cryptography: Knowledge Wiki Overview

## Current State
Cryptography is undergoing a fundamental transition driven by the dual pressures of quantum computing threats and AI-enabled attacks. The field is rapidly migrating from classical public-key infrastructure toward post-quantum cryptographic standards, while simultaneously grappling with new attack surfaces in hardware, software supply chains, and public infrastructure. Enterprise adoption of quantum-safe systems is accelerating, with measurable commercial momentum.

---

## Key Developments
- **Post-quantum migration** is moving from research to production, with hybrid key establishment mechanisms (combining classical and PQC algorithms) being deployed on embedded devices
- **Side-channel attacks** on established primitives (SHA-256, HMAC) remain active threats, with bit-level analytical techniques exposing vulnerabilities in hardware implementations
- **Oblivious quantum computation** (OQRAM) is emerging as a framework for securing delegated quantum queries against untrusted servers
- **DNS/credential attacks** on public Wi-Fi infrastructure highlight persistent weaknesses in applied cryptographic deployments
- **Formal verification** of cryptographic primitives (polynomial commitments, KZG schemes) is gaining traction using proof assistants like Isabelle/HOL
- **Lightweight cipher vulnerabilities** (e.g., DIZY stream cipher) remain a concern for resource-constrained IoT devices

---

## Key Players & Organizations
- **NSA** – historical and ongoing role in cryptanalysis and standards influence
- **Keyfactor** – enterprise PKI and post-quantum migration platform ($200M+ ARR)
- **IBM** – foundational cryptanalysis hardware; ongoing quantum research
- **Academic/arXiv community** – primary driver of PQC algorithm research and formal verification

---

## Outlook
Post-quantum cryptography will become the dominant enterprise standard within 3–5 years, driven by regulatory pressure and quantum computing milestones. Side-channel and AI-assisted cryptanalysis will intensify, making formal verification and hardware-level security increasingly critical. Quantum-delegated computation security is an emerging frontier requiring new cryptographic primitives.

## Source Entries

- [[how-candidates-could-use-ai-for-good|How Candidates Could Use AI for Good]]
- [[hacking-public-wi-fi-dns-to-steal-credentials|Hacking Public Wi-Fi DNS to Steal Credentials]]
- [[oqram-oblivious-quantum-random-access-memory-for-securing-de|OQRAM: Oblivious Quantum Random Access Memory for Securing Delegated Quantum Queries]]
- [[on-the-nsas-supercomputer-from-the-1960s|On the NSA’s Supercomputer from the 1960s]]
- [[friday-squid-blogging-neon-flying-squid|Friday Squid Blogging: Neon Flying Squid]]
- [[keyfactor-surpasses-200-million-arr-amid-enterprise-post-qua|Keyfactor Surpasses $200 Million ARR Amid Enterprise Post-Quantum Migration Surge]]
- [[cryptanalysis-of-the-dizy-stream-cipher-with-provable-securi|Cryptanalysis of the DIZY Stream Cipher with Provable Security]]
- [[soft-analytical-side-channel-attacks-on-sha-2-and-hmac|Soft Analytical Side-Channel Attacks on SHA-2 and HMAC]]
- [[transcript-bound-combiners-for-downgrade-resilient-hybrid-po|Transcript-Bound Combiners for Downgrade-Resilient Hybrid Post-Quantum Key Establishment: Definition, Proof, and Embedded-Device Cost]]
- [[efficient-additive-randomized-encodings-for-string-oblivious|Efficient Additive Randomized Encodings for String Oblivious Transfer: A Core Primitive for General Functions]]
- [[on-the-formal-verification-of-polynomial-commitments-two-kzg|On the Formal Verification of Polynomial Commitments: two KZG constructions and the Algebraic Group Model]]
- [[chasing-quoccas-in-a-quantum-world-type-2-oracles-for-cca-se|Chasing QuOCCAs in a Quantum World: Type-2 Oracles for CCA-Secure PKE]]
- [[verification-meets-calibration-bounds-and-secret-independent|Verification Meets Calibration: Bounds and Secret-Independent State Preparation with an NV-Center as a Case Study]]
- [[one-more-a-sharper-tails-without-scaling|One More A: Sharper Tails Without Scaling]]
- [[ai-coding-agents-are-installing-unknownuntrusted-code-on-cor|AI Coding Agents Are Installing Unknown/Untrusted Code on Corporate Networks]]
