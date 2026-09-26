---
title: "Static Group Signature with Post-Compromise Accountability"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2184"
summary: "Signatures with Post-Compromise Accountability (SPCA), introduced by Dayanikli et al. at SCN'26, are signature schemes that enable signatures generated before the compromise of a signing key to be dis"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Signatures with Post-Compromise Accountability (SPCA), introduced by Dayanikli et al. at SCN'26, are signature schemes that enable signatures generated before the compromise of a signing key to be distinguished from those produced after the compromise. In this paper, we extend this notion to static group signatures and introduce Group Signatures with Post-Compromise Accountability (GSPCA). GSPCA preserves the anonymity and traceability guarantees of group signatures while enabling pre-compromise signatures to be revalidated after key compromise. The coexistence of opening and revalidation algorithms gives rise to a new consistency requirement, which we formalize as opening--revalidation consistency. We present a generic construction of GSPCA from public key encryption schemes, signature schemes, and simulation-sound non-interactive zero-knowledge proof systems. A central technical difficulty is that the encryption randomness in our construction is derived from a randomized signature component and may therefore have high min-entropy without being uniformly distributed. To address this issue, we introduce adaptive hedged security against adaptive chosen-ciphertext attacks (AH-CCA), which extends indistinguishability under adaptive chosen-ciphertext attack (IND-CCA2) to adaptively chosen high-min-entropy message--randomness distributions, and show how to realize the required randomness-recovering encryption in the random oracle model. We also give a generic signature-based mechanism that provides the required min-entropy and key-binding properties. Finally, we show that ordinary IND-CCA2 security alone is insufficient as a general assumption for our construction by exhibiting an IND-CCA2 secure encryption scheme for which the resulting GSPCA scheme fails to satisfy anonymity.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2184) | 2026-09-23
