---
title: "Succinct Shortness Check Under a Few Kilobytes via Tensor Train Random Projections"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2146"
summary: "Range proofs are a fundamental building block of lattice-based proof systems. Existing approaches relying on standard Johnson-Lindenstrauss (JL) struggle to provide succinctness: unstructured JL incur"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Range proofs are a fundamental building block of lattice-based proof systems. Existing approaches relying on standard Johnson-Lindenstrauss (JL) struggle to provide succinctness: unstructured JL incurs linear verifier complexity, while structured JL introduced in RoK and Roll [ASIACRYPT'25] produce large projection vectors that need to be sent in costly committed form. For a witness of dimension m and a security parameter lambda, the JL projection vector is O(lambda), but the projection matrix is O(lambda m). Structured JL can be represented in widetilde O(rho lambda^2), but the resulting projection length grows to widetilde O(m / rho) for any trade-off parameter rho > 1. hspace{5mm} In this paper, we introduce Tensor Train Random Projection (TTRP) to lattice-based cryptography, offering a ``best of both world" structured JL variant. The Tensor Train (TT) matrix representation drops to widetilde O(lambda), while maintaining the projection vector at O(lambda). hspace{5mm} We show that TTRP can be seamlessly integrated into proof systems by linearizing the well-formedness of the projection with the sum-check protocol. Concretely, using TTRP + sum-check as a drop-in replacement for existing range proof techniques yields an approximate shortness check with O(lambda log m (loglog m)^2) verifier complexity and proof size around 4 KB for relevant parameter settings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2146) | 2026-09-22
