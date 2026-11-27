---
title: "Security Analysis of Homogeneous MQ-Based Post-Quantum Signature Schemes"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3056"
summary: "The security of multivariate cryptography relies on the hardness of solving the public multivariate quadratic (MQ) systems over finite fields. For a homogeneous MQ map P over F_q and a nonzero target "
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

The security of multivariate cryptography relies on the hardness of solving the public multivariate quadratic (MQ) systems over finite fields. For a homogeneous MQ map P over F_q and a nonzero target t, Ostuzzi recently introduced the target quotient that removes one equation from P(x)=t, and then each solution x of the resulting system has P(x)=bt for some bin F_q. This implies that a preimage of t can be recovered exactly when b is a nonzero square. In this paper, we first compare reoptimized direct and quotient costs using scheme-specific Wiedemann XL (WXL) gate-count estimates. The comparison covers Hashimoto's method on all 19 recommended UOV, SNOVA, and QR-UOV parameter sets, and Thomae-Wolf (TW) and Furue-Nakamura-Takagi (FNT) on the 13 characteristic-two sets. With the ideal retry multiplier 1/p_0(q), where p_0(q) is the acceptance probability for uniform b, nominal Hashimoto-WXL savings are 2.04-4.61, 1.81-3.20, and 0.05-2.44 bits, respectively. Over F_{256}, Hashimoto's quotient procedure recovered preimages in 640 of 1,000 reduced-parameter random UOV trials (64.0% overall), corresponding to 640 of 642 non-oil returns (99.69%), close to 255/256 (99.61%). Second, we establish an exact recovery law in the random UOV model with independent coefficients. Solvers may select solutions with arbitrary bias using only quotient equations and randomness independent of key generation. Averaged over keys and solver randomness, single-trial recovery probability equals p_0(q) times the valid non-oil return probability. With positive return probability, the residual conditional on return is uniform exactly when oil-space returns have probability zero; otherwise zero has excess mass and nonzero values remain equiprobable. We also derive finite recovery bounds under stated geometric candidate conditions and exhaustive residual-blind search; the FNT argument uses collinear-quadruple counting.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3056) | 2026-11-26
