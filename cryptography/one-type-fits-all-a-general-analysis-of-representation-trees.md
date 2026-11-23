---
title: "One Type Fits All: A General Analysis of Representation Trees for Subset Sum, LWE and Decoding"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2997"
summary: "The representation technique is the basis of the best known algorithms for random subset sum, of combinatorial attacks on small LWE keys and of information set decoding. It builds the solution in a se"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

The representation technique is the basis of the best known algorithms for random subset sum, of combinatorial attacks on small LWE keys and of information set decoding. It builds the solution in a search tree, the representation tree, whose analysis has so far required a combinatorial derivation by hand for every variant. We introduce a general analysis technique for any representation tree, which replaces this derivation by a few short entropy formulas and turns the whole analysis into one explicit optimization problem, so that a new variant needs no new analysis. This technique alone improves the asymptotic exponents for almost all applications we consider. We then extend this analysis by adding filters, known from nearest-neighbor search, to every level of the best known trees and optimize them jointly with all other parameters. Finally, we improve the filtering technique by partitioning the enumerated vectors into a sparse and a dense part, which lets the filters act in a more concentrated way, with significant gains especially for subset sum and LWE. Further, we reduce the number of optimization variables for the filters from quadratic to linear, which makes optimizations feasible that were previously out of reach. Heuristically, random subset sum is solved in time T=2^{0.2620n} and memory M=2^{0.2120n} instead of T=M=2^{0.2830n}, and LWE keys following the distribution used in Dilithium are recovered in time 2^{0.2954n} instead of 2^{0.378n}. We also obtain the fastest combinatorial algorithms for ternary LWE keys and LWE keys as in Kyber, the fastest algorithms for decoding over F_q for small qgeq3, ternary decoding with large weight, decoding with restricted errors and Lee metric decoding. Further, we improve on the best known algorithms for nearest-neighbor search over F_q and on the best known time-memory trade-offs for subset sum.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2997) | 2026-11-23
