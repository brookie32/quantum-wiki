---
title: "Efficient Dynamic Group Signatures with Forward Security"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1751"
summary: "In dynamic group signature schemes (GSS), forward security ensures that newly joined members cannot generate valid signatures for past time periods. Additionally, non-frameability prevents even privil"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

In dynamic group signature schemes (GSS), forward security ensures that newly joined members cannot generate valid signatures for past time periods. Additionally, non-frameability prevents even privileged entities, such as the group manager or key issuer, from falsely attributing signatures to honest users. Most GSS either lack non-frameability or face significant efficiency challenges when updating signing keys to ensure forward security. In this paper, we introduce a forward-secure dynamic group signature scheme that guarantees non-frameability. We also present an alternative scheme that, while lacking non-frameability, offers higher efficiency compared to existing schemes with comparable security. For both protocols, we propose efficient revocation mechanisms that allow an authority to revoke users without requiring re-registering existing users. Additionally, we propose a technique that enables the verification process of both protocols to be performed in batches. We prove the security of our schemes, ensuring the standard dynamic GSS security notions; anonymity, traceability and non-frameability (second scheme). Experimental results demonstrate that our schemes are competitive in both computational and communication efficiency when compared to existing literature.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1751) | 2026-08-20
