---
title: "Nowhere Man: Device Binding for Post-Quantum Anonymous Credentials"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2472"
summary: "Anonymous credentials are seeing widespread deployment. Notably, the European Commission plans to roll out age-verification solutions based on anonymous credentials by the end of 2026. Similarly, Goog"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Anonymous credentials are seeing widespread deployment. Notably, the European Commission plans to roll out age-verification solutions based on anonymous credentials by the end of 2026. Similarly, Google open-sourced Longfellow, a zero-knowledge proof system that lifts the standardized mobile Driver License framework into a full-fledged anonymous credentials, and is currently being integrated with Google Wallet. Any secure deployment of anonymous credentials must address two major challenges: 1) provide guarantees against credential sharing, and 2) support proof-of-personhood. The standard approach adopted by the industry to address both is device binding, which is mandatory for mDL and was only recently formalized for anonymous credentials by Friedrichs et al. (Eurocrypt '26). Simply put, the idea is to have the user's phone Secure Element sign a fresh challenge from the verifier, and to prove knowledge of this signature in zero-knowledge at each credential presentation. To date, all existing approaches, including Vega (S&P '26), have only considered non-post-quantum solutions based on legacy signature schemes. Crucial for near-term deployments and adoption is to work with standardized post-quantum signature schemes, such as ML-DSA, which were not designed for privacy. Because of this, solutions based on general non-interactive zero-knowledge proof systems (e.g., Longfellow) appear to be needed. This genericity, however, requires proving complex statements, significantly impacting proving time. In this work, we present a modular device binding protocol tailored to work with ML-DSA. We avoid the pitfalls of the generic approach by leveraging the structure of ML-DSA resulting in an efficient solution, but retaining the security underlying the post-quantum standard. Our most efficient variants additionally rely on a weak-MLWR assumption for unlinkability, which can be removed at the cost of lower efficiency. While tailored for ML-DSA and requiring no modification to the FIPS~204 signing interface, our solution is modular enough to be integrated with different anonymous credential schemes, allowing real-world solutions to pick the most efficient building blocks. To demonstrate the feasibility of our solution, we provide a proof-of-concept implementation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2472) | 2026-10-14
