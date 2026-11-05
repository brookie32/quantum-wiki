---
title: "Leakage-Tolerant Computation without Leakage-Free Setup"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2737"
summary: "Leakage-tolerant multi-party computation (MPC) ensures that leakage from each honest party’s internal state reveals no more than the leakage from honest parties' individual inputs and outputs, beyond "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Leakage-tolerant multi-party computation (MPC) ensures that leakage from each honest party’s internal state reveals no more than the leakage from honest parties' individual inputs and outputs, beyond the standard security guarantee of MPC. Previous constructions either require a leakage-free preprocessing, or rely on indistinguishability obfuscation in the common reference string (CRS) model and only achieve semi-honest security. In the computational setting, assuming only an augmented non-committing encryption scheme, we show that every adaptively well-formed functionality admits a semi-honest leakage-tolerant MPC protocol, without any leakage-free preprocessing execution or CRS. Under the decisional Diffie–Hellman assumption, we further extend this result to malicious security in the CRS model for all deterministic functionalities. The limitation of deterministic functions is subject to an impossibility result of leakage-based coin-tossing protocols. In the information-theoretic setting, we show that secure erasure enables statistically secure leakage-tolerant MPC of arbitrary functionalities assuming strictly less than half of the participants are maliciously corrupted. We complement this construction with an impossibility result: without secure erasure, general-purpose statistically secure leakage-tolerant MPC with leakage-oblivious simulation, an important property to enable universal composition, is impossible in the plain model, even when all parties are honest. As a further application, we also obtain information-theoretic leakage-tolerant circuits against bounded communication leakage, while all prior works are restricted only to the weaker variant of leakage-resilient circuits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2737) | 2026-11-03
