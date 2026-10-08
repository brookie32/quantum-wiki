---
title: "Quantum Time-Lock Puzzles in the Quantum Random Oracle Model"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2387"
summary: "A time-lock puzzle allows a sender to hide a message in a puzzle such that recovering the message requires substantially more sequential computation than the time required to generate the puzzle, even"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

A time-lock puzzle allows a sender to hide a message in a puzzle such that recovering the message requires substantially more sequential computation than the time required to generate the puzzle, even when parallel computation is allowed. Applications of time-lock puzzles include timed-release encryption, sealed-bid auctions, electronic voting, fair contract signing, coin flipping, and Byzantine consensus. However, time-lock puzzles are known to be impossible in the classical random oracle model. To overcome the classical barrier, in this work we consider quantum time-lock puzzles, in which the puzzle itself is a quantum state. Our construction in the quantum random oracle model achieves generation in one oracle round, solving in at most T oracle rounds, and security against polynomial-width quantum adversaries of depth o(T) for every polynomially bounded delay T, resolving an open problem posed by Mahmoody, Moran, and Vadhan (2011).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2387) | 2026-10-06
