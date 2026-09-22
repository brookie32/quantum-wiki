---
title: "United: Shuffle-Free Multiparty PSU via Oblivious  Invertible Sketches"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2132"
summary: "Multiparty Private Set Union (MPSU) allows multiple parties to compute the union of their private sets while revealing no additional information beyond the prescribed output. Existing practical MPSU p"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Multiparty Private Set Union (MPSU) allows multiple parties to compute the union of their private sets while revealing no additional information beyond the prescribed output. Existing practical MPSU protocols typically manipulate individual elements and rely on a distributed shuffle to hide element ownership, introducing an O(n) round-complexity bottleneck. We present United, a shuffle-free MPSU framework based on a new data-structure abstraction, Oblivious Insert-Only Invertible Sketches (OIIS). Rather than anonymizing an element-wise intermediate representation, the parties directly construct a protected symmetric sketch of the union. Conditional oblivious insertion ensures that each distinct union element is inserted exactly once while hiding the insertion condition and modified locations. We provide two realizations of OIIS. Our HE-based construction instantiates OIIS with a standard Invertible Bloom Lookup Table protected by multi-key partially homomorphic encryption, while our MPC-based construction uses additive secret sharing and introduces a new row-local power-sum OIIS technique for efficient conditional insertion. We implement and evaluate both constructions. Across the evaluated configurations, our MPC-based construction achieves up to 3.10imes lower runtime in LAN settings, while our HE-based construction achieves up to 2.73imes lower runtime in WAN settings compared with prior MPSU protocols.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2132) | 2026-09-20
