---
title: "A Probabilistic Extension of the Division Property: Integral Distinguishers with Key-Independent Bounds"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2602"
summary: "Classical integral cryptanalysis relies on zero-sum properties that, for every key, hold with probability one. Existing arguments against such deterministic integrals, based on the division property a"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Classical integral cryptanalysis relies on zero-sum properties that, for every key, hold with probability one. Existing arguments against such deterministic integrals, based on the division property and its algebraic variants, only exclude this extreme case: once the zero-sum probability falls below one, they say nothing about its actual value, nor about a probabilistic bias that could still be exploited. We develop a tool combining MILP-based trail search with a recursive evaluation of assignments to the constant inputs. It estimates the probability that no valid trail remains and uses an additional heuristic to predict the zero-sum probability. Applying this tool to PRESENT and GIFT, we obtain probabilistic integral distinguishers for 6 to 9 rounds, including 6- and 7-round PRESENT distinguishers using 2^4 and 2^{12} plaintexts per structure, respectively. For the ASCON permutation, we obtain 4- and 5-round distinguishers using as few as 2 and 2^{12} inputs per structure. We further explain algebraically the large bias of the 6-round PRESENT distinguisher, showing how the S-box and bit permutation restrict the way active variables combine. Finally, we show how these distinguishers can be used for key recovery, reducing both the data and time complexities compared to their deterministic variants for PRESENT and GIFT-64.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2602) | 2026-10-22
