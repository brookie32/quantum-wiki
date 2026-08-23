---
title: "Constant-round MPC protocols with Fall-back Security"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1768"
summary: "The notion of Best-of-Both-Worlds introduced in the work of Ishai et al. (CRYPTO 2006) investigated whether an MPC protocol can simultaneously provide two incomparable security guarantees depending on"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

The notion of Best-of-Both-Worlds introduced in the work of Ishai et al. (CRYPTO 2006) investigated whether an MPC protocol can simultaneously provide two incomparable security guarantees depending on the number of corrupted parties. As a special case of this, Chaum et al. initiated the study of protocols that tolerate unbounded corruption within a certain adversary structure and PPT corruption of any number of parties beyond that. More recently, Acharya et al. (CRYPTO 2023) formalized this notion as MPC with fall-back security. Although the feasibility of such protocols has now been thoroughly studied in prior works, most of the existing protocols require round complexity linear in the number of parties and the computation size. In this work, we study the round complexity of MPC with fall-back security in the threshold corruption setting, presenting constant-round protocols for optimal thresholds. We present a semi-honest fall-back secure protocol for t < frac{n}{2} with 3 rounds, in the plain model, whereas the best known protocol in the same setting takes at least 11 rounds. In the CRS model, we present a maliciously fall-back secure protocol for the same threshold with 4 rounds, satisfying unanimous abort (UA). Finally, we extend this to a 5-round protocol that satisfies fairness in the presence of unbounded adversaries for t < frac{n}{2} corruptions and UA tolerating PPT adversaries for arbitrary corruption beyond that. In the malicious setting, we construct the first constant-round fall-back secure protocols.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1768) | 2026-08-21
