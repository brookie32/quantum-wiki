---
title: "Multi-Reprogramming with Quantum Advice in the Quantum Random Oracle Model"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2140"
summary: "Adaptive reprogramming is a central tool for proving security in the quantum random oracle model (QROM). Recently, it has been extended to the setting when an oracle-dependent advice is in presence. H"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Adaptive reprogramming is a central tool for proving security in the quantum random oracle model (QROM). Recently, it has been extended to the setting when an oracle-dependent advice is in presence. However, the existing result is restricted to classical advice, and addresses only a single reprogramming. Extending it to n reprogrammings through naive hybridization yields a loss that is linear in the number of reprogrammings. In this paper, we establish an adaptive reprogramming theorem that accommodates quantum advice, and has a tighter overall security loss that only scales in the cubic-root of n, with an attack that matches the number of queries required in order to reach constant advantage. Using our reprogramming theorem, we provide improved time-space tradeoff bounds for PRG security of random oracles, and an IND-CPA security proof of salted pseudo one-time pad, in the quantum advice setting. Along the way, we also identify and prove a folklore lemma about indistinguishability of two oracles, which may be of independent interest. As another application, we provide a generic security analysis of Fiat-Shamir and hash-and-sign signature schemes, in QROM with quantum advice. We do so via a two-step modular analysis, where in the first step we perform a generic UF-CMA to UF-NMA reduction using our reprogramming theorem, and in the second step we provide a characterization of when such a scheme satisfies UF-NMA security, which we then use to discuss security of several signature schemes in this model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2140) | 2026-09-21
