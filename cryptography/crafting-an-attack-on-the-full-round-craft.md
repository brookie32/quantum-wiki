---
title: "CRAFTing an Attack on the Full-Round CRAFT"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3024"
summary: "CRAFT is a 64-bit block, 128-bit key tweakable block cipher presented in 2019 by Beierle et al. can be efficiently protected against differential fault attacks. Since its introduction, numerous attack"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

CRAFT is a 64-bit block, 128-bit key tweakable block cipher presented in 2019 by Beierle et al. can be efficiently protected against differential fault attacks. Since its introduction, numerous attacks were presented, where the best one (in number of attacked rounds) can break up to 26 rounds out of the cipher's 32. In this paper, we present the first full-round attack on CRAFT in the single-key model. The attack uses the recently presented (FSE 2026) observation that CRAFT can be decomposed into two parts, with minimal inter-part mixing. We use this property to construct a dissection attack that breaks the full 32-round CRAFT in 2^{121} time and 2^{120} memory, using 3 known plaintexts; an information-theoretic argument suggests that two already suffice. The same attack extends to 36 rounds of CRAFT in 2^{126} time and 2^{124} memory with 3 known plaintexts, and so remains faster than exhaustive search well beyond the specified number of rounds.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3024) | 2026-11-24
