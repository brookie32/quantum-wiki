---
title: "UdMAC: Efficiently Updatable Message Authentication Codes"
date: "2026-08-25"
updated: "2026-08-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1796"
summary: "Message authentication codes (MAC) are ubiquitous and are considered to be the most important tool employed to ensure authenticity of messages in the symmetric key setting. In this work, we aim to emp"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

Message authentication codes (MAC) are ubiquitous and are considered to be the most important tool employed to ensure authenticity of messages in the symmetric key setting. In this work, we aim to empower MACs with a newly added functionality of updatablility, i.e., the goal is to construct a MAC scheme where the authentication tag for a message can be updated with every update to the message without recomputing the tag for the entire message. Such a functionality can be useful in several scenarios, primarily where the storage of a frequently changing large message is delegated to an un-trusted server. In such a scenario it may be infeasible for an user to download the entire message and recompute the tag for every update. We introduce a new class of MACs called updatable message authentication code (UdMAC), which inherently enjoys the functionality of updates. We systematically develop UdMACs, provide syntax for UdMAC, propose formal security notion. We then present two constructions: mathsf{concatu} and mathsf{xoru}, which support two distinct message updates, namely, concatenation and xor difference. We analyze both the constructions in details and prove security of the construction in the newly proposed security model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1796) | 2026-08-25
