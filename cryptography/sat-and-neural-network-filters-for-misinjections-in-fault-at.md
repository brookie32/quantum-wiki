---
title: "SAT and Neural Network Filters for Misinjections in Fault Attacks"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2537"
summary: "A misinjection, an injection that misses the fault form an attack assumes, can make an elimination fault attack discard the correct key. They occur when the attacker has not determined the timing of t"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

A misinjection, an injection that misses the fault form an attack assumes, can make an elimination fault attack discard the correct key. They occur when the attacker has not determined the timing of the device, and a random-delay countermeasure wider than the S-box layer can force them even on one who has. This paper presents a SAT filter that removes misinjections without the secret key, one injection at a time. It models the differential propagation from the injected round to the end of the cipher in SAT and rejects an injection when the model has no solution for the assumed fault and the observed ciphertext difference. The paper also presents a neural network filter, which passes an injection when the score of a network trained for the same decision is at least 0.5, and a combined filter, which passes it only when the SAT model of the injection also has a solution. We measure the filters on faults injected by clock glitching into GIFT-64, GIFT-128 and BAKSHEESH on a microcontroller, in three settings, a non-profiling attacker without and with a random-delay countermeasure and a profiling attacker with it. The SAT filter rejected none of the 14669 intended faults and, for the non-profiling attacker without the random-delay countermeasure, at least 0.940 of the misinjections at the full-diffusion round, over at least 385 each. For the same attacker it raises the success probability of ToFA on BAKSHEESH, which recovers the master key, from 5.2% to 61.2%, and the combined filter raises it to 96.2%, each over 2000 trials.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2537) | 2026-10-19
