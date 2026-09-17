---
title: "Maliciously Secure Shuffled Distributed OPRF with Applications to Private Set Operations"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2035"
summary: "Private Set Intersection (PSI) enables two parties to compute the intersection of their private sets without revealing any additional information. For plain PSI, there exist extremely efficient soluti"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Private Set Intersection (PSI) enables two parties to compute the intersection of their private sets without revealing any additional information. For plain PSI, there exist extremely efficient solutions based on symmetric-key techniques for both the semi-honest and malicious settings. However, for more enriched set operations such as PSI-Cardinality, PSI-Sum, Circuit-PSI, and Private Set Union, the efficiency gap between the semi-honest and malicious settings is significant, often spanning orders of magnitude. A key bottleneck underlying these protocols is the need for a shuffled distributed oblivious pseudorandom function (SH-DOPRF) with malicious security. Existing constructions for this primitive are asympotically suboptimal and/or concretely inefficient. In this work, we present a new protocol for SH-DOPRF with malicious security that achieves linear computation and communication complexity. We present two instantiations: a DDH-based construction using the Dodis-Yampolskiy PRF (PKC 2005), and a plausibly post-quantum secure construction based on a variant of the Dark-Matter PRF (Aranha et al., S&P 2026). Our approach is almost entirely based on symmetric-key techniques, with public-key operations used only for evaluating PRF outputs. This primitive yields maliciously secure protocols for multi-query reverse private membership test (Zhang et al., USENIX Security 2023), which in turn can be used to realize the aforementioned private set operations. These protocols provide two-sided outputs while only additionally leaking the cardinality of the intersection. We implement and evaluate our construction to demonstrate concrete efficiency. Our DDH-based maliciously-secure SH-DOPRF achieves a 2--3 orders of magnitude improvement in total running time compared to the state-of-the-art (Miao et al., CRYPTO 2020 & Yang et al., PoPETs 2025), leading to a similar improvement for PSI-Cardinality. The resulting protocols for various other private set operations also achieve significant improvements over prior work; for example, our PSI-Sum and Circuit-PSI protocols are 1--2 orders of magnitude more efficient.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2035) | 2026-09-15
