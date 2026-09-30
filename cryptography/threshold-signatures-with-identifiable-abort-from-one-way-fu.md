---
title: "Threshold Signatures with Identifiable Abort from One-way Functions"
date: "2026-09-27"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2238"
summary: "A (T,N)-threshold signature scheme distributes a signing key among N participants so that any T participants can jointly generate a valid signature, while fewer than T cannot. In this work, we first i"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

A (T,N)-threshold signature scheme distributes a signing key among N participants so that any T participants can jointly generate a valid signature, while fewer than T cannot. In this work, we first introduce a threshold one-time signature scheme with identifiable abort based on a variant of Lamport one-time signature and Shamir secret sharing, enabling authorized participants to jointly reconstruct signatures from partial signatures. We then extend the scheme to support multiple messages using multi-layer Merkle trees. One-time signatures introduce specific coordination challenges: participants must agree on both the message and the one-time key index to avoid unsafe key reuse. We address this using a bulletin-board mechanism for consensus. Under this framework, our construction produces signatures with one message from the bulletin board to each signer and one response message from each signer, while the bulletin board may require additional communication to reach agreement. With a simple majority-vote bulletin board, the scheme signs in four rounds. Subject to this coordination constraint, the construction inherits the guarantees of the underlying threshold framework: Universal Composability (UC) unforgeability with identifiable abort, non-UC robustness, and a bulletin-board mechanism that is UC-secure with an honest super-majority and robust when the central aggregator is honest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2238) | 2026-09-27
