---
title: "A Unifying Umbrella for Circular-Secure Cryptographic Primitives"
date: "2026-08-14"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1686"
summary: "The main message of this paper is that several seemingly different circular-style primitives are existentially equivalent. In particular, somewhat surprisingly, we show that hinting PRGs (Koppula and "
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

The main message of this paper is that several seemingly different circular-style primitives are existentially equivalent. In particular, somewhat surprisingly, we show that hinting PRGs (Koppula and Waters, CRYPTO 2019) are equivalent to secret-key encryption (SKE) schemes satisfying key-dependent-message (KDM) security. As a conceptual centerpiece, we introduce key-dependent-shift (KDS) security for weak pseudorandom functions (PRFs), and show that they serve as a convenient hub connecting these primitives. We also show that KDS secure weak PRFs imply other cryptographic primitives with circular-style security, such as linear-resistant PRGs (Hajiabadi et al., ITC 2023) and hinting weak PRFs (Alamati and Patranabis, ASIACRYPT 2022), all of which are thus existentially equivalent to KDM secure SKE and hinting PRGs as well. Hence, KDS secure weak PRFs can be thought of as a unifying umbrella for circular-secure cryptographic primitives. As another application of our new notion, we show that KDS security enables new constructions of public-key encryption (PKE) satisfying randomness-dependent-message (RDM) security and correlated-product secure trapdoor functions (TDFs). Our key technical contribution is a generic construction of KDS secure weak PRFs from any KDM secure SKE.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1686) | 2026-08-14
