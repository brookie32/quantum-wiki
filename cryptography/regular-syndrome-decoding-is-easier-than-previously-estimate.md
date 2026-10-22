---
title: "Regular Syndrome Decoding Is Easier Than Previously Estimated"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2563"
summary: "The Regular Syndrome Decoding (RSD) problem is a structured variant of classical Syndrome Decoding and underlies a growing number of efficient cryptographic constructions, including zero-knowledge pro"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

The Regular Syndrome Decoding (RSD) problem is a structured variant of classical Syndrome Decoding and underlies a growing number of efficient cryptographic constructions, including zero-knowledge protocols, pseudorandom correlation generators, and MPC-in-the-Head signatures. Although RSD is generally believed to be computationally hard, recent works have shown that algebraic attacks can outperform information-set decoding on important RSD parameter regimes. Building on this line of work, we revisit the concrete hardness of RSD and show that many widely used parameter sets are substantially easier to solve than previously estimated. This improvement stems from a refined hybrid-algebraic attack that exposes and removes a previously overlooked source of concrete complexity: the joint blockwise placement of zero-coordinate guesses and syndrome-based variable eliminations. Rather than treating the two guessing stages and linear elimination as largely separate choices, our method coordinates them across all regular blocks so that the guessing penalty is balanced while sufficient equations are retained for linearization. This gives a systematic block-balancing principle for the entire guess–reduce–solve pipeline. We reassess several RSD-based applications, including Ferret (CCS~2020), Wolverine (IEEE S&P~2021), and committed VOLE (CCS~2025). Our estimates place at least one parameter set per application below its 128-bit target, with losses approaching 67~bits. On PCG benchmarks, we improve previous best attack costs by up to 29.77 and 25.91~bits over non-binary and binary fields, respectively. Moreover, for the revised 128-bit PCG parameter sets of Liu et al. (EUROCRYPT~2024) evaluated here, estimated attack costs are all below 2^{111} field operations. These results substantially revise the concrete-security landscape of RSD and indicate that several existing parameter choices overestimate the hardness of their underlying RSD instances.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2563) | 2026-10-20
