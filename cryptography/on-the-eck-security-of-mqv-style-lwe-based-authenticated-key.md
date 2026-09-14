---
title: "On the eCK Security of MQV-Style LWE-Based Authenticated Key Exchange"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2017"
summary: "Designing Authenticated Key Exchange (AKE) directly from the Learning with Errors (LWE) assumption, without relying on generic constructions, remains a prominent and challenging goal in post-quantum c"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Designing Authenticated Key Exchange (AKE) directly from the Learning with Errors (LWE) assumption, without relying on generic constructions, remains a prominent and challenging goal in post-quantum cryptography. Such designs inherently require reconciliation mechanisms, which may introduce additional leakage against active adversaries under key reuse. Yet previous signal leakage attacks of Bindel et al. (LATINCRYPT 2021) and Qin et al. (ESORICS 2022) fail against protocols hardened with dedicated countermeasures. In this paper, we propose new signal leakage attacks capable of compromising LWE-based (authenticated) key exchange, where prior attacks fail. First, we target the landmark MQV-style AKE protocol proposed by Zhang et al. (EUROCRYPT 2015), known as ZZDSD-AKE. Determining whether it can natively achieve security under the strong extended Canetti-Krawczyk (eCK) model has remained a long-standing open question. By exploiting the ephemeral key compromise defined within the eCK model, our new attack based on a geometric perspective recovers the static secret key from signal leakage, definitively resolving this open question with a negative result. Furthermore, we extend our methodology to the GDLL-KE protocol of Gao et al. (IEEE TC 2018), which is designed to be robust against key-reuse via a randomized noise countermeasure. Our attack shows that its ad-hoc countermeasure fails to eliminate secret-dependent leakage. Our implementations demonstrate that the proposed attacks recover the secret key in roughly 1,700 queries against ZZDSD-AKE and 180 queries against GDLL-KE, respectively. These results reveal that MQV-style structures and simple randomization are insufficient for securing AKEs directly based on LWE against sophisticated active attacks, providing critical insights for future protocol design and standardization.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2017) | 2026-09-14
