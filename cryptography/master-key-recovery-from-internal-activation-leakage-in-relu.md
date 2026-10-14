---
title: "Master-Key Recovery from Internal Activation Leakage in ReLU Realizations of Camellia"
date: "2026-10-13"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2458"
summary: "This paper investigates functional correctness and masterkey reconstruction in explicitly constructed rectified linear unit (ReLU) implementations of Camellia-128, Camellia-192, and Camellia-256. Exac"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

This paper investigates functional correctness and masterkey reconstruction in explicitly constructed rectified linear unit (ReLU) implementations of Camellia-128, Camellia-192, and Camellia-256. Exact neural realizations of Boolean gates, S-box selectors, and bit permutations provide a framework for reproducing Camellia on binary inputs. We present a component-wise correctness argument and report known-answer-test agreement for Camellia-128. We then analyze how selected whitening and round-key quantities determine the external master key through public key-schedule identities. Inverse rotations of suitable subkey pairs recover the required key components, whereas prewhitening-key recovery alone is insufficient for complete reconstruction of the longer keys. Under explicitly constructed synthetic internal-oracle access, symmetric real-valued perturbations identify target subkey bits, requiring 128 and 256 query pairs for the coordinate-wise Camellia-128 and Camellia-256 procedures, respectively. A separate Camellia-192 experiment validates deterministic key-schedule inversion under direct access to DNN-generated round keys. Across 1,000 independently sampled master keys per variant, all three procedures achieved exact recovery in every trial, yielding 3,000 successful recoveries out of 3,000 trials, with zero recovery failures and no Camellia-192 complement-consistency failures. These results validate conditional master-key reconstruction under the specified internal-access models and highlight the distinction between binary functional correctness and security under stronger access assumptions. They do not establish plaintext/ciphertext-only attacks against standard Camellia.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2458) | 2026-10-13
