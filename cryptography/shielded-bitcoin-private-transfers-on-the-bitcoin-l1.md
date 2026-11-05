---
title: "Shielded Bitcoin: Private Transfers on the Bitcoin L1"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2749"
summary: "This paper introduces Shielded Bitcoin, a protocol for private transfer of Bitcoin directly on the Bitcoin L1, requiring no changes to Bitcoin consensus. Its design borrows from the architecture of Zc"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

This paper introduces Shielded Bitcoin, a protocol for private transfer of Bitcoin directly on the Bitcoin L1, requiring no changes to Bitcoin consensus. Its design borrows from the architecture of Zcash and earlier shielded-note systems: value is held as encrypted notes, spends are marked by public nullifiers, and validity is established by zero-knowledge proofs. Unlike Zcash, Shielded Bitcoin introduces no dedicated consensus chain: all protocol data is published on Bitcoin, transfer validity is enforced through PIPEs v2 [ACG+26], and shielded state is reconstructed by deterministic replay of accepted transfers in Bitcoin order. At the metaprotocol transfer level, Shielded Bitcoin is non-custodial: spending authority remains with user-controlled wallet keys encrypted in a ciphertext, and neither indexers nor the replay layer receive authority to spend user notes. A shielded transfer does not publicly reveal its amount, sender, receiver, and place in the transfer graph, while keeping the validity of every encrypted state transition publicly verifiable. Shielded state, comprising the note tree, nullifier set, and block-level root history, is maintained entirely off-chain: any two correct implementations replaying the same Bitcoin history derive identical protocol state without coordination. The paper defines the transfer model, note structure, ciphertext-derived note leaves, nullifier rules, transaction binding, replay semantics, and publication assumptions. Peg-in and peg-out, the mechanisms by which value enters and exits the shielded transfer system, belong to the broader system and fall outside the scope of this paper.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2749) | 2026-11-03
