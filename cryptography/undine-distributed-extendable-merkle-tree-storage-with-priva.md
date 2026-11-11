---
title: "Undine: Distributed Extendable Merkle Tree Storage with Private Retrieval and Efficient Reconfiguration"
date: "2026-11-08"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2834"
summary: "Clients of transparency logs, public-key directories, and shielded blockchain pools require authenticated access to an ever-changing Merkle tree, without storing it in full or revealing which entry th"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Clients of transparency logs, public-key directories, and shielded blockchain pools require authenticated access to an ever-changing Merkle tree, without storing it in full or revealing which entry they open. We seek to distribute storage and query work across independent servers as the data grows and participants join, leave, change their shares, or misbehave. We present Undine, which combines a distributed Merkle tree encoding with private retrieval from independently-maintained fragments. Maintainers can choose and efficiently adjust the size of their stored fragments, to offer a flexible tradeoff against the number of maintainer replies needed for authenticated data reconstruction by clients. Maintainers can also perform authenticated updates and appends, at a write cost of just twice the number of modified Merkle nodes. Undine uses a linear encoding of the Merkle tree nodes to divide evenly the storage and retrieval load across maintainers. This is combined with a private information retrieval (PIR) protocol that operates directly over the linearly-encoded fragments. Undine avoids repeated storage and computation for nodes shared by Merkle paths across records, producing the same PIR replies with work over tree values linear in the filled prefix. Record sizes adapt as the prefix grows to balance query and reply sizes. Clients verify against the Merkle root, without commitments to individual PIR databases. Computational query privacy holds against any coalition. Undine is also secure against selective-failure leakage (i.e., deductions from acceptance), up to the PIR backend's correctness error, given enough timely honest replies, fixed public timing, and no reply-dependent follow-up. We evaluate UndineLog, our append-only implementation of Undine combined with YPIR. On a height-50 sparse Merkle tree with a 4GiB prefix of nonempty 32-byte leaves and a reconstruction threshold of 64, a maintainer replies in 100ms (single-core); a client can process 192 replies from maintainers and reconstruct a verified opening in 380ms, even with 64 corrupted replies. Scaled up to 1TiB and 256 threshold , a maintainer answers in 1.13s. Existing shielded pools can use this service without consensus changes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2834) | 2026-11-08
