---
title: "Seven Bindings: A Machine-Checked Map of the Assumptions Behind Lightning's BOLT 12"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2038"
summary: "Lightning's BOLT 12 (offers, onion messages, blinded paths) is the largest addition to the Lightning protocol suite, and it is rolling out now. The specification changed three times in 2026, the commu"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Lightning's BOLT 12 (offers, onion messages, blinded paths) is the largest addition to the Lightning protocol suite, and it is rolling out now. The specification changed three times in 2026, the community is actively debating its privacy posture, and its newest mechanism, Payer Proofs, landed in July 2026 without any analysis. We give the offer family its first formal treatment, covering the full lifecycle from request to receipt, pinned to specification commits e20a924/1528972 and machine-checked in twenty-two ProVerif models that each converge within seconds. The results read as a map rather than a checklist: the family's privacy and integrity rest on seven bindings, removable assumptions whose removal consequences we check row by row. Receiver anonymity and payer-payee unlinkability hold under unbounded sessions and corrupted path nodes, and every protocol-level attack we exhibit lands on an assumption the specification already leans on out-of-band. The map's structure is itself the finding. The blinding key chain, designed for unlinkability, authenticates recipient-side transit for free, while the payer side's delivery binding rests on implementation discipline alone. The newest part of the specification, its payment receipts, turns out to hide a precise disclosure boundary. We close with six testable recommendations for the BOLTs repository.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2038) | 2026-09-15
