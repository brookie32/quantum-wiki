---
title: "How to Fold Linear Error-Correcting Codes with Optimal Proximity Gaps"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2133"
summary: "Folding is a core technique in building efficient code-based polynomial commitment schemes with polylogarithmic proof size and verification. To date, there are two families of linear error-correcting "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Folding is a core technique in building efficient code-based polynomial commitment schemes with polylogarithmic proof size and verification. To date, there are two families of linear error-correcting codes that have been known to allow folding, i.e., Reed-Solomon (RS) codes and foldable codes. However, neither admits optimal proximity gaps, which constitutes a fundamental bottleneck in the resulting proof sizes. In this work, we give the first folding scheme that enjoys optimal proximity gaps. Specifically, we construct IOPPs (interactive oracle proofs of proximity) for both folded RS (FRS) codes and univariate multiplicity (UM) codes, which achieve optimal proximity gaps 1-R-arepsilon as shown in a recent work of Goyal and Guruswami (STOC 2026), where R is the code rate and 0<arepsilon<1-R. Our key observation is that the typical even/odd folding commutes with polynomial reduction for suitably paired moduli, enabling consistency checks via the Chinese remainder theorem. This implies a new generic folding framework that recovers the FRI folding for RS codes and enables efficient folding for FRS and UM codes. We further refine the optimal proximity gap analysis for FRS and UM codes, yielding tighter concrete soundness bounds. Our IOPPs have O(N) prover time and oracle proof size, together with O(lambdalog{N}) query complexity and verification time, where N is the block length and lambda is the security parameter. These bounds match the asymptotic complexity of FRI while attaining optimal proximity gaps and allowing smaller underlying fields at the same security level. E.g., a 128-bit field suffices for 100-bit security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2133) | 2026-09-21
