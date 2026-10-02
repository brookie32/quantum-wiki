---
title: "One-Way Quantum Symmetric Private Information Retrieval Protocol From A Single Database Server Using NISQ Devices"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02093"
summary: "arXiv:2610.02093v1 Announce Type: new Abstract: Symmetric private information retrieval (SPIR) lets an inquirer obtain one specific bit only, without leaking any information about its index to the dat"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.02093v1 Announce Type: new Abstract: Symmetric private information retrieval (SPIR) lets an inquirer obtain one specific bit only, without leaking any information about its index to the database owner. With a single server, this is impossible for parties with unrestricted quantum power. We show that it becomes possible, with information-theoretic security, when the server and the user hold only noisy intermediate-scale quantum (NISQ) devices without long-term quantum memory and measure each qubit on arrival, while the eavesdropper remains all-powerful; this is a stricter form of the memory restriction of the bounded- and noisy-quantum-storage models. The server sends BB84 states one way; the user discriminates them unambiguously and so knows a random subset of the bits. After a joint random permutation into blocks, the user announces the conclusive locations of one privately chosen block, and the server hashes and takes a random parity of these locations in every block; the permutation makes it exponentially unlikely that one set of locations fits two blocks. We prove secrecy against the eavesdropper, database privacy through an explicit size rule for the announced set, and user privacy against a server who prepares the prescribed BB84 states and announces truthfully, exactly for single photons and up to a small multi-photon term over a tolerated noise channel. The only addition to BB84 equipment is a passive linear-optical measurement with one ancillary mode. For a 10^{4}-bit database and database privacy 10^{-6}, blocks of about a thousand qubits suffice over a tolerated noise channel for a user who applies the prescribed measurement; certifying an arbitrary memoryless user and committing to the permutation need larger auxiliary transmissions, which we quantify with finite keys. Database privacy extends to decoy-state weak coherent pulses, and simulations show that the bound is nearly tight.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02093) | 2026-10-02
