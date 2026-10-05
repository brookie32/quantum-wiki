---
title: "Beyond Mosca’s Heuristic: Supported Is Not Protected in Post-Quantum Migration"
date: "2026-10-03"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2318"
summary: "Post-quantum (PQ) migration is usually tracked per asset, with Mosca’s inequality and a share of “migrated” systems. For a flow of sensitive data, the relevant questions are different: is every sessio"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Post-quantum (PQ) migration is usually tracked per asset, with Mosca’s inequality and a share of “migrated” systems. For a flow of sensitive data, the relevant questions are different: is every session that carries it keyed by a quantum-safe secret, what evidence supports that claim, and what can an assessor establish from outside? We propose an assessment method whose unit is the data path and whose verdicts are tied to evidence. Key lineage is an algebra on break dates: a derived key falls when all its inputs fall, and a key falls when any of its copies falls. This covers TLS 1.3 resumption, key transport and keys wrapped several times. A verdict is a pair of strong-Kleene evaluations, one taking claims at face value and one admitting only claims that meet an evidence policy; the reachable pairs form four ordered labels. We characterize what an external probe can establish. A probe of the server decides a hop only if the server enforces PQ or cannot negotiate it; enforcement must be shown by a negative test paired with a positive control; a server that resumes sessions without a fresh key exchange leaves the layer undecided; and behind a load balancer the confidence of a negative test follows a sampling bound only under an independence assumption that a default balancer violates. We implement the probe and validate its inference rules on 22 configurations of five server stacks built on three TLS libraries, including confounders and a heterogeneous load balancer. The same nominal configuration yields different states across implementations, so declared configuration cannot replace runtime evidence. A protocol for an internet-scale enforcement study accompanies the paper

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2318) | 2026-10-03
