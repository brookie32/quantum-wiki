---
title: "Tighter  Nonuniform Trace Reductions from Ring-LWE to MP-LWE"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2151"
summary: "Middle-Product LWE (MP-LWE) can inherit hardness from Ring-LWE over many number fields. Peikert and Pepin developed a direct reduction using field traces. Njah Nchiwo and Pellet-Mary (NP26) proved pol"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Middle-Product LWE (MP-LWE) can inherit hardness from Ring-LWE over many number fields. Peikert and Pepin developed a direct reduction using field traces. Njah Nchiwo and Pellet-Mary (NP26) proved polynomial loss for the route through Polynomial-LWE under an additional condition on the defining polynomial. Recently, Pellet-Mary and Xia (PX26) unified both routes and proved polynomial loss for defining polynomials with polynomially bounded coefficients under suitable modulus conditions. We analyze Peikert and Pepin's trace reduction for monic irreducible integer polynomials f of degree nge2 with coefficients of absolute value at most a fixed Bge1. First, when the prime modulus satisfies qnmid[mathcal O_{Q(heta)}:Z[heta]], where heta is a root of f, we prove the existence of multipliers with primal loss O_B(nsqrt{log n/loglog n}) and dual loss O_B(n^2). The multipliers have polynomial-size descriptions and serve as advice. Second, whenever the polynomial class is nonempty, every Qge21 admits a prime qin[Q,2Q] for which the index condition holds for at least a 1-O_B(nlog n/Q) fraction of the polynomials. At the same prime, we prove the same lower bound when counting the distinct number fields defined by these polynomials. Both coverage bounds tend to one as noinfty if Q/(nlog n)oinfty. Third, we prove that the trace reduction can match the linear noise bounds achieved by NP26's reduction through Polynomial-LWE. For the same defining polynomial, Ring-LWE variant, and MP-LWE parameters, a suitable trace multiplier exists whose linear noise amplification is no larger than that achieved by NP26's multipliers.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2151) | 2026-09-22
