---
title: "Automated Reasoning for Indistinguishability in the CCSA"
date: "2026-09-01"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1853"
summary: "Cryptographic protocols are the foundation of secure digital communication, yet their design remains error-prone, as evidenced by the vulnerabilities that have plagued even the most widely adopted pro"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

Cryptographic protocols are the foundation of secure digital communication, yet their design remains error-prone, as evidenced by the vulnerabilities that have plagued even the most widely adopted protocols throughout history. Security properties are typically formalized using either trace properties or indistinguishability, each addressing distinct security guarantees, such as agreement and authenticity for the former and anonymity and strong secrecy for the latter. Formal verification of cryptographic protocols spans both symbolic and computational models. While symbolic techniques enable automation and scalability, they do not provide computational security guarantees. Computational models, though robust, are harder to formalize and automate. Recent advances, such as the Computationally Complete Symbolic Attacker (CCSA) model and its logic, the Bana-Comon Logic (BC Logic), bridge this gap by supporting both trace properties and indistinguishability. However, despite significant progress in proof assistants, automating indistinguishability remains a challenge due to its combination of unstructured equality theories, complex non-classical calculus, and partially inductive reasoning—all requiring expert knowledge in both cryptography and logic. This paper introduces a novel approach to automate indistinguishability proofs in the CCSA model, implemented in the automated prover CryptoVampire2. We extend CryptoVampire to support indistinguishability by designing golgge, a Prolog-inspired backtracking engine over equality graphs (e-graphs), which provides strong, rewrite-driven equational reasoning capabilities. We adapt the BC Logic rules to this new framework, yielding semantically compatible statements. The effectiveness of our approach is demonstrated by automating all indistinguishability goals in the Squirrel repository.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1853) | 2026-09-01
