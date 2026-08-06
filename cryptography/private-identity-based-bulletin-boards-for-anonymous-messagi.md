---
title: "Private Identity-based Bulletin Boards for Anonymous Messaging and Other Online Services"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1611"
summary: "Secure and anonymous messaging has many compelling use-cases and is becoming increasingly popular. In this paper, we consider it in the context of delay-and-disruption-prone networks, which are charac"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Secure and anonymous messaging has many compelling use-cases and is becoming increasingly popular. In this paper, we consider it in the context of delay-and-disruption-prone networks, which are characterized by handicapped network access, disrupted operation, censorship, and intermittent network outages. With such settings in mind, we define and design a Private Identity-Based Bulletin Board (PIB^3) scheme, which allows users to anonymously post and retrieve messages to and from a distributed database, and supports communication between users without pre-established setup or pre-exchanged keys. Anyone can encrypt a message for an identity and public epoch, such that only the party with the decryption key for that identity can identify, retrieve, and decrypt the message. Against one corrupted non-colluding PIB^3 server, the server learns neither the recipient identity nor the retrieved record indices beyond the leakage explicitly modeled by the scheme: the public epoch, the database size, and the number of retrievals made by the receiver. If retrieval-count privacy is required, retrievals can be padded to a fixed bound. The multi-server construction extends this guarantee to larger server sets, and gives coalition privacy whenever the underlying multi-server PIR scheme is private against the corresponding coalition. Contributions of this work are: (1) formally defining functionality and security requirements for PIB^3-s, (2) defining and constructing a Hierarchical Identity-based Encryption (HIBE) scheme with searchable ciphertexts, which serves as a building block for the proposed PIB^3 scheme and may be of independent interest, (3) designing an efficient PIB^3 scheme that can be realized with ngeq 2 servers based on the HIBE scheme with searchable ciphertexts combined with additional primitives, and (4) implementing a functional PIB^3 prototype which demonstrates practicality of the entire concept and allows us to assess its performance empirically.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1611) | 2026-08-05
