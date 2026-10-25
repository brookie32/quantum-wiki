---
title: "Tight Post-Quantum Multi-Key Security of the FX Construction"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2614"
summary: "The FX construction (FX) is one of the simplest key-length extension schemes for block ciphers, introduced by Kilian and Rogaway as a generalization of DESX. By extending the key length without modify"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

The FX construction (FX) is one of the simplest key-length extension schemes for block ciphers, introduced by Kilian and Rogaway as a generalization of DESX. By extending the key length without modifying the underlying block cipher, FX can improve security against adversaries that perform quantum computation but are restricted to classical queries to the keyed construction. Recently, Shiba and Iwata showed in their ToSC 2026 paper that FX with an n-bit block and a kappa-bit internal key is secure up to approximately 2^{(n+kappa-log_2mu)/3} total classical and quantum oracle queries in the quantum ideal cipher model, where muleq2^kappa is the number of independently keyed instances. In this paper, we improve this bound to approximately 2^{(n+kappa)/3} total oracle queries in the same model against fully adaptive adversaries, for every mugeq1 and 1leqkappaleq2n. The known attack based on the offline Simon's algorithm can target a single keyed instance and matches our bound in the exponent. Thus, the exponent of the total query complexity required to break FX is independent of the number of keyed instances in this parameter regime.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2614) | 2026-10-23
