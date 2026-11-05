---
title: "The Price of Agreement in Secure Multiparty Computation"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2745"
summary: "Secure multi-party computation (MPC) cannot guarantee output delivery, in general, in the dishonest-majority setting. Security of MPC is therefore relaxed to security with abort, where the adversary m"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Secure multi-party computation (MPC) cannot guarantee output delivery, in general, in the dishonest-majority setting. Security of MPC is therefore relaxed to security with abort, where the adversary may prevent honest parties from obtaining their output. The standard notion of unanimous abort (UA-MPC) ensures that either all honest parties obtain their output or all of them abort. Goldwasser and Lindell [JCRYPT '05] introduced the relaxed notion of selective abort, allowing some honest parties to abort and others to obtain their output. While two-round SA-MPC can be achieved over point-to-point channels, two-round UA-MPC necessitates the second round to be over broadcast. The price of agreement in dishonest-majority MPC is thus tied to the round complexity of broadcast with unanimous abort (UA-broadcast). The round complexity of broadcast has been extensively studied for more than four decades. Garay, Katz, Koo, and Ostrovsky [FOCS '07] (GKKO) proved that the expected round complexity of broadcast protocols tolerating t corruptions is at least 2n/(n-t)-1. Their argument, however, relies on all honest parties obtaining an honest sender's input, and does not extend to UA-broadcast. Recently, Cohen {em et al.} [TCC '26] showed that UA-MPC is possible in an expected constant number of rounds when a constant fraction of the parties is honest, and asked whether this extends to n-o(n) corruptions. In this work we answer this question in the negative: Agreement alone already incurs the GKKO barrier. Concretely, we prove that for tleq n-2, UA-broadcast---and hence UA-MPC---requires at least t/(2(n-t)) rounds in expectation, matching the asymptotic bound for broadcast without abort. As a corollary, expected-constant-round UA-MPC is possible if and only if a constant fraction of the parties is honest. Next, we consider UA-broadcast protocols that terminate in an {em a-priori} known round, and show that the bound that the argument of GKKO gives for broadcast holds for them exactly. Combined with the broadcast protocol of Dolev and Strong [SICOMP '83], our bound is tight for arbitrarily many corruptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2745) | 2026-11-03
