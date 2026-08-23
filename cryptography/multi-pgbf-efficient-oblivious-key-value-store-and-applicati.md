---
title: "Multi-PGBF: Efficient Oblivious Key-Value Store and Application to Private Set Intersection"
date: "2026-08-22"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1772"
summary: "An oblivious key-value store is a data structure that can encode and decode n key-value pairs in a table of size m obliviously. After encoding, one cannot distinguish the encoded key-value pairs from "
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

An oblivious key-value store is a data structure that can encode and decode n key-value pairs in a table of size m obliviously. After encoding, one cannot distinguish the encoded key-value pairs from other key-value pairs in the input domain. In this paper, we first propose a data structure called Peelable Garbled Bloom Filter (PGBF), which encodes the key-value pairs in a similar way to peeling and unpeeling an onion. Specifically, it can divide the key-value pair set (i.e., onion) as multiple subsets (i.e., peels) and order them from the outermost peel to the innermost peel by using a counting Bloom filter. However, using a small expansion rate (i.e., eta=m/n) in PGBF will result in a non-empty core issue with non-negligible probability. To handle this issue, we propose Multi-PGBF by combining multiple PGBFs to do the peelings and unpeelings recursively. In addition, we propose a variant C-Multi-PGBF by clustering a large set into small sets to achieve faster encoding efficiency. Our experiments show that Multi-PGBF and C-Multi-PGBF obtain the best encoding and decoding efficiency. Multi-PGBF improves the encoding time of RR (CCS’22) by 65.1%sim 77.6%, while C-Multi-PGBF improves the encoding time of the clustered RR variant by 60.2%sim 64.7%. For decoding, Multi-PGBF is 28.6%sim 62.4% faster than RR (CCS'22) and 89.7%sim 96.3% faster than RB-OKVS (Usenix'23). When integrated into the state-of-the-art two-party and multi-party private set intersection protocols (Eurocrypt'21, Usenix'24), Multi-PGBF and C-Multi-PGBF lead to faster protocols than those using existing OKVS constructions in most settings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1772) | 2026-08-22
