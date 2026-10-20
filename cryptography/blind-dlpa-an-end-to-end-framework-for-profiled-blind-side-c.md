---
title: "Blind-DLPA: An End-to-End Framework for Profiled Blind Side-Channel Analysis"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2544"
summary: "Conventional profiled side-channel analysis generally assumes that the plaintexts or ciphertexts associated with target traces are available during key recovery. We consider a profiled blind setting i"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Conventional profiled side-channel analysis generally assumes that the plaintexts or ciphertexts associated with target traces are available during key recovery. We consider a profiled blind setting in which the attacker can obtain labeled traces from a profiling device using known inputs and keys, but observes only leakage traces from the target device. Under this setting, we propose Blind-DLPA, an end-to-end multi-task framework for {profiled blind side-channel analysis (profiled BSCA) that processes complete preprocessed trace windows} and jointly estimates the soft Hamming-weight posteriors of an input variable and a key-dependent intermediate variable. These posteriors are combined with pre-computed theoretical joint distributions to rank the key hypotheses, avoiding both manual {point of interest} (PoI) selection and a parameter-sensitive Gaussian label-error model. Evaluations on unprotected AES and Kyber demonstrate successful key recovery, while experiments on protected AES implementations show robustness to desynchronization and Boolean masking. To the best of our knowledge, Blind-DLPA provides the first reported profiled blind key recovery on the ASCAD dataset, reaching a guessing entropy of zero with 39 attack traces. Complementing these results, we revisit the Ascon Hamming-weight joint-distribution model adopted in prior work and identify previously overlooked collisions between key-dependent theoretical distributions that prevent unique key recovery under this model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2544) | 2026-10-19
