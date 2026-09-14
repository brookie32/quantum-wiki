---
title: "Bounded Information: PAC Certification of Multivariate Side-Channel Traces"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1990"
summary: "Side-channel leakage certification aims to quantify what an attacker can learn about a secret variable from observed leakage. Existing information-theoretic estimators, such as perceived information ("
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Side-channel leakage certification aims to quantify what an attacker can learn about a secret variable from observed leakage. Existing information-theoretic estimators, such as perceived information (PI), hypothetical information (HI), and nonparametric mutual information (MI), aim to quantify distributional leakage, but they become unstable in high-dimensional traces and do not provide a finite-sample certificate of the best attacker. We introduce Bounded Information (BI), a probably approximately correct (PAC)-style finite-sample certification method that upper-bounds the exact-recovery success of a fixed attacker scope on unseen traces. The attacker suite certificate, BI^{suite}, applies a KL-binomial confidence interval with a union bound over a fixed suite that contains every trained attacker, preprocessing choice, and hyperparameter. BI therefore turns standard profiled-attack evaluation into an auditable certificate with an explicit attacker scope and confidence level. We further define BI^{loc}(arepsilon) to bound the recovery success of attackers whose normalized scores differ by at most arepsilon from those of a model in the suite. Across eight side-channel benchmarks with trace dimensions up to 7{,}000, BI provides stable certificates without density estimation, and its tightness diagnostics tell an evaluator whether a certified value is a genuine measurement of leakage or a conservative bound that more attack traces would tighten.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1990) | 2026-09-12
