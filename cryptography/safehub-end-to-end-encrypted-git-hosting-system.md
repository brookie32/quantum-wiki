---
title: "SafeHub: End-to-end encrypted Git hosting system"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1748"
summary: "Private repositories remain readable to Git hosts despite transport and at-rest encryption. We present SafeHub, an end-to-end encrypted Git hosting system. It encrypts repository contents and semantic"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

Private repositories remain readable to Git hosts despite transport and at-rest encryption. We present SafeHub, an end-to-end encrypted Git hosting system. It encrypts repository contents and semantic metadata - file names, commit messages, authors, branches, issues, pull requests, and refs - so the host sees only ciphertext, opaque identifiers, lengths, and order. Each repository is a Messaging Layer Security (MLS) group, providing admin-mediated membership, post-compromise healing, and per-invite history windows. Ordinary Git behavior is preserved within each member's window: branches, merges, and blame still work. Forward-only members start from a join shallow snapshot rather than the full past. Confidentiality alone is not enough: Git's hash-linked objects do not protect mutable refs. SafeHub records refs in an encrypted, device-signed, hash-chained manifest that detects rollback against a member's own anchor and host forks when members compare checkpoints; force-pushes require administrator co-signatures. We specify a single ideal functionality F_safehub for the system and prove that SafeHub universally composably realizes it against a malicious server and adaptive member corruptions, in a hybrid model over group key agreement and certification, assuming secure erasure in the quantum random oracle model. Our NIST PQ Category-5 Rust prototype measures full-stack push, pull, fetch, clone, merge, rebase, and force-push on a client-server pair of AWS Graviton4 hosts, together with the epoch rotation and consolidation that Git has no counterpart for. Against Git on its lowest-overhead native transport, wall-clock push runs 1.45x plain Git at a 0.05 MB delta and 0.98x at a 5 MB one, its marginal cost 46.7 ms/MB against Git's 49.3. We compare SafeHub with five other systems - plain Git, git-crypt, git-remote-gcrypt, and a reimplementation of the closest peer - over a single transport, with clients and remotes on separate hosts. The comparison separates designs whose cost follows the edit from designs whose cost follows the whole file. For a fixed 1 KiB edit, with the edited file growing from 10 KiB to 8 MiB, SafeHub's cost per update remains constant at 6.7 kB, because it seals the packfile Git has already built, whereas the systems that encrypt each file individually grow with the file and reach 8.39 and 13.4 MB. On that shared transport SafeHub is the fastest of the six at push, pull, fetch, merge, rebase, and force-push, each constant in history depth, and its stored size matches plain Git to within 0.2%, whereas the per-file encryption used by the other systems costs 13 to 21 times as much. The cost that does not amortize is clone, which grows with sealed history: a host that cannot read a repository cannot repack it.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1748) | 2026-08-20
