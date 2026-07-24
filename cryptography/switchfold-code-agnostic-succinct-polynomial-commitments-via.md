---
title: "SwitchFold: Code-Agnostic Succinct Polynomial Commitments via Recursive Code Switching"
date: "2026-07-21"
updated: "2026-07-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1489"
summary: "We study large-scale, field-agnostic, hash-based polynomial commitment schemes (PCSs) with the goal of minimizing prover time while preserving polylogarithmic proof size and verifier time. This settin"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

We study large-scale, field-agnostic, hash-based polynomial commitment schemes (PCSs) with the goal of minimizing prover time while preserving polylogarithmic proof size and verifier time. This setting is motivated by advanced applications of zero-knowledge succinct non-interactive arguments of knowledge (zkSNARKs) such as zero-knowledge machine learning (zkML), where committed polynomials may encode billions of parameters and large prime fields are desirable for avoiding wraparound in fixed-point arithmetic. We introduce SwitchFold, a generic construction of a hash-based multilinear PCS from any sequence of linear codes with geometrically increasing block lengths. The polylogarithmic proof size and verifier time do not rely on any specific algebraic structure of the codes, while the linear prover time follows solely from the linear encoding time. At its core, SwitchFold recursively applies the code-switching technique (Ron-Zewi and Rothblum, JACM ’24), reducing each multilinear extension (MLE) claim under one code to a simpler MLE claim under a shorter code. The generator-matrix MLE claims produced by code switching are accumulated across repeated PCS openings using an accumulation scheme (Bünz et al., TCC ’20), and are then proved through a final recursion. We instantiate SwitchFold with the Brakedown code sequence (Golovnev et al., CRYPTO ’23), whose recursive code structure aligns naturally with our framework; we call the resulting scheme BrakeFold. In contrast to prior code-switching PCSs such as Blaze (Brehm et al., EUROCRYPT ’25) and BrakingBase (Nair et al., ASIACRYPT ’25), SwitchFold does not require an auxiliary foldable code. At the scale of one billion coefficients and 100-bit security, the marginal cost of each additional PCS opening in BrakeFold yields 3.5× smaller proof size and 20.6× faster verification than Brakedown, with only a 1.3× increase in prover time. Its succinctness matches that of BaseFold (Zeilberger et al., CRYPTO ’24), while reducing prover time by 17.0×.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1489) | 2026-07-21
