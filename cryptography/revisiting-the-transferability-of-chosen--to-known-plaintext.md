---
title: "Revisiting the Transferability of Chosen- to Known-plaintext Attacks and Applications to Round-reduced AES"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1759"
summary: "Differential-based attacks represent the best known results for many block ciphers. Such attacks usually demand that the adversary an choose plaintexts (CP) or ciphertexts (CC) in subspaces to satisfy"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

Differential-based attacks represent the best known results for many block ciphers. Such attacks usually demand that the adversary an choose plaintexts (CP) or ciphertexts (CC) in subspaces to satisfy differential trails. However, many widespread modes of operation or applications prohibit the adversary from directly choosing inputs for the majority of primitive calls. While Biham and Shamir already suggested a straightforward trade-off for standard differential attacks in their work on the DES, studies on advanced differential-based types, such as impossible-differential, rectangle, or mixture attacks, have surprisingly received little attention so far. In this work, we study applications of differential-based attacks in the random known-plaintext model (RKP) of the above. For the AES as the probably most widespread block cipher, we derive the best existing distinguishers and attacks in the RKP model on all versions, improving earlier results by at least one round. Interestingly, we show that Demirci-Selcuk meet-in-the-middle attacks with differential enumeration, which require much related data, can also be effective in that setting without approaching the full codebook too closely. For several of our attacks, we showcase differences between the models as trails that lead to the best known attack complexities under chosen data are suboptimal in the RKP model, and can be replaced by better trails. While our results do not threaten the security of the full AES, and their complexities are too high to represent any threats, we hope to inspire cryptographers to also consider attacks in the RKP for future attacks.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1759) | 2026-08-21
