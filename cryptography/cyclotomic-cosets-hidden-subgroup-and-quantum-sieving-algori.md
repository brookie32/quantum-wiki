---
title: "Cyclotomic Cosets: Hidden Subgroup and Quantum Sieving Algorithm for Prime-Power Moduli"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2249"
summary: "The Learning With Errors (LWE) problem is a fundamental assumption in post-quantum cryptography. Regev established a quantum reduction from LWE to the Dihedral Coset Problem (DCP). Later, Brakerski et"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

The Learning With Errors (LWE) problem is a fundamental assumption in post-quantum cryptography. Regev established a quantum reduction from LWE to the Dihedral Coset Problem (DCP). Later, Brakerski et al. introduced the Extrapolated Dihedral Coset Problem (EDCP), proving its equivalence to LWE. However, unlike DCP, EDCP no longer admits a coset structure. This limits the direct application of techniques for hidden subgroup problems. In this work, we introduce the Cyclotomic Coset Problem (CCP), a cyclotomic generalization of DCP that preserves an exact hidden-subgroup structure. Let zeta_p be a primitive p-th root of unity, let pi=zeta_p-1, and write q=p^t and L=t(p-1). We work over R_q=mathbb Z_q[zeta_p] ong mathbb Z[zeta_p]/(pi^L), where the isomorphism follows from the total ramification identity (p)=(pi)^{p-1}.We exploit the resulting pi-adic ideal chain to construct a quantum sieve that successively reduces phase states modulo pi^{L},pi^{L-1},ldots,pi. For every fixed prime p and modulus q=p^t, our algorithm solves the CCP in time and sample complexity 2^{O_p(log nlog q)}, using polynomial quantum space. The sieve also applies to uniform EDCP and Gaussian Sket{ext{LWE}}, yielding quasi-polynomial time algorithms for all the above problems when q=ext{poly}(n). This extends the power-of-two EDCP sieve of Bai et al. (CRYPTO 2025) to a cyclotomic setting. However, we emphasize that our result does not, by itself, yield a quasi-polynomial-time algorithm for standard LWE, because the currently known reduction produces only a limited number of approximate CCP states.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2249) | 2026-09-28
