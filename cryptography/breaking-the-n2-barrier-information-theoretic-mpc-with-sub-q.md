---
title: "Breaking the n^2 Barrier: Information-Theoretic MPC with Sub-Quadratic Communication"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2311"
summary: "Secure multi-party computation (MPC) considers the problem of securely computing a function across n parties such that no adversary controlling t corrupted parties may learn any additional information"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Secure multi-party computation (MPC) considers the problem of securely computing a function across n parties such that no adversary controlling t corrupted parties may learn any additional information beyond the function output. For information-theoretic security in the honest majority setting, recent works have made tremendous progress in reducing the MPC communication costs for large circuits obtaining as low as ilde{O}(|C|) total communication. To date, all information-theoretic MPC protocols require an additive ilde{Omega}(n^2) communication independent of the circuit size that becomes the dominant cost for small circuits. In this work, we consider the problem of building more efficient information-theoretic MPC protocols with o(n^2) communication for small circuits. For corruption threshold t< (1/2-epsilon)dot n, we present an information-theoretic MPC protocol secure against adaptive and malicious adversaries with subquadratic communication for a wide range of circuits, including those in which the number of input parties I satisfies |I| = o(n), circuit size |C| = o(n^{1.5}/|I|), and circuit depth mathsf{depth}(C) = o(n); for example, |C| = o(n^{3/4}) and |I| = o(n^{3/4}) input parties. To our knowledge, this is the first information-theoretic MPC protocol with o(n^2) communication for a wide-range of circuit classes. Furthermore, we note the requirement of sublinear input parties |I| = o(n) is necessary to obtain o(n^2) communication due to the Omega(|I| dot n) lower bound by Damgård {em et al.} [EUROCRYPT'16]. To obtain our new MPC protocol, we develop new techniques for key MPC subroutines including randomness generation, player virtualization and output reconstruction with o(n^2) communication leveraging the sublinear number of input parties, |I| = o(n), and randomized output distribution with unpredictable communication patterns. Finally, we also prove a separation showing that o(n^2) communication MPC is impossible for adversaries with stronger than standard adaptive rushing capabilities even for constant-size circuits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2311) | 2026-10-02
