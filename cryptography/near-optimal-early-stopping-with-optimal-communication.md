---
title: "Near-Optimal Early Stopping with Optimal Communication"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2553"
summary: "Minimizing both the round and communication complexity of Byzantine agreement (BA) is a longstanding problem. In the synchronous setting, early stopping protocols aim to terminate in number of rounds "
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Minimizing both the round and communication complexity of Byzantine agreement (BA) is a longstanding problem. In the synchronous setting, early stopping protocols aim to terminate in number of rounds that is proportional to the actual number fleq t of corruptions in an execution, rather than on the worst case threshold t. The lower bound on the round complexity for such protocols is known to be min{f+2, t+1} rounds. Existing protocols, however, achieve either round complexity close to the optimal bound or low communication complexity, but not both simultaneously. Elsheimy, Loss, and Papamanthou (ASIACRYPT 2024) obtain (1+epsilon)f+O(1) rounds for any 1> epsilon>0, with O(n^4f kappa) communication. In contrast, Lenzen and Sheikholeslami (PODC 2022) achieve asymptotically optimal O(n dot t) communication for t<n/3, but with a 25f+13 number of rounds. In this work, we present deterministic synchronous Byzantine agreement protocols that achieve new tradeoffs between early stopping round complexity and communication. For t<n/3, without cryptographic setup, we obtain f+O(sqrt{flog f}) termination rounds with optimal O(ndot t) communication (here and throughout, sqrt{f} denotes sqrt{f+1} and log f denotes log(f+2), so that the bounds are well defined when f=0). Thus, our round complexity has the optimal leading coefficient of one, with a sublinear additive overhead. By allowing slightly higher communication, we reduce this overhead to O(sqrt f), obtaining f+O(sqrt f) rounds with O(ndot t+f^2log f) communication. Finally, for t<n/2, assuming a public key infrastructure and threshold signatures, we obtain f+O(sqrt f) rounds with O(ndot tdotkappa) bits of communication, where kappa is the signature length.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2553) | 2026-10-19
