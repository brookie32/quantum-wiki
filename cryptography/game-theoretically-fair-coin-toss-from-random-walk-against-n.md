---
title: "Game-Theoretically Fair Coin Toss from Random Walk Against n-1 Corruptions"
date: "2026-10-07"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2405"
summary: "Coin-tossing protocols allow mutually distrustful parties to generate trusted randomness. While strong fairness is impossible against a corrupted majority, Chung et al. (2018) introduced cooperative-s"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

Coin-tossing protocols allow mutually distrustful parties to generate trusted randomness. While strong fairness is impossible against a corrupted majority, Chung et al. (2018) introduced cooperative-strategy-proof (CSP) fairness for multi-party coin tossing, under the assumption that each party gets utility only when the outcome matches its public preference. CSP-fairness ensures that no PPT adversary can increase the expected joint utility of the corrupted parties through deviation. Since then, a line of work (Wu et al., 2022; Thyagarajan et al., 2024; Zhang and Wu, 2025) has explored the landscape of CSP-fair coin tossing and shown that CSP-fairness can be achieved even against a corrupted majority. In this work, we study CSP-fair multi-sided coin tossing against up to n-1 corruptions when parties may have arbitrary utilities over the possible outcomes. Perhaps surprisingly, we show that CSP-fairness against any semi-malicious adversary corrupting up to n-1 parties is achievable for every full-row-rank utility matrix. More generally, we introduce an abort-safe opening order condition on the utility matrix that suffices for resilience against n-1 corruptions. Our construction uses a public random walk whose state dynamically determines the distribution of the eventual outcome. The parties jointly generate randomness deciding each walk step using commit-and-reveal. When a party aborts, the protocol adjusts the transition distribution of the walk based on the parties' utilities. These adjustments, together with a carefully chosen opening order, prevent profitable deviations. We also identify conditions on the utility matrix under which CSP-fair coin tossing is impossible. For three parties, our positive and negative results together give a complete characterization of the utility matrices for which CSP-fairness against two corruptions is achievable.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2405) | 2026-10-07
