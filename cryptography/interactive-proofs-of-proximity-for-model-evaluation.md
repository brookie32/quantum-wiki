---
title: "Interactive Proofs of Proximity for Model Evaluation"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2217"
summary: "We study interactive proofs of proximity (IPP) for model evaluation: a resource-limited verifier interacts with an untrusted prover, typically the model owner, to certify statistical properties of a m"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

We study interactive proofs of proximity (IPP) for model evaluation: a resource-limited verifier interacts with an untrusted prover, typically the model owner, to certify statistical properties of a model under an unknown input distribution. Our formulation is shaped by the constraints of practical evaluation: it separates sampling the input distribution from querying the model and evaluating its output, allowing their costs and access patterns to be treated independently; it distinguishes real audit data (black-box sampling) from generated data (chosen-randomness, or gray-box, access to the sampler); and it allows the prover and the verifier to score outputs with different evaluators, as happens when scores come from human or judge models. We focus on doubly-sublinear mathsf{IPP}s, in which both the verifier and the designated honest prover use sublinear resources, and on (weighted) Hamming weight properties, which capture the expectation of a Boolean evaluation rule under an unknown distribution and, consequently, a broad range of model-evaluation statistics. As a first step, we give a tolerant mathsf{dsIPP} for ordinary Hamming weight. For completeness and soundness radii arepsilon_c <arepsilon_f and gap g=arepsilon_f-arepsilon_c, its logarithmic-round instantiation uses ilde{O}(1/g) verifier queries and O(1/g^2) honest-prover queries, improving the cubic dependence of Amir, Goldreich, and Rothblum [ITCS 2025]. We prove matching query lower bounds up to polylogarithmic factors. We then study distribution-weighted Hamming weight under several access models. Under black-box sampling, the verifier uses Theta(1/g^2) samples but only ilde{O}(1/g) evaluations, and we show that the quadratic sample complexity is necessary in the interior regime. With chosen-randomness access to a sampler, the problem reduces to ordinary Hamming weight, giving ilde{O}(1/g) verifier calls and evaluations. When the two parties' evaluators may disagree arbitrarily on a rho-fraction of the distribution and by up to gamma elsewhere, we give protocols that remain doubly sublinear whenever g exceeds twice the mean mismatch kappa = rho + (1-rho)gamma. Finally, we show how our technical results can improve the efficiency of model evaluation in natural motivating scenarios by shifting the bulk of the evaluation burden to the model owner while letting any number of auditors verify claims cheaply; we apply them to auditing criteria including accuracy, group fairness, calibration, harmlessness, usefulness, and average-case robustness.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2217) | 2026-09-25
