---
title: "Vespa: Efficient Secure Aggregation with Integrity Defense under Server Privacy"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2183"
summary: "Secure aggregation with input validation enables a server to securely compute the summation of private data from multiple clients while verifying that the inputs satisfy specific constraints. However,"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Secure aggregation with input validation enables a server to securely compute the summation of private data from multiple clients while verifying that the inputs satisfy specific constraints. However, the practical deployment of this paradigm at scale is hindered by two primary limitations. First, existing schemes suffer from severe efficiency bottlenecks due to their reliance on generic, computationally expensive zero-knowledge proofs (ZKPs). Second, the scope of input validation is currently restricted to norm checks (e.g., L_2 and L_infty) against public bounds. This paper presents extsf{Vespa}, a single-server secure aggregation scheme that simultaneously achieves practical efficiency and expands validation capabilities to support both extit{norm checks against public bounds} and extit{similarity checks against private server inputs}. Specifically, we design a novel validity-weighted secure aggregation protocol over committed inputs, built upon highly efficient vector oblivious linear evaluation (VOLE). To efficiently realize input validation, we introduce customized L_2 and L_infty norm checks based on VOLE-based ZKPs, centered around optimized range proofs with reduced range sizes. Furthermore, we extend our framework to support advanced similarity-based checks against private server inputs, instantiated with widely used Euclidean and cosine similarities. This allows extsf{Vespa} to first filter out invalid inputs using norm checks, followed by performing fine-grained validation via similarity metrics. We compare our scheme with the state-of-the-art secure aggregation works, including RoFL (S&P 2023), ACORN (USENIX Security 2023), and Armadillo (CCS 2025), and extensive evaluation shows that our L_2 and L_infty norm checks achieve runtime improvements of up to 2sim 3 and 1sim 3 orders of magnitude, respectively. Our similarity checks also achieve practical performance, consuming only around 94 seconds for an 818k-entry vector.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2183) | 2026-09-23
