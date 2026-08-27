---
title: "Beyond Linear Subspace Trails: Nonlinear Subspaces for Grobner Basis Attacks on Poseidon/Poseidon2 and Neptune"
date: "2026-08-24"
updated: "2026-08-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1792"
summary: "Poseidon/Poseidon2 and Neptune are prominent primitives for zero-knowledge proof systems. Their arithmetic circuit cost is reduced mainly through partial S-box layers and low-degree finite field opera"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

Poseidon/Poseidon2 and Neptune are prominent primitives for zero-knowledge proof systems. Their arithmetic circuit cost is reduced mainly through partial S-box layers and low-degree finite field operations. Algebraic attacks are therefore a central part of their security analysis, and Grobner basis methods are a main tool for studying such attacks. For such attacks, controlling the algebraic degree of the polynomial systems induced by partial rounds is a central issue. Previous work has shown that linear subspace trails can reduce the algebraic degree of partial rounds in constrained-input-constrained-output (CICO) problems. Therefore, subspace analysis has become an important tool for evaluating the algebraic security of Poseidon-like permutations. The main contribution of this paper is to extend the existing linear subspace trail framework to nonlinear subspaces. More precisely, we first introduce a parametric Macaulay matrix method. This method transforms the search for algebraic constraints that reduce degree growth into the problem of solving a parametric system. It provides a general algebraic approach for constructing longer nonlinear subspace trails that suppress degree growth over more internal partial rounds. Second, for the CICO problem with Ec extra constraints, we give a concrete constraint pattern that extends a linear subspace trail into a nonlinear one. In this nonlinear construction, the first Ec subspace constraints generate an ideal, and further compatible subspace constraints can be added along the chain without enlarging this ideal. As a result, the nonlinear subspace trail can cover up to 2Ec internal rounds, whereas the previous linear subspace trail can cover up to Ec rounds. We further show that the balancing matrix required by this construction is generically nonsingular. Furthermore, we propose subspace modeling variants without variable substitution. These variants impose linear or nonlinear constraints directly on high-degree intermediate states. For the Poseidon/Poseidon2 and Neptune instances proposed by Grassi et al. in ToSC 2025, our experiments show that, under the same complexity bound and the same Grobner basis cost model, the nonlinear subspace model can analyze approximately twice as many internal partial rounds as the linear subspace model considered in ToSC 2025. For several concrete instances, our method reaches or even exceeds the recommended number of internal rounds given by the designers in sponge mode or compression mode.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1792) | 2026-08-24
