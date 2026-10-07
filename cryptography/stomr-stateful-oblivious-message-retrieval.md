---
title: "StOMR: Stateful Oblivious Message Retrieval"
date: "2026-10-06"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2369"
summary: "Oblivious Message Retrieval (OMR) enables recipients to retrieve messages from an untrusted server without revealing which messages correspond to them. OMR is useful for privacy-preserving systems suc"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Oblivious Message Retrieval (OMR) enables recipients to retrieve messages from an untrusted server without revealing which messages correspond to them. OMR is useful for privacy-preserving systems such as anonymous messaging and blockchains. Existing constructions are inherently built in the public-key setting and use Fully Homomorphic Encryption (FHE) to allow a detector to scan a public bulletin board and produce a compact encrypted digest containing only relevant messages. However, this design incurs a major practical limitation: sender-published signals are large (hundreds of kilobytes), leading to significant bandwidth, storage, and on-chain costs. In this work, we explore the efficiency gains achievable by moving to a private, stateful setting, and introduce stateful OMR, a new model in which senders and receivers maintain lightweight private state to enable more efficient anonymous communication. Based on this model, we design StOMR, a protocol that significantly reduces the size of sender signals compared to prior approaches. To support the required shared state, we further introduce an OMR Key Encapsulation Mechanism (OMR-KEM), which allows users to privately establish shared state and instantiate stateful OMR without out-of-band channels. We implement StOMR in C++ and evaluate it against the state-of-the-art systems PerfOMR (USENIX Security '24), SophOMR (USENIX Security '26), and InstantOMR (USENIX Security '26). Our results show that StOMR preserves detector performance while achieving a signal size approximately 550×, 650×, and 178× smaller than PerfOMR, SophOMR, and InstantOMR, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2369) | 2026-10-06
