---
title: "A decrementally-improved algorithm for Boolean MQ"
date: "2026-08-16"
updated: "2026-08-18"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1704"
summary: "The MQOM signature scheme is currently a third-round candidate in the NIST competition for additional signatures. It is based on the ``MPC-in-the-Head'' paradigm and relies on the hardness of the MQ p"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

The MQOM signature scheme is currently a third-round candidate in the NIST competition for additional signatures. It is based on the ``MPC-in-the-Head'' paradigm and relies on the hardness of the MQ problem. Some of its parameter sets expose a Boolean quadratic system in the public key. While the situation for MQ over larger fields has been relatively quiescent over the last decade, Boolean MQ has seen active progress, culminating with Dinur's algorithms at SODA 2021 and Eurocrypt 2021. We propose yet another algorithm for Boolean MQ. It is a hybrid between the ``polynomial-method'' of Lokshtanov, Paturi, Tamaki, Williams and Yu from SODA 2017 and Dinur's ``second algorithm'' from Eurocrypt 2021. We remove some machinery from the latter to obtain a modest improvement of 1--4 bits in performance for MQOM parameters (``decremental improvement''). MQOM optionally uses the ``correlated GGM trees'' technique to shorten signatures; in that case, its security also relies on the hardness of the ``Partial-Guessing One-Wayness'' problem for MQ (PGOW-MQ): given an MQ system supposed to offer lambda bits of security, the adversary has to find the first lambda bits of a solution, and they have access to an oracle that enables them to check candidate prefixes. The designers of MQOM implicitly assumed that PGOW-MQ is as hard as MQ itself. Our algorithm can exploit the availability of the solution-testing oracle to solve PGOW-MQ 2 to 4 times faster than it solves MQ, thus showing that the two problems are marginally different. This yields attacks against MQOM that are 3--4 bits below the expected security level, but that suffer from huge memory complexities. Lastly, we survey old and new techniques to find an invertible linear change of variables that puts a few arbitrary polynomials in UOV shape. This leads to a small acceleration of our algorithm, and also incidentally improves upon the Thomae-Wolf and Furue-Nakamura-Takagi algorithms to solve underdetermined Boolean systems. A new idea based on matrix pencils was used to solve the largest underdetermined Boolean Fukuoka MQ challenges and may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1704) | 2026-08-16
