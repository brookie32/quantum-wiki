---
title: "Revisiting Accountability in Accountable Tracing Signatures"
date: "2026-11-02"
updated: "2026-11-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2718"
summary: "Accountable tracing signatures (ATS), introduced by Kohlweiss and Miers (PoPETs 2015), classify each group member (user) as either traceable or non-traceable. A traceable user corresponds to one in co"
last_verified: "2026-11-04"
review_by: "2027-02-02"
stale: false
---

Accountable tracing signatures (ATS), introduced by Kohlweiss and Miers (PoPETs 2015), classify each group member (user) as either traceable or non-traceable. A traceable user corresponds to one in conventional group signature schemes whose identity can be revealed by the opener from a signature, whereas a non-traceable user cannot be identified from any signature they produce. The opener, who issues a witness, can certify a user's status via the Account algorithm. In this paper, we formalize accountability soundness, which ensures that no two witnesses can simultaneously certify a user as both traceable and non-traceable. We show that the Kohlweiss-Miers ATS scheme admits conflicting witnesses that violate this property. Since accountability is a fundamental aspect of ATS, as reflected in its name, such conflicting witnesses undermine the intended guarantees of the primitive. To address this issue, we propose a patched version of the Kohlweiss-Miers ATS scheme that provides accountability soundness. We also discuss the applicability of our attack to the lattice-based ATS scheme (Ling et al., CT-RSA 2019) and the isogeny-based ATS scheme (Shaw-Dutta, Indocrypt 2021), together with preliminary investigations of possible countermeasures. We emphasize that all our attacks fall outside the original security models.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2718) | 2026-11-02
