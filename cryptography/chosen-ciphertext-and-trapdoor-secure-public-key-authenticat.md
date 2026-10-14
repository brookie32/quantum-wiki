---
title: "Chosen Ciphertext and Trapdoor Secure Public Key Authenticated Encryption with Keyword Search"
date: "2026-10-11"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2446"
summary: "For public-key encryption with keyword search (PEKS), chosen-ciphertext attack (CCA) security has been studied in settings where an adversary is allowed to access the test oracle. Notably, the CHK tra"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

For public-key encryption with keyword search (PEKS), chosen-ciphertext attack (CCA) security has been studied in settings where an adversary is allowed to access the test oracle. Notably, the CHK transformation (Canetti, Halevi, and Katz, EUROCRYPT 2004) does not yield CCA-secure PEKS. To address this limitation, Abdalla, Bellare, and Neven (TCC 2010/JoC 2018) proposed a generic construction of CCA-secure PEKS from CCA-secure anonymous and weakly robust identity-based encryption. However, CCA security alone is insufficient to resist keyword-guessing attacks (KGAs) arising from trapdoor leakage in PEKS. To mitigate KGAs, public-key authenticated encryption with keyword search (PAEKS) has been studied. In particular, Li and Boyen (IACR CiC 2024) proposed a generic construction of PAEKS. In this paper, we propose a generic transformation that converts a PAEKS scheme into a CCTA-secure one, where CCTA denotes security against chosen-ciphertext and trapdoor attacks. Our transformation can be viewed as a variant of the CHK transformation. The key observation is that, unlike in PEKS, the receiver in PAEKS identifies and specifies the sender when generating a trapdoor, enabling keywords to be used as tags. The transformation directly upgrades PAEKS instantiations obtained via the Li-Boyen generic construction under various assumptions to CCTA-secure schemes. As a result, we obtain the first fully CCTA-secure PAEKS schemes from both pairings and lattices. As an additional benefit, the transformation improves search efficiency. By leveraging verification keys embedded in ciphertexts and trapdoors, sender-receiver matching can be performed without cryptographic computation, for example, by using hash tables. Consequently, for a trapdoor associated with a particular sender, the search complexity measured in cryptographic operations becomes independent of the number of senders and is essentially the same as that of PEKS. Although improving efficiency is not the primary goal of the transformation, this benefit is of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2446) | 2026-10-11
