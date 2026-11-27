---
title: "Classical Key Agreement with Near-Quadratic Quantum Security"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3057"
summary: "In 1974, Merkle proposed a key exchange protocol where the honest parties make N queries to a random oracle to compute a secret key, while the best attacker needs to make Omega(N^2) queries to recover"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

In 1974, Merkle proposed a key exchange protocol where the honest parties make N queries to a random oracle to compute a secret key, while the best attacker needs to make Omega(N^2) queries to recover the key with constant probability. This protocol was later proved to be optimal by Barak and Mahmoody (Crypto'09). In the quantum setting, Belovs et al. (TQC'17) proved that for any arepsilon>0, there exists a classical protocol with O(N) expected honest queries, for which any quantum eavesdropper making O(N^{1.5-arepsilon}) queries has vanishing key recovery probability. In this paper, we give two families of classical key-establishment protocols in the random oracle query model. The first is a two-message protocol and the second is a three-message protocol with perfect agreement. In both cases the honest parties make widetilde O(N) classical oracle queries, whereas every constant-success quantum eavesdropper needs widetildeOmega(N^2) quantum queries to recover the key. Our result is tight up to logarithmic factors, as the quadratic classical attack of Barak and Mahmoody applies in this setting. The construction combines two levels of hidden sum relations. In the two-message protocol, Alice samples random labels and encodes their bits using masked oracle blocks. A zero is encoded by a uniformly random block, while a one is encoded by a block containing a planted sum relation. Bob decodes a random subset of the labels and publishes their sum. Alice uses her original labels to identify this subset, which becomes their shared key. We also give an efficient implementation with O(Nlog N) honest oracle queries and O(N(log N)^2) combined honest running time, for which recovering the key with constant probability requires Omega(N^{4/3}) quantum queries.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3057) | 2026-11-26
