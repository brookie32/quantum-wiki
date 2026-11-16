---
title: "Byzantine Agreement with Signature Tokens"
date: "2026-11-13"
updated: "2026-11-16"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2890"
summary: "We investigate the power and limitations of quantum cryptography in distributed consensus protocols. Specifically, we study the fundamental problem of Byzantine Agreement in partial synchrony, in a se"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

We investigate the power and limitations of quantum cryptography in distributed consensus protocols. Specifically, we study the fundamental problem of Byzantine Agreement in partial synchrony, in a setting in which each party has access to a finite number k of signature tokens. Classically, this problem is solvable only when less than one-third of the parties can be faulty (Dwork, Lynch, Stockmeyer 1988). We prove that protocols with signature tokens can bypass this lower bound by designing a protocol that remains secure against up to a frac{2^{k+1}-1}{2^{k+2}-1}-fraction of faults. In particular, with k=Theta(log n), where n denotes the number of parties, our protocol solves Byzantine Agreement in partial synchrony assuming only an honest majority. Conversely, we prove that Omega(log n) signature tokens are necessary for such a result. Finally, for k=1, we prove that the fault-tolerance threshold of 3/7 achieved by our protocol is the best possible.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2890) | 2026-11-13
