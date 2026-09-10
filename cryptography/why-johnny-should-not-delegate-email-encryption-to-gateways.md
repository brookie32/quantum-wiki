---
title: "Why Johnny Should Not Delegate Email Encryption to Gateways"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1911"
summary: "Email encryption based on S/MIME and, to a lesser extent, PGP is widely deployed in enterprise environments, often through centralised server-side encryption gateways that decrypt and sign messages on"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Email encryption based on S/MIME and, to a lesser extent, PGP is widely deployed in enterprise environments, often through centralised server-side encryption gateways that decrypt and sign messages on behalf of end users. Gateways can also be run locally to implement encryption for email clients that do not natively support it. We systematically analyse the security of four such products: SEPPmail, CipherMail, Cisco Email Security Appliance, and the Proton Mail Bridge. We identify 29 attacks which allow an adversary to fully decrypt messages and confuse users on the authenticity of received emails. To this end, we exploit the legacy cryptographic primitives in S/MIME and the backwards compatibility features for PGP, adapt well-known attacks such as EFAIL (Poddebniak et al., USENIX Security 2018) to this setting, and expose novel attack vectors such as the error signals produced by email infrastructure. Our findings show that moving cryptographic operations to gateways strips important signals that email clients rely on. This re-enables attacks like EFAIL, which were largely considered resolved, and introduces exploitable features in how the security status of emails is communicated. Such systems also expose sensitive decrypted plaintext to intermediate email infrastructure, which was not designed to handle it. We conclude that delegating cryptographic operations to a gateway undermines the end-to-end security model that PGP and S/MIME were designed to provide.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1911) | 2026-09-07
