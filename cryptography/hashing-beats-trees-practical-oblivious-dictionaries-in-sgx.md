---
title: "Hashing Beats Trees: Practical Oblivious Dictionaries in SGX"
date: "2026-10-07"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2397"
summary: "Oblivious RAM (ORAM) is a powerful cryptographic primitive that hides both the contents of outsourced data and the access pattern to the data. However, it offers only a restrictive array-based interfa"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

Oblivious RAM (ORAM) is a powerful cryptographic primitive that hides both the contents of outsourced data and the access pattern to the data. However, it offers only a restrictive array-based interface. A principal obstacle to its deployment is building an efficient oblivious dictionary upon it. To build such a dictionary, the state-of-the-art layers an oblivious AVL tree over ORAM, avoids an expensive local position map, but forces every operation to traverse a full root-to-leaf path, costing Theta(log n) ORAM accesses. We show this trade-off to be suboptimal, particularly when deployed in a common setup within a trusted execution environment like SGX. There, a small amount of client memory can reduce the position map recursion depth to three levels or less, rendering its overhead relatively small. With low position map cost, probabilistic hash tables prevail as dictionary data structures due to their small, constant number of accesses compared to Theta(log n) path traversal of a tree. We implement and analyze oblivious, probabilistic hash tables over Path ORAM, including several different strategies: chaining, power-of-two-choices, stash-less cuckoo, and de-amortized cuckoo hashing. Execution of these algorithms within a secure enclave requires "double obliviousness", which in turn needs strict concrete maximum cost limits for each access that current literature does not provide. We derive these concrete padding parameters bounding the hash table rebuild probability to le 2^{-40} via large-scale simulation. In an SGX deployment, our constructions outperform oblivious trees by up to 20imes for mathsf{lookup}s and 12imes for mathsf{insert}s.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2397) | 2026-10-07
