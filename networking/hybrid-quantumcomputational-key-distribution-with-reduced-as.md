---
title: "Hybrid Quantum–Computational Key Distribution with Reduced Assumptions (Short Paper)"
date: "2026-10-13"
updated: "2026-10-14"
source: "agent"
category: "networking"
tags: [networking, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2462"
summary: "The HM-QCT protocol, presented by Mazzoncini et al. in 2025, uses a unique feature of quantum information to achieve quantum key distribution (QKD) with secret-key rates beyond standard constructions."
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

The HM-QCT protocol, presented by Mazzoncini et al. in 2025, uses a unique feature of quantum information to achieve quantum key distribution (QKD) with secret-key rates beyond standard constructions. The protocol has been designed in the hybrid quantum–computational time-lock (QCT) security model which imposes two independent (but related) restrictions on the attacker: (1) a computationally secure encryption scheme which a successful attacker must break within a narrow timeframe and (2) an assumption that the attacker can only store quantum information with low fidelity. We first review the protocol and its two-assumption model by presenting, in explicit form, the two natural “harvest now, decrypt later” strategies against it, one using quantum memory and one using classical memory. We show how each is excluded by exactly one of the two assumptions, so that harvesting resistance rests on their conjunction and on the presumed existence of a technological gap: the adversary's quantum memory must decohere much faster than the time it takes to break the short-term encryption. Finally, we introduce HM-PRF, a variant that replaces the short-term encryption with a pseudorandom function (PRF), evaluated locally. By eliminating the transmission of enciphered classical information, the adversary does not need to race an impending expiry event. We compare the security of our construction against the original and argue that our PRF-based assumption yields a more realistic adversary. It simply requires the existence of one-way functions rather than a predicted lasting limitation of quantum computation and memory technology.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2462) | 2026-10-13
