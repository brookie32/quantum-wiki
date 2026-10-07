---
title: "Rare-Event Decorrelation for Linear Tests of Low-Complexity Pseudorandom Functions"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2357"
summary: "Linear tests are a basic obstacle to pseudorandom functions built from low-depth circuits and secret linear or affine maps. Ball, Ducros, Erabelli, Kohl, Resch, and Scholl left open whether their boun"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Linear tests are a basic obstacle to pseudorandom functions built from low-depth circuits and secret linear or affine maps. Ball, Ducros, Erabelli, Kohl, Resch, and Scholl left open whether their bounded-query strong-PRF candidate in AC^0[2] resists general non-adaptive linear tests with polynomially many chosen queries. Boyle, Couteau, Gilboa, Ishai, Kohl, and Scholl left linear-attack resistance of their Sipser-based weak-PRF candidate open. We address both questions through a common correlation argument based on rare local events. Repeated Cauchy--Schwarz reduces the original correlation to a parity correlation of indicators of substantially rarer events while preserving the independence supplied by the underlying linear forms. Pairwise independence suffices to bound the resulting parity correlation by a constant below 1, while higher-order independence gives stronger cancellation. For the candidate of Ball et al., this resolves the open problem for arbitrary polynomially many non-adaptive queries with unrestricted linear or affine dependencies. More generally, for every fixed ain(0,1) and qle2^{a(log_2lambda)^2}, every such linear test has bias exp(-lambda^{1-a-o(1)}). For the Sipser-based family of Boyle et al., for every fixed 0<arepsilon<2, with overwhelming probability over Qle2^{(2-arepsilon)(log_2lambda)^2} random samples, every linear attack has bias exp(-lambda^{arepsilon-o(1)}). This establishes linear-attack resistance throughout this quasipolynomial-sample regime. Extending the guarantee to the conjectured subexponential weak-PRF regime remains open.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2357) | 2026-10-05
