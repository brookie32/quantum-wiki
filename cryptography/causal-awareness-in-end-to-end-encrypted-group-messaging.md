---
title: "Causal Awareness in End-to-End Encrypted Group Messaging"
date: "2026-10-13"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2459"
summary: "Chats do not always unfold in a single clear order. Two users may send messages before information about either message reaches the other sender. Such messages are concurrent, but most instant messeng"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Chats do not always unfold in a single clear order. Two users may send messages before information about either message reaches the other sender. Such messages are concurrent, but most instant messengers provide no way for users to recognize this relationship. Chen and Fischlin (Eurocrypt 2024) studied this limitation in the two-user setting, showing that Signal does not expose enough information to recover the context in which a message was sent; they proposed a fix. We study group chats, where a user may need to reason about ordering and concurrency among other users' messages. This can become a security problem when network delays or adversarial interference cause an authentic message to be shown in a misleading context. Event ordering is a classical problem; Lamport clocks and vector clocks are standard starting points. Secure messaging needs a different treatment because communication is asynchronous, bandwidth is limited, and added latency is undesirable. To address the problem under these constraints, we introduce causal awareness: the ability of a receiver to reconstruct a specified part of the causal context in which an accepted message was sent. Senders transmit records of what they have sent and received. Receivers verify these records and compare them with their own. We develop a framework of correctness and security notions for causal awareness in group chats. Our definitions are parameterized by how much causal information receivers must recover. We give baseline constructions and prove their properties. We also introduce checkpoint-aided and server-aided variants of the framework and prove that, in each, our notions of correctness and integrity imply causal awareness. We discuss how causal information could be surfaced in a messenger's user interface.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2459) | 2026-10-13
