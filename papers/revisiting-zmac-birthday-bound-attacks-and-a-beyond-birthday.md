---
title: "Revisiting ZMAC+: Birthday-Bound Attacks and a Beyond-Birthday-Bound Repair"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2647"
summary: "ZMAC+ is a tweakable-block-cipher-based MAC proposed by List and Nandi in ToSC 2017 with claimed beyond-birthday-bound security. We show that a tag-swap mechanism previously observed for a hypothetica"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

ZMAC+ is a tweakable-block-cipher-based MAC proposed by List and Nandi in ToSC 2017 with claimed beyond-birthday-bound security. We show that a tag-swap mechanism previously observed for a hypothetical two-output extension of DoveMAC also applies to the published ZMAC+ construction. For two-block tags, we give a distinguisher with constant advantage and a fresh-message forgery with constant success probability using O(2^{n/2}) queries in the ideal-TBC model, where n is the block length. An internal collision between two message families exchanges their tag blocks; a common extension preserves this relation and leads to a forgery with one additional authentication query. We identify a counting error in the published Lemma~4 and prove a corrected aggregate differential bound. The resulting PRF and MAC upper bounds match the birthday query threshold for bounded message lengths and two-block tags, under explicit field-order conditions. The distinguisher extends to every legal fixed output length dge2, and the forgery to every legal even d. We also retain ZHash and separate the output domains. Under stated field-order, length, and domain-capacity conditions, this modification admits an adaptive PRF bound of order q^2/2^{n+min(n,t)} for bounded lengths. Finally, a one-query counterexample shows that the ZAE security theorem must retain the per-message length restriction required by its counter-in-tweak encryption component.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2647) | 2026-10-26
