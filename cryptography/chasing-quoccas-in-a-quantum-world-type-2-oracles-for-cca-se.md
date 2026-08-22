---
title: "Chasing QuOCCAs in a Quantum World: Type-2 Oracles for CCA-Secure PKE"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1746"
summary: "In the context of PKE schemes, Gagliardoni et al. proposed at PQCrypto 2021 a qIND-qCPA security notion (a superposition-based analogue of the classical IND-CPA security notion), by using the theory o"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

In the context of PKE schemes, Gagliardoni et al. proposed at PQCrypto 2021 a qIND-qCPA security notion (a superposition-based analogue of the classical IND-CPA security notion), by using the theory of so-called type-2 unitary operators. On one hand, this notion is very natural, closely mirrors the classical intuition, and can be handled without relying on complex techniques such as Zhandry’s compressed oracles. On the other hand, it is restricted to a certain class of PKE schemes (so-called isometric). Moreover, it is not immediately clear how to extend the definition to chosen-ciphertext attack (CCA) scenarios, mainly due to the possibility of decryption failures – something that is entailed by most quantum-resistant PKE schemes. In this work, we use the theory of type-2 operators to extend superposition-based security notions to any PKE schemes, in the CPA and CCA setting, without Zhandry’s compressed oracle technique. We start first by showing that a trivial extension of Gagliardoni et al.’s techniques to the general case is not possible, even for the CCA1 case, by identifying barriers preventing the realization of a ‘natural’ type-2 decryption operator. Then we define a subclass of PKE schemes (which we call ‘strongly decryptable’ ), for which it is easy to circumvent the aforementioned barriers and to define superposition-based CCA1 and CCA2 notions. Further, we introduce a novel transformation (that we call ‘purification’) which applies to any PKE scheme, producing a ‘quasi-PKE’ scheme, for which it is possible to define properties that mimic the security notions defined for strongly decryptable schemes; we can thus ‘unload’ the security definitions for an arbitrary PKE scheme on its purification. Finally, we show implications and separations between our security notions, as well as constructions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1746) | 2026-08-20
