---
title: "Oblivious Signaling"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1975"
summary: "An anonymous messaging service has to solve a basic routing problem: a server must deliver an encrypted message to its recipient without learning who the recipient is. Broadcasting all ciphertexts hid"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

An anonymous messaging service has to solve a basic routing problem: a server must deliver an encrypted message to its recipient without learning who the recipient is. Broadcasting all ciphertexts hides the destination but forces every recipient to constantly scan for new messages. Oblivious Message Retrieval (OMR; CRYPTO~'22) tackles this by using fully homomorphic encryption (FHE) to let an untrusted server perform message retrieval on a recipient's behalf without learning which messages are pertinent. We introduce Oblivious Signaling, which shifts this cost from retrieval to sending. The server maintains a fixed-size encrypted inbox for each recipient. When a sender submits a message, the server applies the same homomorphic update to every inbox: the intended inbox absorbs the message, and the rest remain unchanged at the plaintext level. The update is uniform, can be parallelized across inboxes, and ties the delivery cost strictly to the size of the anonymity set rather than global traffic. Recipients retrieve by fetching and decrypting their inbox, so checking for new messages is independent of the global traffic. We formalize receiver privacy against an untrusted server, even when it colludes with other users, give a concrete construction based on fully homomorphic encryption, and analyze the resulting "digital postage'' trade-off: delivery is expensive, but checking is cheap. Our prototype identifies practical regimes in which this cost-model shift is preferable to scan-based retrieval, even with highly optimized OMR implementations. This cost model is well-suited to settings where recipients check frequently, and messages arrive sporadically, and it naturally discourages high-volume spam.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1975) | 2026-09-11
