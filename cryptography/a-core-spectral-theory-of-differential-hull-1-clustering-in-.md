---
title: "A Core-Spectral Theory of Differential Hull 1 Clustering in Nibble SPNs: Improved Differential 2 Distinguishers for CRAFT"
date: "2026-11-21"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2973"
summary: "Differential hull clustering, i.e., the phenomenon that the differential probability of a cipher can exceed its best single trail by many orders of magnitude, has long been observed, but a structural "
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Differential hull clustering, i.e., the phenomenon that the differential probability of a cipher can exceed its best single trail by many orders of magnitude, has long been observed, but a structural explanation of where the clustering comes from has been missing. This paper gives such an explanation for four-bit nibble SPNs: the core-restricted clustering gap is governed by the recurrent cores of the round function, i.e. the irreducible recurrent components of the differential transition. For a core C with k active S-boxes and weighted adjacency matrix T_C of spectral radius ρ, the clustering gap obeys the asymptotic law gap_C(R) = R (µ(C) + log2 ρ) + O(1), where µ(C) is the minimum-mean-cycle weight. A central consequence is that the branch number, the standard diffusion metric, is not sufficient to bound clustering: it controls only the single-trail weight, not the trail multiplicity measured by ρ. We make the energy/entropy split rigorous through the variational principle, which identifies log2 ρ as an entropy term, and we show that for a periodic core the O(1) transient is the discrete Fourier transform of its cyclic classes; two branch-2 layers differ by 12.3 bits of gap while a branch-4 layer clusters less than both. We construct new differential distinguishers on CRAFT in the single-tweak model for 11 to 14 rounds; at each of these round counts, the probability of our distinguisher is, to our knowledge, the highest reported to date. The 11-round distinguisher reduces the data complexity from 2^49.79 to 2^49.559. We also report, to our knowledge, the first single-tweak differentials for 1 to 8 rounds. The theory is implemented in an open, C++-accelerated tool (coretool) that automates core search, spectral analysis and finite-round validation on CRAFT, GIFT-64, PRESENT-80, SKINNY-64 and controlled ablations, yielding actionable design guidelines for hull-resistant linear layers.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2973) | 2026-11-21
