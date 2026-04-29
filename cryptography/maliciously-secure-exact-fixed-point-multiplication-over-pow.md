---
title: "Maliciously Secure Exact Fixed-Point Multiplication over Power-of-Two Rings for Replicated 3PC"
date: "2026-04-27"
updated: "2026-04-29"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/822"
summary: "Exact fixed-point multiplication over Z_{2^k} is a fundamental primitive for secure fixed-point arithmetic. However, in the honest-majority, maliciously secure 3PC setting, no prior work simultaneousl"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

Exact fixed-point multiplication over Z_{2^k} is a fundamental primitive for secure fixed-point arithmetic. However, in the honest-majority, maliciously secure 3PC setting, no prior work simultaneously provides cross-ring compatibility, exact semantics, and malicious security within this efficient framework. In this paper, we address this gap by showing that the core cross-ring bottlenecks, namely exact signed truncation and signed extension, share a unified algebraic structure. Based on this insight, we propose a general extbf{quotient-correction framework} that reduces complex non-linear cross-ring operations to a highly efficient extbf{2-bit bounded-quotient extraction} problem. We instantiate this framework to construct maliciously secure protocols for exact truncation and extension. By sequentially composing these primitives with standard in-ring multiplication, we realize the first end-to-end exact fixed-point multiplication protocol that satisfies all aforementioned requirements in the replicated 3PC setting. We also present optimized variants under relaxed guarantees (e.g., 1-ULP error) that offer superior performance trade-offs. We formalize our constructions within the Universal Composability (UC) framework and provide rigorous security proofs. Theoretical analysis and experimental results demonstrate that our approach achieves practical online efficiency while maintaining exact semantics and malicious security, overcoming the limitations of prior baselines regarding security assumptions, input domains, or output precision.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/822) | 2026-04-27
