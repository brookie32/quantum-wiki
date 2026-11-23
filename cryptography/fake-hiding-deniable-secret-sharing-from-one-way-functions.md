---
title: "Fake-Hiding Deniable Secret Sharing from One-Way Functions"
date: "2026-11-20"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2966"
summary: "Deniable secret sharing (DSS), introduced by Canetti et al. (TCC 2025), considers an adversary who coerces or bribes shareholders into revealing their shares. Shareholders are either fakers, who submi"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Deniable secret sharing (DSS), introduced by Canetti et al. (TCC 2025), considers an adversary who coerces or bribes shareholders into revealing their shares. Shareholders are either fakers, who submit fake shares of a target message, or snitches, who reveal their real shares. Fake hiding, the strongest security notion considered in their work, ensures that the adversary cannot tell whether any submitted shares are fake. We focus on their coordinated shareholder-specified setting for threshold DSS, where fakers coordinate and choose the target fake message. When the fakers form a strict majority but remain unqualified to reconstruct the secret, Canetti et al. rule out information-theoretic fake-hiding DSS and give a construction based on indistinguishability obfuscation. In this regime, we construct a DSS scheme with statistical fake hiding and computational privacy from one-way functions alone, and prove that one-way functions are also necessary for such schemes. We further define a property that strengthens fake hiding by guaranteeing deniability even when the fakers' original shares are revealed, and call it strong fake hiding. We show that public-key encryption is necessary and sufficient to construct DSS schemes satisfying this property.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2966) | 2026-11-20
