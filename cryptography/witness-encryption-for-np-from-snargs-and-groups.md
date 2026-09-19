---
title: "Witness Encryption for NP from SNARGs and Groups"
date: "2026-09-16"
updated: "2026-09-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2063"
summary: "We construct the first witness encryption for NP in the generic group model from succinct non-interactive arguments (SNARGs) for NP. Our construction applies to any SNARG with subexponential soundness"
last_verified: "2026-09-19"
review_by: "2026-12-18"
stale: false
---

We construct the first witness encryption for NP in the generic group model from succinct non-interactive arguments (SNARGs) for NP. Our construction applies to any SNARG with subexponential soundness and polylogarithmic online verification time after input preprocessing. Central to our result is the first Karp-Levin reduction from satisfiability for circuits of size polylog(lambda) to the minimum-distance problem for linear codes (GapMDP) over a prime field of size lambda^{omega(1)}, with an approximation factor of omega(log lambda), where lambda is the security parameter. We obtain this reduction by adapting Hair and Sahai's recent hardness result for GapSVP. Combining our reduction with the witness encryption framework due to Barta, Ishai, Ostrovsky, and Wu [CRYPTO 2020], we obtain the first unconditional extractable witness encryption for circuits of size polylog(lambda) in the generic group model. These techniques may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2063) | 2026-09-16
