---
title: "Privacy-Preserving Inclusion Lists"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1582"
summary: "Blockchains aim to provide open access and censorship resistance, but centralization of block production in blockchains like Ethereum undermines these goals. Inclusion List (IL) protocols mitigate thi"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

Blockchains aim to provide open access and censorship resistance, but centralization of block production in blockchains like Ethereum undermines these goals. Inclusion List (IL) protocols mitigate this by requiring block proposers to include transactions selected by an IL committee to enforce the inclusion of transactions that appear to have been censored. However, protecting the confidentiality of individual committee members’ contributions is essential to prevent retaliation and ensure robust censorship resistance. We propose a lightweight, privacy-preserving inclusion list protocol that allows committees to collectively construct transaction lists while hiding individual contributions and ensuring plausible deniability. Our approach builds on multiparty computation (MPC) techniques to achieve strong privacy without relying on heavyweight cryptography or anonymous broadcast channels. We implement two variants of our protocol design: an optimistic version providing malicious security with abort (latency sim 4.0s) for speed, and a robust variant (latency sim 124.7s) for guaranteed output delivery in the presence of a Byzantine threshold of t < n/3 malicious parties.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1582) | 2026-08-03
