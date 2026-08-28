---
title: "Practical Silent Threshold Signatures and Silent Threshold Encryption for Dynamic Committees"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1820"
summary: "Silent threshold signatures (STS) and encryption (STE) enable threshold cryptography without interactive distributed key generation, allowing a group of N parties to non-interactively generate a joint"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Silent threshold signatures (STS) and encryption (STE) enable threshold cryptography without interactive distributed key generation, allowing a group of N parties to non-interactively generate a joint public signature verification key or an encryption key. However, modern distributed systems (such as Ethereum) rely on small, dynamically changing committees of size n ll N for efficiency, and existing silent threshold schemes either fail to support this dynamic setting or suffer from severe scalability issues. The only known STS construction for dynamic committees, Dyna-hinTS, requires an aggregation time of O(Nlog N) per epoch, tightly coupling the cost to the global system size rather than the small active committee. Furthermore, no STE scheme for dynamic committees has been proposed yet. In this work, we present practical silent threshold signature and encryption schemes for dynamic committees, bringing the aggregation cost down to strictly depend only on the committee size n. For signatures, we redesign the Dyna-hinTS framework by replacing its Plonk-style SNARKs with linear pairing checks and a new polynomial commitment for representing the committee, yielding an aggregation time of O(nlog^2n). We also introduce the first silent threshold encryption scheme for dynamic committees with matching efficiency. We further significantly optimize the silent setup phase common to prior STS and STE schemes, reducing each party’s one-time setup (i.e., generating the setup data, referred to as a "hint") cost from O(N^2) to O(N). We implement our schemes in Rust, and the results demonstrate practicality at scale. For a system parameterized with N = 2^{20} and n = 2^{10}, the per-party hint generation takes 197 seconds, and signature aggregation takes 0.153 seconds, achieving a >1900imes improvement over Dyna-hinTS. At the same time, our aggregated signature size, verification key size, and verification time remain constant.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1820) | 2026-08-27
