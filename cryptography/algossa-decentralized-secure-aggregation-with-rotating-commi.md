---
title: "Alg{Ossa}: Decentralized Secure Aggregation with Rotating Committees and Eventual Delivery"
date: "2026-10-27"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2659"
summary: "Secure aggregation lets clients reveal only an aggregate of their private contributions, supporting a variety of applications, including privacy-preserving sensing, collaborative analytics, and federa"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

Secure aggregation lets clients reveal only an aggregate of their private contributions, supporting a variety of applications, including privacy-preserving sensing, collaborative analytics, and federated learning. Building on the single-server, committee-aided model for one-shot clients used by OPA and Willow~(CRYPTO~'25), we present Ossa, a generic construction with a modular security analysis. Ossa realizes the standard secure aggregation functionality with non-selective abort against a malicious server, but leaves role selection unspecified and provides no delivery guarantee. We therefore present AlgOssa, which integrates Ossa into an Algorand-style consensus backbone in which cryptographic sortition selects fresh potential leaders and verifier committees in each round and refreshes the decryptor committee from finalized chain state at key epochs. AlgOssa further selects the server from among the potential leaders, and we establish an explicit lower bound on the probability that the selected server is honest. Consequently, the probability that a round delivers a non-empty aggregate is bounded below by a positive constant, yielding an eventual delivery guarantee across repeated rounds. This variable delivery cadence fits delay-tolerant statistical sensing and, with persistent buffering and staleness control, buffered asynchronous federated learning. Our generic core supports classical and post-quantum instantiation routes; we evaluate complete local classical rounds and demonstrate the feasibility of the post-quantum route.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2659) | 2026-10-27
