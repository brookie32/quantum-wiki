---
title: "TreeOnion: Efficient Private Retrieval of Tree Paths"
date: "2026-11-20"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2969"
summary: "Private information retrieval (PIR) lets clients retrieve entries from a public database hosted on a server without revealing which entries are retrieved. Traditionally, the database is assumed to be "
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Private information retrieval (PIR) lets clients retrieve entries from a public database hosted on a server without revealing which entries are retrieved. Traditionally, the database is assumed to be an array or a key-value store, and the client has the index or keyword of the entry it wishes to retrieve. However, in practice, the database can have a more complex structure. An important example is when the database is organized as a tree, and the client wants to retrieve all nodes along a root-to-leaf path. Notably, retrieving a Merkle proof is a natural instance of this problem, as is done in applications such as certificate transparency and blockchain systems. We present TreeOnion, a single-server scheme that allows clients to privately retrieve a path of nodes from a public database organized as a tree. For small node sizes, the communication and computation costs of TreeOnion are comparable to the costs of privately retrieving a single node from the same database. Compared with alternate approaches, TreeOnion is strictly better in both communication and computation, and is at least an order of magnitude better in one of the two metrics.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2969) | 2026-11-20
