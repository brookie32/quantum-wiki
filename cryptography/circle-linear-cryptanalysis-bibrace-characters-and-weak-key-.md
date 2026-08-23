---
title: "Circle-Linear Cryptanalysis: Bibrace Characters and Weak-Key Linear Distinguishers for CRAFT"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1767"
summary: "Linear cryptanalysis measures the correlation of a cipher with the characters of the group used to define differences. If that group is replaced by a second elementary abelian group structure on the s"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

Linear cryptanalysis measures the correlation of a cipher with the characters of the group used to define differences. If that group is replaced by a second elementary abelian group structure on the same set, here the one coming from a binary bibrace, then the admissible masks are no longer the ordinary scalar products: exactly half of them survive, and the other half are forced to be quadratic. Beyne’s geometric approach develops linear cryptanalysis over an arbitrary finite abelian group, providing a natural framework for this setting. We instantiate it on the group of a particular bibrace and apply it to Craft. Over this group the Midori/Craft S-box has four probability-one relations, forming a small subgroup of the dual which the S-box preserves in both directions. Inside that subgroup a mask propagates deterministically and linearly, so the search for the best trail is a minimum weight codeword problem, which we solve exactly by complete enumeration rather than heuristically. A trail costs correlation, and it restricts the key to a weak-key class. The two are usually derived from the same data. We show that the correct reading, obtained by analysing the diffusion layer and the key addition together rather than separately, gives a class several bits larger than the one obtained cell by cell. One concrete consequence is that Craft’s round constants, whatever their values, impose no restriction at all. On Craft we obtain weak-key distinguishers up to eighteen rounds. At fourteen rounds the squared correlation is 2−44 over a class of 2^108 keys, against 2−62.12 for the designers’ linear hull, which is the best known linear result on the cipher and holds for all keys. On that class we therefore improve the best linear correlation by eighteen bits at equal round count, and we reach four rounds further than the best known linear hull. Both the distinguishers and the weak-key criterion are verified experimentally, with a negative control on random keys.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1767) | 2026-08-21
