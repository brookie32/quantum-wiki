---
title: "EA Codes Approaching Singleton Bound (with Application to Field-Agnostic SNARKs)"
date: "2026-08-23"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1782"
summary: "SNARKs based on error-correcting codes require codes that simultaneously support fast encoding and large relative distance. Reed--Solomon codes achieve the optimal rate--distance tradeoff given by the"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

SNARKs based on error-correcting codes require codes that simultaneously support fast encoding and large relative distance. Reed--Solomon codes achieve the optimal rate--distance tradeoff given by the Singleton bound, but their fast encoding relies on FFT-friendly fields, limiting their applicability to field-agnostic constructions. In this work, we revisit expand--accumulate (EA) codes, a simple family of linear codes that admit efficient encoding over arbitrary fields. We prove strong distance guarantees for EA codes whose sparse expansion matrix is sampled from the exact-weight ensemble. Over sufficiently large finite fields, we show that these codes achieve a rate--distance tradeoff arbitrarily close to the Singleton bound with high probability, resolving conjectures from prior work. Building on these results, we construct extsf{Flare}, a new field-agnostic polynomial commitment scheme based on EA codes. Our construction develops an efficient IOP for the constrained relation of EA codes and combines it with code switching and random linear folding for interleaved codes. For statements of size M, extsf{Flare} achieves O(Mlog M) prover time and O(log^2 M) proof size, improving upon the O(sqrt{M}) proof size of prior constructions based on EA codes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1782) | 2026-08-23
