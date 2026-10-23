---
title: "Compromised TLS Certificates"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "cryptography"
tags: [cryptography, schneier-on-security]
url: "https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html"
summary: "The Indian CA eMudhra Limited has eight TLS certificates with laughably weak private keys: The compromised eMudhra keys were defective at a level that’s challenging the imagination of many of the engi"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

The Indian CA eMudhra Limited has eight TLS certificates with laughably weak private keys: The compromised eMudhra keys were defective at a level that’s challenging the imagination of many of the engineers studying the incident. A normal size for a NIST P-384 elliptic curve cryptography private key contains roughly 384 bits of entropy, a size allowing almost 2384, or a number with 116 digits, different possibilities. The private key sizes of the compromised keys ranged from 3 to 8 bits. Astonishingly, the private keys were 4, 56, 66, 115, 155, 156, 230, 237...

**Source:** [Schneier on Security](https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html) | 2026-10-23
