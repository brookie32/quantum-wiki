---
title: "Optimal Byzantine Atomic Broadcast with Message Drops"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2150"
summary: "Recent works have studied Byzantine agreement (BA) in the mixed-fault model with resilience threshold n>2t+r+s, where n is the number of parties, t is the number of Byzantine parties, r is the number "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Recent works have studied Byzantine agreement (BA) in the mixed-fault model with resilience threshold n>2t+r+s, where n is the number of parties, t is the number of Byzantine parties, r is the number of receive-faulty parties, and s is the number of send-faulty parties. In particular, Feng et al.~(ASIACRYPT~2025) proposed a BA protocol with optimal resilience, expected asymptotically quadratic communication complexity, and expected constant round complexity. However, existing BA protocols guarantee a meaningful output v only when all parties hold the same input v. Such a guarantee is insufficient for efficient construction of atomic broadcast protocols, leaving efficient atomic broadcast in the mixed-fault setting as an open problem. In this paper, we present the first atomic broadcast protocol (UABC) with optimal resilience in the mixed-fault model. In addition, our protocol achieves communication complexity O(nell+n^2lambda^2) when t=Theta(n), where ell is the input size and lambda is the security parameter. This complexity is asymptotically optimal for moderately large ell, namely when ellge nlambda^2. At the core of our design is an undead verifiable information dispersal (UVID) protocol, which allows an input to be efficiently dispersed and later reconstructed in the mixed-fault setting. Leveraging UVID together with the undead multi-valued consensus (ASIACRYPT~2025), we further construct a new primitive called weak undead multi-valued validated Byzantine agreement (wUMVBA) and its optimized variant (Opt-wUMVBA). Unlike standard multi-valued validated Byzantine agreement, wUMVBA and Opt-wUMVBA guarantee that the output is either a meaningful value satisfying the validity predicate or ot. Moreover, the probability of outputting ot is at most (t+s)/n. Finally, by leveraging Opt-wUMVBA, we obtain our optimal atomic broadcast protocol for the mixed-fault setting.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2150) | 2026-09-22
