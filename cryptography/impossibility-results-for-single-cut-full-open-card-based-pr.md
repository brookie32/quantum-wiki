---
title: "Impossibility Results for Single-Cut Full-Open Card-Based Protocols with Any Number of Cards"
date: "2026-11-20"
updated: "2026-11-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2960"
summary: "Card-based protocols are cryptographic protocols using a deck of physical cards instead of electronic computers, where information is encoded into a sequence of face-down cards and decoded by opening "
last_verified: "2026-11-22"
review_by: "2027-02-20"
stale: false
---

Card-based protocols are cryptographic protocols using a deck of physical cards instead of electronic computers, where information is encoded into a sequence of face-down cards and decoded by opening the cards, and random operations are realized by shuffles of cards. In this research area, there are known impossibility results for protocol construction, but most of the existing results (except for one result for a specific function under a non-standard encoding rule) are conditional on the number of cards used in a protocol, i.e., just giving lower bounds for the number of cards. In contrast, in this paper we give impossibility results, unconditional on the number of cards, for some kind of protocols computing wide classes of functions. Technically, our result is given by deepening a recently explored connection between card-based protocols and combinatorics on words. Specifically, we consider card-based protocols with the following two properties: (1) just a single random cut is used as shuffles; (2) an opening operation is used just once, where all cards are opened at the same time. It has been known that an arbitrary function can be computed by slightly relaxing (1) to "a single shuffle" (not necessarily a random cut) or (2) to "a part of cards are opened". As opposed to them, in this paper we prove that for protocols satisfying both (1) and (2), for the case of symmetric Boolean functions and Boolean functions without redundant variables, the currently known protocols are essentially all of the possible cases; for any other function (in the sense of NPN non-equivalence), such a protocol is shown to be impossible regardless of the number of cards. We also partially extend the impossibility result to functions with non-binary outputs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2960) | 2026-11-20
