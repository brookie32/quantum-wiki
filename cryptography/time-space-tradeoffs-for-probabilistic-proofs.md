---
title: "Time-Space Tradeoffs For Probabilistic Proofs"
date: "2026-10-07"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2406"
summary: "Many recent constructions of probabilistic proofs achieve fast proving times but have high space complexity (much higher than that of the computation being proved). Empirically this arises due to the "
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

Many recent constructions of probabilistic proofs achieve fast proving times but have high space complexity (much higher than that of the computation being proved). Empirically this arises due to the fact that error-correcting codes, a key ingredient of such constructions, suffer from limiting time-space tradeoffs. It remained open, however, whether such time-space tradeoffs exist for proofs themselves. We establish time-space tradeoffs for probabilistically checkable proofs (PCPs) as well as for their multi-round extension, interactive oracle proofs (IOPs), with straightline knowledge soundness. Our results hold for machine computations that have sequential input access, the same model for which similar tradeoffs hold for error-correcting codes. We complement this result by describing an IOP for R1CS that avoids the tradeoff but requires random access to the R1CS witness. Our techniques build on and extend results for codes of Cook and Moshkovitz (CCC~2024). A key difficulty that we encounter in establishing our tradeoff is that distance of the code plays a key role in prior results, while for probabilistic proofs there is no natural notion of distance. Nevertheless, we show that, assuming the existence of collision-resistant hash functions, we can establish time-space tradeoffs by carefully relating a small-space machine's information flow to the proof system's properties.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2406) | 2026-10-07
