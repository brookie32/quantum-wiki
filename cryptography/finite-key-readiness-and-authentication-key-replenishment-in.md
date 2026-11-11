---
title: "Finite-Key Readiness and Authentication-Key Replenishment in QKD-Assisted UAV Edge Computing"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.14461"
summary: "arXiv:2611.14461v1 Announce Type: new Abstract: A service that needs fresh quantum keys must wait for key release, and may be denied it, before protected computation starts. We quantify this cost for "
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.14461v1 Announce Type: new Abstract: A service that needs fresh quantum keys must wait for key release, and may be denied it, before protected computation starts. We quantify this cost for a trusted stationary UAV serving two ground gateways, each obtaining its keys from one finite-key decoy-state BB84 attempt with parameters fixed in advance. A count-level Monte Carlo model, reproduced by a semi-analytic model, links key acceptance to protected upload, computation, and download, including failed attempts and hover energy. At 26~dB effective optical loss, with authentication hashing at its proxy-benchmarked, near-zero cost, fresh keys raise the 95th-percentile completion time of both tasks from 10.37 to 28.65~s; hover energy grows in proportion. The scalar rate models evaluated here miss the deadline limit on the block size. The pulse budget lies in a window bounded below by authentication-key replenishment and above by the deadline; for a fixed source, channel, and acceptance model, the authentication debit shifts the floor, whereas hashing cost does not. At a 35-s deadline the largest tested loss with a non-empty window is 27~dB at 1% misalignment and 22~dB at 2%; at 3% no tested setting has one. Conditional on the assumed acquisition probability, the selected configurations meet this deadline with simultaneous lower confidence bounds of 96.9--97.3% on held-out trials, at 26~dB and at 18--20~dB with 2% misalignment. A high-cost stress reference that charges hashing in full narrows the window and lowers these loss limits to 26 and 20~dB at the reference processing capacity. A small rise in error rate or loss pushes the deadline probability well below its target and drains authentication keys, while the protocol's security parameter is unchanged.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.14461) | 2026-11-11
