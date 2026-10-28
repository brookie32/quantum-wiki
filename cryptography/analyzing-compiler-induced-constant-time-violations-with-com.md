---
title: "Analyzing Compiler-induced Constant-time Violations with Compiler at Scale"
date: "2026-10-26"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2653"
summary: "The constant-time programming policy is a de facto standard for cryptographic libraries to prevent timing side-channel attacks. However, compiler optimizations may break constant-time source code duri"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

The constant-time programming policy is a de facto standard for cryptographic libraries to prevent timing side-channel attacks. However, compiler optimizations may break constant-time source code during compilation. Systematically preventing this requires understanding where a violation arises, how it is introduced, and which compiler configurations are problematic. Existing approaches analyze a single compilation point, either the final binary or one intermediate representation, and thus only partially answer the three questions. We propose CTGREP, a compiler-based framework that answers all three questions by applying differential analysis across the entire compilation chain. We use CTGREP to analyze seven complete cryptographic libraries across three Clang versions, six target platforms, and thousands of compiler configurations. We systematically detect compiler-induced constant-time violations in the wild and collaborate with library developers to address 48 cases. We further identify seven new problematic LLVM passes, bypass and improve the state-of-the-art compiler-flag-based mitigation. Finally, we quantify how the compiler version, target platform, and optimization configuration affect the violations. By covering entire libraries across the full compilation chain, CTGREP effectively detects remaining compiler-induced constant-time violations and complements the community's ongoing hardening efforts.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2653) | 2026-10-26
