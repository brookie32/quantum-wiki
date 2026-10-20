---
title: "Circular Dragon: widetilde{{O}}ptimal Adaptively Secure Distributed Randomness/Key Generation and Parallel Broadcast"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2534"
summary: "We present the first strongly adaptive common coin protocol, under the PKI setup (in the random oracle model and the algebraic group model, yet with no trusted dealer), that (i) achieves the optimal r"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

We present the first strongly adaptive common coin protocol, under the PKI setup (in the random oracle model and the algebraic group model, yet with no trusted dealer), that (i) achieves the optimal resilience t< n/2 in synchronous networks, and (ii) attains near-optimal asymptotics: near-quadratic communication O(kappa lambda n^2log n) and logarithmic rounds O(kappalog n), with failure probability extsf{negl}(lambda)+2^{-kappa}, where lambda (resp. kappa) is the computational (resp. statistical) security parameter. Furthermore, the coin protocol assumes no memory erasure. At its core is a ``special-purpose'' distributed key generation (DKG) protocol that produces a secret in an elliptic-curve group. Our common coin immediately implies the first strongly adaptive and optimally resilient Byzantine Agreement with subcubic communication and sublinear rounds in the absence of a trusted dealer. Furthermore, we give two non-trivial applications of independent interest: (i) a strongly adaptive Parallel Broadcast (PBC) under standard PKI with near-quadratic communication and logarithmic rounds, whereas all existing subcubic solutions (Gelles et al. CRYPTO'25, Civit et al. PODC'24) require at least linear rounds; (ii) a strongly adaptive ``general-purpose'' DKG for field-element secrets with O(lambdakappa n^2log n) communication and O(kappalog n) rounds (assuming memory erasures), fully compatible with legacy threshold schemes (BLS, Schnorr, ElGamal), improving upon (Feng et al. PODC'24), which requires O(lambdakappa n^{2.5} log n) communication and O(n) rounds. Our core is a new design methodology, which we call Circular Dragon. This extends the Dragon method (PODC'24) that was originally developed for sub-cubic communication DKG protocols but with linear rounds, by further reducing the round complexity.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2534) | 2026-10-19
