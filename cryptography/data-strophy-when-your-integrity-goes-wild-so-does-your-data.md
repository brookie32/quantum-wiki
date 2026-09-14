---
title: "Data-strophy: When Your Integrity Goes Wild, So Does Your Data!"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1994"
summary: "Proton is a popular privacy-focused service vendor, serving over 100,000 organizations. Proton Docs/Sheets supports real-time collaborative document editing, which claims to offer end-to-end security."
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Proton is a popular privacy-focused service vendor, serving over 100,000 organizations. Proton Docs/Sheets supports real-time collaborative document editing, which claims to offer end-to-end security. This is mainly achieved by applying cryptographic protection through users' Web clients so that data outside the user's client remains confidential and intact. We analyze the cryptographic design and the collaborative editing protocol of Proton Docs/Sheets based on the open-source Web client code and the webpage code inspection. We demonstrate three distinct "integrity" attacks against Proton Docs/Sheets that can cause history rewriting, context manipulation, and censorship, all of which can, in fact, evade detection. The first two can be launched even when the Proton server acts honestly, and the third is mounted by a corrupted Proton server. We also present the corresponding mitigation methods. Our attacks highlight the subtleties of end-to-end security in collaborative settings involving multiple users and constant updates. This state of affairs naturally calls for systematic formal treatment (i.e., design and/or analysis) of the security of such systems.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1994) | 2026-09-12
