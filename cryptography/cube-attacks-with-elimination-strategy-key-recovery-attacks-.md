---
title: "Cube Attacks with Elimination Strategy: Key Recovery Attacks on Trivium"
date: "2026-10-13"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2460"
summary: "In this paper, we present a novel framework for cube attacks named cube attacks with elimination strategy. The core idea is to find specific key conditions and cubes such that their superpolies under "
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

In this paper, we present a novel framework for cube attacks named cube attacks with elimination strategy. The core idea is to find specific key conditions and cubes such that their superpolies under these key conditions can be efficiently computed. By recovering these conditional superpolies, we can solve the corresponding equation system and thereby retrieve key information. If a sufficient number of such key conditions can be found, the attack can be extended to a larger key space. To apply this framework in practical attacks, we propose the following techniques. First, we propose a nested coefficient solver that combines variable substitution and symbolic computation to efficiently recover superpolies, and present the conditional monomial prediction technique to rapidly recover conditional superpolies. Second, by combining numeric mapping with monomial prediction techniques, we propose an automated cube search algorithm that is capable of generating a large number of good cubes for attacks. Finally, we develop two kinds of testing methods, which are used to efficiently extract substantial key information from large-scale equation systems. To illustrate the power of our techniques, we apply them to Trivium. As a result, for 840 rounds of Trivium, a practical key recovery attack is mounted with complexity below 2^{55} and a success rate 77.8%. For 845 rounds, we present a practical key recovery attack with complexity below 2^{56} and a success rate 98.1% for 2^{80} imes 59.1% keys. For 855 rounds, we present a theoretical weak-key recovery attack for 2^{74} keys. To the best of our knowledge, these are the best practical and theoretical attacks on Trivium. The improvements in the number of rounds reached are 13 for practical attacks and 4 for theoretical attacks, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2460) | 2026-10-13
