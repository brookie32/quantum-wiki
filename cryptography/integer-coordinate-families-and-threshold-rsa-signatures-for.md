---
title: "Integer Coordinate Families and Threshold RSA Signatures for Any Prime Exponent"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2601"
summary: "At CT-RSA 2026, Ng and Lau introduced (t,n)-integer coordinate families for threshold RSA signatures with e=3, and found some families by heuristic search for 2le t le n le 9. They asked whether such "
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

At CT-RSA 2026, Ng and Lau introduced (t,n)-integer coordinate families for threshold RSA signatures with e=3, and found some families by heuristic search for 2le t le n le 9. They asked whether such families always exist and, if so, can they be constructed efficiently. We answer both of these questions positively. We prove that a (t,n)-integer coordinate family is also a (t+1,n)-integer coordinate family. We construct such families for t=2, and 2le n < 19, using a polynomial time algorithm in n and its output bit length. Answering another question raised in the Ng-Lau work, we prove super-polynomial lower bounds on coordinates of pairwise families. We also find the minimum families for n le 9. Ng and Lau proposed a threshold signature scheme based on integer coordinate families. We show that the Ng-Lau scheme admits trivial forgeries, and has a flawed proof. We give a repaired scheme PiIC which does not suffer from these issues. Finally, we propose an integer secret-sharing scheme PiZ that works for every prime e and every (t,n), without relying on any special coordinate family. We prove that both the schemes PiIC and PiZ are TS-UF-CMA secure under the standard RSA assumption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2601) | 2026-10-22
