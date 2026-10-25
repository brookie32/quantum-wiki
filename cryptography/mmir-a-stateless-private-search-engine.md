---
title: "Mímir: A Stateless Private Search Engine"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2605"
summary: "Private search engines allow a user to retrieve documents from a public database that are similar to a text query. Our cryptographic protocol Mímir employs state-of-the-art homomorphic ciphertext swit"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Private search engines allow a user to retrieve documents from a public database that are similar to a text query. Our cryptographic protocol Mímir employs state-of-the-art homomorphic ciphertext switching techniques to realize the first stateless semantic private search engine for highly dynamic databases. The security of Mímir relies on (Ring) Learning with Errors. Mímir requires no offline communication, and it trades higher but highly parallelizable server computation for low per-query communication. When the database may change between queries, Mímir matches Tiptoe's search quality with 84imes less per-query communication (0.24 MiB). At Tiptoe's per-query communication, it reaches 64% instead of 36% of non-private search quality and is 4.2imes faster (0.87s on a single multithreaded machine). Against PACMANN, Mímir improves search quality from 76% to 81% of non-private with 72% of its per-query communication and a 9.54 MiB instead of 2.68 GiB one-time cost, but is 2.1imes slower. Mímir can achieve 59% of the non-private search quality with 8.13 MiB of per-query communication and 0.77s of total latency. This matches PACMANN's latency at a 7.6imes smaller per-query communication, and outperforms Tiptoe in all three metrics.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2605) | 2026-10-22
