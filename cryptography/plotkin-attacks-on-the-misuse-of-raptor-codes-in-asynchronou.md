---
title: "Plotkin Attacks! On the (Mis)use of Raptor Codes in Asynchronous Verifiable Information Dispersal"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2338"
summary: "Some asynchronous verifiable information dispersal (AVID) and data-availability protocols certify that a disperser's message is available once 2f+1 of n=3f+1 parties, at most f of them Byzantine, atte"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Some asynchronous verifiable information dispersal (AVID) and data-availability protocols certify that a disperser's message is available once 2f+1 of n=3f+1 parties, at most f of them Byzantine, attest that they hold their erasure-coded fragments, and defer reconstruction and validation of the encoding until later. We call this design pattern reconstruct-later AVID. If the f Byzantine attesters later withhold their fragments, reconstruction must succeed from the f+1 honest fragments that remain, and a Byzantine disperser chooses which f+1 after seeing the encoding symbols assigned to the honest parties. We call a subset of fragments that does not determine the message bad. Raptor codes are a tempting choice here: with modest coding overhead they have very small decoding-failure probability under random erasures, and a preliminary Walrus design and an earlier Walrus testnet used RaptorQ in this way. We show that the pattern is insecure with the standardized Raptor codes R10 (RFC 5053) and RaptorQ (RFC 6330). For a message of K input symbols, every assignment of R10 encoding symbols to the honest parties contains a bad (f+1)-subset whenever K>lfloorlog_2(2f+2)rfloor, and every RaptorQ assignment whenever K>7H_{HDPC}+lfloorlog_2(2f+2)rfloor, where H_{HDPC} is RFC 6330's number of high-density parity-check symbols. Under slightly stronger conditions, randomized polynomial-time algorithms find such subsets, and an implementation of the RaptorQ attack defeats an RFC 6330 decoder on every adversarial subset tested. The key ingredient is the Plotkin bound, which forces a nonzero input whose encoded image has low Hamming weight. For RaptorQ at n=3f+1, an empirical attack over F_{256} succeeds at every tested f from 9 to 45 with K=f+1, far below the f=77 at which the bound above first applies, and empirical attacks over F_4, F_{16}, and F_{256} succeed at values of K well below that bound. For R10, a smaller K does not help: for every standardized 34le Kle8192 and every n with 3f+1le nle4fle65520, explicit certificates give a bad subset for every assignment to the honest parties when the encoding-symbol identifiers (ESIs) are 0,1,ldots,n-1, and with probability at least 1/2 when the ESIs are uniformly random. Benchmarks of our implementations show that the MDS alternative costs little: in our parameter regime, Reed-Solomon is often faster than, and never more than a small constant factor slower than, either R10 or RaptorQ, for both encoding and decoding.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2338) | 2026-10-04
