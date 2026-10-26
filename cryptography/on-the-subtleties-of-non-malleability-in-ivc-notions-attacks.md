---
title: "On the Subtleties of Non-Malleability in IVC: Notions, Attacks and Constructions from Falsifiable Assumptions"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2631"
summary: "We investigate non-malleable Incrementally Verifiable Computation (IVC), a subject that has received limited attention. We focus on whether and how simulation-sound IVC can be obtained from falsifiabl"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

We investigate non-malleable Incrementally Verifiable Computation (IVC), a subject that has received limited attention. We focus on whether and how simulation-sound IVC can be obtained from falsifiable assumptions. We provide additional evidence of the unique aspects of non-malleable incremental proofs, identifying definitional challenges in formalizing simulation-sound IVC, and showing how existing IVC designs from falsifiable assumptions cannot exhibit simulation-soundness "for free" (without modifications). In addition to a new family of definitions of simulation-sound IVC, our main results are the following. - A general negative result: common Valiant-style proofs are malleable. We isolate and formalize a feature shared by the dominant Valiant-style IVC designs (Valiant, TCC 2008) related to the ability to merge proofs together. We show that, assuming one-way functions, natural zero-knowledge versions of Valiant's design are malleable. As an implication of our framework of attacks, we show that the only IVC for NP from falsifiable assumptions (Datta et al., CRYPTO 2025) cannot satisfy any form of simulation-soundness; this is the case even when instantiating this scheme from non-malleable building blocks. - A positive result: first IVC from falsifiable assumptions with non-malleability features. We construct an IVC satisfying a non-trivial form of simulation-soundness under subexponential iO and either subexponential LWE or subexponential bilinear-map assumptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2631) | 2026-10-24
