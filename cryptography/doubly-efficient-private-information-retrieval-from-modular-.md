---
title: "Doubly-Efficient Private Information Retrieval from Modular Forms"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2836"
summary: "We present new information-theoretic protocols for s-server, doubly-efficient private information retrieval (PIR) in sublinear server time and one extra bit of space on the servers, for every constant"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

We present new information-theoretic protocols for s-server, doubly-efficient private information retrieval (PIR) in sublinear server time and one extra bit of space on the servers, for every constant s geq 2. On an n-bit database, each of the s PIR servers first builds and stores a preprocessing data structure consisting of n+1 bits (which is unique to each server, and after which the server may discard the original database). Then, each server answers a PIR query in time T_s(n), by reading at most T_s bits of its data structure and sending them to the user. In the two server setting (s=2), our PIR protocols achieve T_2 = n^{0.82}, matching the server time of the state-of-the-art schemes of Henzinger and Ragavan (EUROCRYPT 2026) while shrinking their storage from O(nsqrt{log n}) to n+1 bits. With s geq 3 servers, our PIR protocols retain the n+1 bits of storage and additionally improve on the server time of all prior information-theoretic s-server schemes with n^{1+o(1)} storage: for example, achieving T_3 = n^{0.74} and T_{10} = n^{0.61} (previously n^{0.79} and n^{0.75}). Asymptotically, as the server count s grows, we shrink the number of servers required to achieve a given server-work exponent from s^{3.9} to s. Our results draw inspiration from matching-vector techniques (Efremenko, STOC 2009), which we generalize to handle degree-two computations in the exponent. Using this generalization, we build doubly-efficient PIR from the new intermediate abstraction of Fourier-sparse cone-delta functions. Then, we construct such Fourier-sparse cone-delta functions via a connection to modular forms and complex analysis: if a Fourier-sparse cone-delta function does not exist, then there exists a modular form which has too many roots, contradicting the valence formula.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2836) | 2026-11-09
