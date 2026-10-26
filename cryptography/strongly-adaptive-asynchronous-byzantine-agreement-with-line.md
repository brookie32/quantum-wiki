---
title: "Strongly Adaptive Asynchronous Byzantine Agreement with Linear Communication and Almost-Everywhere Termination"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2627"
summary: "It is well known that Byzantine agreement requires Omega(t^2) messages against a strongly adaptive adversary that may corrupt t=Theta(n) parties and suppress a party's undelivered messages upon corrup"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

It is well known that Byzantine agreement requires Omega(t^2) messages against a strongly adaptive adversary that may corrupt t=Theta(n) parties and suppress a party's undelivered messages upon corruption. We circumvent this lower bound by relaxing termination: for any constant 00 and every tleq(1-elta)n/3, we construct binary agreement with this guarantee in authenticated asynchronous networks against strongly adaptive corruptions with message takebacks. Except with negligible probability, these guarantees hold and every honest decision carries a transferable justifier. The protocol achieves almost-everywhere termination in expected O(1) rounds, expected total communication O(nkappa^2) bits, and expected maximum communication widetilde O(kappa^2) bits over honest parties before corruption, where kappa is the computational security parameter. Our construction combines a recursively shared BLS signing key with certificate dissemination over a sparse graph. The recursive sharing is used to implement threshold signing with distinct safety and liveness thresholds. Dissemination propagates existing certificates to almost all honest parties. The construction uses a trusted setup and is secure in the random oracle model under the algebraic one-more computational Diffie--Hellman assumption. We further obtain full binary agreement with the same asymptotic communication and round complexity against adaptive corruptions without message takebacks. The extension requires neither atomic multi-send nor private communication channels.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2627) | 2026-10-24
