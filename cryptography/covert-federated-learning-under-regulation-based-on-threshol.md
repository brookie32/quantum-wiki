---
title: "Covert Federated Learning under Regulation based on Threshold Anamorphic Encryption"
date: "2026-08-31"
updated: "2026-09-02"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1846"
summary: "When communication systems are subject to strict external control, a powerful authority may monitor all transmitted messages and compel users to surrender their secret keys, thereby undermining user a"
last_verified: "2026-09-02"
review_by: "2026-12-01"
stale: false
---

When communication systems are subject to strict external control, a powerful authority may monitor all transmitted messages and compel users to surrender their secret keys, thereby undermining user autonomy and the confidentiality of keys in encrypted communication. Anamorphic encryption (AE) enables covert communication under such surveillance by embedding hidden messages into innocent-looking ciphertexts. However, existing lattice-based AE constructions remain limited and typically rely on lattice trapdoor techniques, which impose restrictive parameter requirements and hinder their deployment in practical post-quantum cryptosystems such as Kyber. Moreover, existing constructions do not address the challenge of enabling covert communication among multiple parties under dictator-controlled environments. In this work, we propose extbf{Threshold Anamorphic Encryption (TAE)}, a new cryptographic primitive that extends receiver-AE to the extbf{N-out-of-N threshold setting}, where the covert message can be recovered only through the collaboration of all N participants. Then we propose extbf{TAKyber}, a concrete instantiation of TAE constructed from the KyberPKE framework. TAKyber embeds covert information into the randomness of ciphertexts rather than the public matrix structure, avoiding the large aspect-ratio requirement imposed by lattice trapdoor techniques and enabling deployment on Kyber and other lattice-based encryption schemes whose public matrices do not satisfy such requirements. Furthermore, TAKyber distributes covert information into multiple components during encryption and enables extbf{all N participants to jointly reconstruct the covert ciphertext}, while preventing any subset of fewer than N participants without the double key from obtaining any information about the covert message. Finally, we apply TAKyber to privacy-preserving federated learning, where participants can securely exchange encrypted model gradients while simultaneously transmitting covert information through the anamorphic channel under dictator-controlled environments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1846) | 2026-08-31
