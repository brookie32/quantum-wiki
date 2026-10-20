---
title: "Evasive Inner Product Functional Encryption Is Broken Too"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2548"
summary: "We show that the Evasive Inner Product Functional Encryption assumption introduced by Hsieh, Lin and Luo (Eurocrypt 2024) is false in its full generality. Our counterexample adds to a long sequence of"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

We show that the Evasive Inner Product Functional Encryption assumption introduced by Hsieh, Lin and Luo (Eurocrypt 2024) is false in its full generality. Our counterexample adds to a long sequence of works that have attacked different variants of Evasive LWE, taking down another instance that has been considered ``public coin'' (and hence safe) in the literature. Our attack extends the counterexample against pseudorandom functional encryption (mathsf{PRFE}), developed by Agrawal, Modi, Yadav and Yamada (TCC 2025) to encompass the notion of Evasive Inner Product Functional Encryption (mathsf{evIPFE}) proposed by Hsieh, Lin and Luo (Eurocrypt 2024). The original attack relied crucially on the underlying functional encryption scheme being powerful enough to compute pseudorandom functions; our attack shows, perhaps surprisingly, that the much weaker ``evasive'' inner product functionality suffices to mount the attack. We interpret our attack as showing that even the slightest power given to the adversary in choosing unrestricted private coins in the evasive LWE family of assumptions, renders it insecure.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2548) | 2026-10-19
