---
title: "Eavesdropper-Blind Remote State Preparation and Applications to Quantum Public-Key Encryption"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1766"
summary: "Remote state preparation (RSP) is a central primitive in quantum cryptography, enabling classical parties to remotely construct quantum states using only classical communication. As a result, RSP serv"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

Remote state preparation (RSP) is a central primitive in quantum cryptography, enabling classical parties to remotely construct quantum states using only classical communication. As a result, RSP serves as a key building block in numerous protocols involving classical clients and quantum servers, allowing classical parties to leverage the advantages offered by powerful quantum computers. All known constructions of RSP rely on strong cryptographic assumptions, typically variants of trapdoor claw-free functions (TCFs). In this work, we initiate the study of a weaker form of remote state preparation, which we call eavesdropper-blind remote state preparation (EB-RSP). Informally, EB-RSP requires blindness only against external observers who see the transcript of the honest protocol, rather than against the quantum server itself. Despite this relaxed adversarial model, the resulting notion remains sufficient for useful cryptographic applications. In particular, we show that two-message EB-RSP already suffices to construct quantum public-key encryption with classical public keys and quantum ciphertexts. We then construct two-message EB-RSP protocols from specific one-way group actions, yielding a first step toward RSP-type primitives based on assumptions that do not rely on trapdoors. Finally, we observe that existing RSP constructions are likely naturally adaptable to the two-message EB-RSP notion; we demonstrate this explicitly for a concrete TCF-based RSP construction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1766) | 2026-08-21
