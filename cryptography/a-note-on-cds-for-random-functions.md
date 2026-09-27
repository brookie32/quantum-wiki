---
title: "A Note on CDS for Random Functions"
date: "2026-09-24"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2208"
summary: "We record the following bound: almost all Boolean functions f : {0,1}^n imes {0,1}^n o {0,1} require 2n - 2log n - O(1) bits of communication for perfect two-party conditional disclosure of secrets wi"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

We record the following bound: almost all Boolean functions f : {0,1}^n imes {0,1}^n o {0,1} require 2n - 2log n - O(1) bits of communication for perfect two-party conditional disclosure of secrets with a one-bit secret. This only gives a factor 2 improvement over the previous best bound due to Applebaum, Holenstein, Mishra and Shayevitz [EUROCRYPT 2018], but at least (nearly) matches the input length. The proof is a straightforward compression argument that uses the birthday bound to give a succinct representation of transcript collisions (the latter being a technique from Feige, Kilian and Naor [STOC 1994], refined in Applebaum et al.). Viewing transcript-collision testing as an elementary case of distribution testing extends the argument to imperfect correctness and privacy. We do not currently know how to extend the argument to an explicit hard predicate.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2208) | 2026-09-24
