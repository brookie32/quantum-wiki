---
title: "Registered Functional Encryption for Circuits with Dynamic Bounded Collusion"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2594"
summary: "Registered Functional Encryption (Reg-FE) eliminates the key escrow issue in traditional functional encryption by allowing users to generate their own public/secret keys without the help of a central "
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Registered Functional Encryption (Reg-FE) eliminates the key escrow issue in traditional functional encryption by allowing users to generate their own public/secret keys without the help of a central authority. The public key is then registered to the system along with a function, and all the registered public keys will be aggregated to a compact master public key by a transparent key curator. Messages are encrypted under the master public key, and users can learn functions of encrypted data from the ciphertext using their own secret keys. Prior constructions of Reg-FE either become insecure when more than one malicious users collude or require the heavy machinery of indistinguishability obfuscation. In this work, we construct the first collusion-resistant Reg-FE without obfuscations. The schemes are secure if the number of colluded users is bounded, and the collusion bound can be either a global parameter or specified by the encryption algorithm dynamically. In both settings, we provide generic constructions of Reg-FE from registered attribute-based encryption and instantiate them from either the standard k-Lin assumption or the succinct LWE assumption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2594) | 2026-10-22
