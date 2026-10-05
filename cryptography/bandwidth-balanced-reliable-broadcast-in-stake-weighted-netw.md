---
title: "Bandwidth-Balanced Reliable Broadcast in Stake-Weighted Networks"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2337"
summary: "Consider an asynchronous network of n validators in which Byzantine validators hold less than one third of the stake. In erasure-coded reliable broadcast, validators relay fragments of the sender's me"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Consider an asynchronous network of n validators in which Byzantine validators hold less than one third of the stake. In erasure-coded reliable broadcast, validators relay fragments of the sender's message. A validator's relay-upload cost is the amount of fragment data it transmits outside the sender's initial dispersal. Assigning each validator a number of fragments proportional to its stake makes the heaviest validators relay far more data than the rest. We show that this imbalance is unnecessary. We give Balanced CT and Balanced MiniCast, adaptations of Cachin-Tessaro (CT) and MiniCast (Locher and Shoup, EUROCRYPT 2025) that retain stake-weighted voting but assign one fragment to each validator, giving every honest validator the same relay-upload bound. Their maximum relay-upload costs depend on how few validators can exceed one third of the total stake for CT, or two thirds for MiniCast. Stake skew can amplify MiniCast's advantage beyond the approximately twofold improvement in equal-stake networks. For the real-world Monad distribution with n=200, the leading maximum relay-upload costs, as multiples of the message size, are approximately 72.2 for CT with proportional assignment, 8.7 for Balanced CT, and 2.2 for Balanced MiniCast. The balanced constructions pay for their low maximum cost with a higher total relay-upload cost. To reduce that total while retaining a prescribed maximum-cost bound, we give a new Capped Swiper heuristic. On eight real-world stake distributions, with at most 4n fragments per code, it lowers total relay-upload cost by 19-81% for CT and 16-71% for MiniCast relative to their balanced counterparts, while keeping maximum relay-upload cost at most 10% higher. We also give sender-aware variants of both constructions in which the sender relays no fragment data, reducing its per-broadcast burden.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2337) | 2026-10-04
