---
title: "Security Analysis of Anonymous Authentication in Apple's Private Cloud Compute"
date: "2026-11-12"
updated: "2026-11-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2875"
summary: "Apple's Private Cloud Compute (PCC) offloads on-device computation, such as large language-model prompts, to the cloud while seeking to preserve the privacy users expect from local processing. At its "
last_verified: "2026-11-14"
review_by: "2027-02-12"
stale: false
---

Apple's Private Cloud Compute (PCC) offloads on-device computation, such as large language-model prompts, to the cloud while seeking to preserve the privacy users expect from local processing. At its core lies a custom authentication protocol that must reconcile three competing goals: restricting access to registered users within a rate limit, doing so without revealing user identities or linking their requests, and nonetheless retaining the ability to hold misbehaving users accountable. Apple's protocol combines blind RSA signatures in a hierarchical issuance with a salted-hash binding trick, but ships without any formal statement -- let alone proof -- of the guarantees it is meant to provide. In this work we close this gap by abstracting the desired authentication protocol as PORTA -- pseudonymously openable, rate-limited tokens for anonymous authentication. We formally define the desired privacy, security, and abuse-mitigation properties such a protocol should satisfy, including a new binding notion specific to the protocol's two-step issuance. We then cast Apple's protocol in this model and show that it achieves the rate-limiting goal and, with a small modification, all privacy goals. Its abuse-mitigation mechanism, which is not yet active in the deployed system, would however not provide the desired accountability guarantees even once enabled. Finally, we present an alternative construction based on anonymous credentials that provably achieves all properties and verifies the binding of tokens already at the gateway, so that a user's pseudonym is only revealed in case of abuse.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2875) | 2026-11-12
