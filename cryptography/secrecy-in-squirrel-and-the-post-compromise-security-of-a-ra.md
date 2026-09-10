---
title: "Secrecy in Squirrel and the Post-Compromise Security of a Ratchet"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1912"
summary: "Ratchets are critical cryptographic protocols deployed in many secure messaging applications such as Signal Messenger, WhatsApp, and Apple's iMessage PQ3, which aim for strong guarantees such as Post-"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Ratchets are critical cryptographic protocols deployed in many secure messaging applications such as Signal Messenger, WhatsApp, and Apple's iMessage PQ3, which aim for strong guarantees such as Post-Compromise Security (PCS). Computer-aided cryptography can be used to increase confidence in security protocols but, until now, has been unable to prove PCS in the computational model for a ratchet due to the complexity of the cryptographic arguments involved. Existing mechanized PCS analyses have been limited to the symbolic model. We tackle this problem with Squirrel, which is well-suited to study such stateful protocols. The task is still a challenge, due to the intricate reasoning required, and because Sqirrel's indirect modeling of secrecy has difficulties in scaling to such a complex proof. To address these issues, we develop a novel logical framework in Squirrel that allows to reason on secrecy as a first-class notion, and we validate our approach by verifying the PCS of an asymmetric ratchet. This provides the first mechanized computational proof of PCS to date for a ratchet, and possibly for any protocol.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1912) | 2026-09-07
