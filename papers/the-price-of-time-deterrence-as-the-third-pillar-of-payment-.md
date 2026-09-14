---
title: "The Price of Time: Deterrence as the Third Pillar of Payment Channel Security"
date: "2026-09-13"
updated: "2026-09-14"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2001"
summary: "Safety and liveness are the two classical pillars of payment channel security. Both price attacks that merely occupy channel resources, such as jamming, at zero. We propose a third pillar, deterrence:"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Safety and liveness are the two classical pillars of payment channel security. Both price attacks that merely occupy channel resources, such as jamming, at zero. We propose a third pillar, deterrence: harm carries a provable price. We give its theory for occupied shared-state resources. Within a holding-cost framework, we characterize occupation pricing for lock-resolve channels. Time-dependence in the occupier's liability is necessary for any deterrence: today's time-independent pricing admits unbounded griefing, with damage-to-cost ratios above 10^7. Linear time-proportional liability achieves the tight rate. Its two faces, deadline-proportional upfront fees and hold-proportional penalty bonds, differ exactly in what they charge honest traffic. Our main theorem maps the landscape of four desiderata: deterrence against colluding sinks, penalty-only honesty, zero intermediary lockup, and path privacy. Three of them are jointly unachievable, and every remaining combination is achieved by a matching construction; onion-message fee-swallowing gives a second enforcement instance. Single-channel enforcement is characterized exactly: penalty-only pricing is unilaterally enforceable if and only if scripts expose time. The proof is a three-case exhaustion, and it explains why pre-BIP65 Bitcoin could not support trustless occupation pricing. Our flagship fused-bond construction runs on Bitcoin today, with no covenants, oracles, or miner assumptions; it improves slot-jamming deterrence by eight orders of magnitude at zero net cost to punctual honest payments. For multi-hop payments we prove the forwarding trilemma, settling a 2020 conjecture of the Lightning engineering community, and we quantify the price of privacy, including a new O(1/n) extreme-value side channel on the sender's path length.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2001) | 2026-09-13
