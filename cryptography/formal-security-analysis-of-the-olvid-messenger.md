---
title: "Formal Security Analysis of the Olvid Messenger"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1622"
summary: "We perform the first formal security analysis of the cryptographic core of Olvid, an end-to-end encrypted messaging app notably used by French government officials, including ministers. Despite its de"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

We perform the first formal security analysis of the cryptographic core of Olvid, an end-to-end encrypted messaging app notably used by French government officials, including ministers. Despite its deployment in sensitive contexts and its role in critical communications infrastructure, Olvid's cryptographic security has received little independent analysis. To address this gap, we develop detailed models of Olvid's authenticated key exchange and continuous key agreement protocols. We formally verify that our protocol models achieve security properties such as mutual authentication, session-key secrecy, forward secrecy, and replay protection, under an active Dolev-Yao network adversary model that can compromise parties. While we constructively prove that the protocol design meets core security guarantees, our analysis also reveals that, contrary to its claims, the protocol does not meet strong modern security properties that are met by other state-of-the-art secure-messaging protocols, such as Signal. For example, we show in our formal analysis that Olvid is not secure in modern security models such as eCK. Along the way, we uncover a potential timing leakage, and discuss Olvid's anonymity claims.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1622) | 2026-08-05
