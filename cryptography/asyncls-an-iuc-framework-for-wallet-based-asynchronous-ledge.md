---
title: "AsyncLS: an iUC Framework for Wallet-Based Asynchronous Ledger Services"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2378"
summary: "We define an asynchronous ledger service (mathsf{AsyncLS}) in the IITM-based universal composability (iUC) framework. The wallet-based service exposes a general state machine for a decentralized ledge"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

We define an asynchronous ledger service (mathsf{AsyncLS}) in the IITM-based universal composability (iUC) framework. The wallet-based service exposes a general state machine for a decentralized ledger-based application through registration, reads of committed application state, authenticated submission, and status queries with immutable final results. Each logical request binds the user's authorization to a finalized checkpoint and the applicable execution context. A confirmed outcome identifies the first eligible transaction and records application success or rejection. Strict expiry requires complete processing beyond the eligible height window with no recorded outcome, and certifies that the request has no application effect. We construct a protocol mathbf{Pi}_{mathsf{AsyncLS}} that realizes the ideal service using four components: Wallet, Relay, Adapter, and Replay. The proof separates the service construction from the implementations of Relay and Adapter while preserving ledger, clock, authentication, and setup interactions. We prove realization for the trusted and local implementations under their respective execution and trust assumptions. We use the service to construct an ORDI interactive payment and a parameterized execution layer above transaction ordering. These examples distinguish the ledger interaction protocol from the application state and effects exposed by the service. Each use requires the stated authorization, setup, ledger, clock, authentication, and ledger-effect assumptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2378) | 2026-10-06
