---
title: "An Input-Fed AES-Round Family for Fixed-Length Hashing"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2314"
summary: "Secure computation often hashes high-entropy fixed-length values in inner loops. A public permutation with terminal Davies--Meyer feed-forward can expose the permutation value when an application appl"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Secure computation often hashes high-entropy fixed-length values in inner loops. A public permutation with terminal Davies--Meyer feed-forward can expose the permutation value when an application applies another feed-forward step. We study an input-fed alternative that injects the input after every AES round. The base construction, H_{128}:{0,1}^{128}o{0,1}^{128}, uses ten full AESENC-style rounds with keys x+c_i and no AES key expansion. Its concrete analysis adapts differential, collision, linear, integral, and meet-in-he-middle (MITM) methods to this shared-input round-key interface. We prove a three-round integral distinguisher and give a five-round anchored MITM attack candidate with estimated time 2^{120}; the remaining results provide reduced-round evidence rather than a proof of random-function behavior. On an AMD Ryzen 9 7950X, measured scalar and eight-lane AES-NI costs are within one percent of fixed-key AES-128; a sixteen-block VAES kernel is 2.3% slower. Two extensions use the same input-fed principle. The tweakable construction H_{128}^{mathsf{tw}} splits a 72-bit public counter into an eight-bit tweak and a 64-bit epoch. One public schedule serves 256 consecutive positions, and consecutive fixed-key AES outputs under a published key supply the epoch schedules. Within one epoch, a pair with different tweaks can cancel at most one complete boundary injection. The construction also admits an exact 256-query two-round integral distinguisher. The wide construction H_{256} maps 256 bits to 256 bits. It uses two AES lanes and adopts the column permutation and round constants of Haraka-256 v2 [KLMR16]. We analyze the differential, integral, collision, slide, rebound, and MITM mechanisms introduced by these extensions. A supporting ideal-permutation analysis shows that affine wrappers with one or two permutation calls fail generically. For three calls with independently uniform public constants, it gives a birthday-order bound when the distinguisher completes its primitive queries before querying the target. Finally, we define checkable punctured vectors and prove a GM-style protocol secure against static semi-honest corruptions in the ideal-OT and random-oracle model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2314) | 2026-10-02
