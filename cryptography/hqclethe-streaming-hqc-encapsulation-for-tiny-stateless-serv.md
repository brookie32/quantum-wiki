---
title: "HqcLethe: Streaming HQC Encapsulation for Tiny Stateless Servers"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2767"
summary: "Stateless post-quantum authenticated key exchanges such as post-quantum WireGuard hedge against unexpected cryptanalytic advances by combining a lattice KEM with code-based Classic McEliece. However, "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Stateless post-quantum authenticated key exchanges such as post-quantum WireGuard hedge against unexpected cryptanalytic advances by combining a lattice KEM with code-based Classic McEliece. However, recent attacks have led Germany's BSI to advise against McEliece, which leaves these protocols with lattices alone. HQC, the code-based KEM that NIST selected, could restore diversity, but its keys do not fit in a single packet, so a server would have to buffer multi-packet handshakes. This would leave an attack surface for memory exhaustion, which is what WireGuard's stateless handshake was designed to avoid in the first place. McTiny demonstrated that stateless key encapsulation for Classic McEliece is possible by streaming key blocks one-at-a-time. However, HQC's encapsulation does not split as easily into individual packets, as cyclic polynomial multiplication, unlike matrix-vector multiplication, is inherently non-local. We present HqcLethe, a stateless key exchange that streams an HQC encapsulation in packet-sized pieces. It uses the Chinese remainder theorem to split the polynomial multiplication into independent remainders, one per packet, and masks them so that they reveal no more than an ordinary HQC ciphertext, which we prove in Rocq with SSProve; we also verify session secrecy, server authentication and forward secrecy in ProVerif. Client puzzles bound CPU exhaustion, and HqcLethe removes memory exhaustion: on a Raspberry Pi 3B+, each worker runs in a fixed 1.2-1.6 MiB. At category 5 it sends 27x fewer bytes and uses 9.0x less server CPU than McTiny, the earlier stateless code-based design.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2767) | 2026-11-04
