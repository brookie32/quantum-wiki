---
title: "Toward Secure Compilation: Leakage Detection for Masked Implementations in Jasmin"
date: "2026-08-15"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1696"
summary: "Masking is a well-established software countermeasure against side-channel attacks, yet even algorithmically correct masked implementations can leak on real hardware once the compiler has performed in"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

Masking is a well-established software countermeasure against side-channel attacks, yet even algorithmically correct masked implementations can leak on real hardware once the compiler has performed instruction selection, register allocation, and stack allocation. Existing approaches either rely on leakage simulation, which is tied to a specific power model and computationally expensive, or on formal verification of the source program, which does not capture the effects introduced by the subsequent compilation stages. We address this gap from within the compiler and propose a leakage detection pass for the Jasmin language, integrated into its formally verified pipeline and operating on the intermediate representation before register and stack allocation. Rather than simulating power traces, the pass implements a configurable, microarchitecture-oriented leakage model that tracks the contact between shares, secrets, random values, and public values, making the root causes of the detected leakage explicit and enabling the detection of masking-order reductions. We validate the pass on 60 dedicated Jasmin test snippets covering all considered leakage sources and category combinations, and intend it as the foundation for a subsequent compiler stage that automatically removes the detected leakage, thus constituting a first step toward secure compilation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1696) | 2026-08-15
