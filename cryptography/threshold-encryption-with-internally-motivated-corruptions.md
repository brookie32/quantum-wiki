---
title: "Threshold Encryption with Internally Motivated Corruptions"
date: "2026-08-28"
updated: "2026-08-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1826"
summary: "In recent years, threshold encryption has gained a lot of interest, particularly due to its potential use in encrypted mempools in blockchains. Standard security models allow the adversary to corrupt "
last_verified: "2026-08-30"
review_by: "2026-11-28"
stale: false
---

In recent years, threshold encryption has gained a lot of interest, particularly due to its potential use in encrypted mempools in blockchains. Standard security models allow the adversary to corrupt parties either statically (i.e., fixed at the onset of the game) or adaptively (i.e., via an oracle one-by-one, depending on keys and ciphertexts). In this work, we observe that neither of these models captures the case in which a party decides to become corrupted based on secret information. For instance, in an encrypted mempool application with randomly rotating committees, an adversary may set up a smart contract that pays parties who reveal their decryption share, and parties decide whether to claim it based on, say, whether they are on the next committee. Such corruptions are not fixed in advance, but they are also not chosen solely by an external adversary based on public information. We initiate the formal study of such internally motivated corruptions and partial decryptions. We introduce a security framework in which each party's corruption behavior may depend on its local secret state. That is, on a corruption, the adversary can submit a motivation function and all parties for which this motivation function outputs 1 (on their secret information) are corrupted. A similar internally motivated behavior is allowed for releasing partial decryptions. We then study threshold encryption under this stronger notion of security. In particular, we show: - Negative Results: We show that for certain classes of motivation functions and number of queries, no threshold encryption scheme can satisfy security. We also show a concrete practical attack with internally motivated corruptions against a scheme that has been proven secure with standard corruptions. - Positive Results: We give two efficient classes of constructions from the (Bilinear) Diffie-Hellman assumptions. The first is secure when partial decryptions on the challenge ciphertext are internally motivated. The second additionally allows internally motivated corruptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1826) | 2026-08-28
