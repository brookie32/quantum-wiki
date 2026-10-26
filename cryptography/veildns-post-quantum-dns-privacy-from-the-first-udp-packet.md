---
title: "VeilDNS: Post-Quantum DNS Privacy from the First UDP Packet"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2629"
summary: "DNS was designed around UDP, and most DNS traffic today still follows that design: one query, one response, and no handshake. This makes DNS fast and scalable, but exposes client queries in cleartext."
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

DNS was designed around UDP, and most DNS traffic today still follows that design: one query, one response, and no handshake. This makes DNS fast and scalable, but exposes client queries in cleartext. DoT, DoH, and DoQ provide privacy by encrypting DNS messages with TLS. This works once TLS/TCP or QUIC handshakes complete, but cold sessions spend extra round trips and CPU before the first private query can be sent—a cost that grows with post-quantum cryptography. We present VeilDNS, a DNS-native protocol that uses a post-quantum KEM and AEAD to encrypt DNS questions and answers and authenticate the resolver in a single UDP exchange. Given an authenticated resolver KEM key, clients have query privacy from their first UDP packet. VeilDNS supports stateless and stateful modes—the latter reducing recurring computation and bandwidth. An optional mode provides forward secrecy from the second query onward. By preserving the DNS wire format, VeilDNS runs on the standard UDP port 53. Compared with ML-DSA-authenticated Do(T/H/Q) on the well-provisioned network profile, VeilDNS's stateless and stateful modes achieve up to 3.5imes higher cold-session throughput, 4.8imes lower average latency, 4.7imes lower CPU time, 13.7imes fewer bytes, and 15.8imes fewer packets. On the constrained profile, the throughput gain reaches 12.4imes. Tamarin establishes query confidentiality, response authentication, and forward secrecy.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2629) | 2026-10-24
