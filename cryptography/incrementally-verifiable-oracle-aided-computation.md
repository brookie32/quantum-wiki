---
title: "Incrementally Verifiable Oracle Aided Computation"
date: "2026-11-08"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2824"
summary: "Incrementally verifiable computation (IVC) allows a prover to maintain a short proof that can be efficiently updated after each computation step, without retaining or recomputing the preceding executi"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Incrementally verifiable computation (IVC) allows a prover to maintain a short proof that can be efficiently updated after each computation step, without retaining or recomputing the preceding execution. In the context of AI safety, the need for incremental verification is particularly important, as AI systems interact with users over time and perform further computation after each interaction. However, standard IVC schemes do not directly address a crucial feature of AI tasks: their dependence on external information and expertise. Indeed, the UK AISI Alignment Team~ite{IrvingM25} emphasizes that verification methods for AI safety should accommodate access to external information and human judgment. This is the topic of this paper. We construct IVC schemes for {em oracle-aided} computations under the Learning with Errors (LWE) assumption by first constructing succinct non-interactive arguments (SNARGs), and then extending them to the incremental setting. We consider the following two settings, where below, lambda is the security parameter, n is the input length, and T, S, and Q are the time, space, and oracle-query bounds. egin{itemize} item extbf{Robust computations.} For bounded-space computations, including non-deterministic computations, in which every accepting purported execution on a false input contains at least an arepsilon-fraction of incorrect oracle answers, we construct {em privately verifiable} SNARGs and IVC. For IVC, the corresponding robustness condition is imposed on the claimed configuration. Public parameters, private verification keys, and proofs have length poly(lambda,S,log T,1/arepsilon), and verification uses O(lambda/arepsilon) oracle calls. We complement this result with a lower bound ruling out (deterministic) publicly verifiable SNARGs and IVCs with public parameters of length o(n), and o(Q) verifier oracle queries. item extbf{Signed oracles.} For oracles that digitally sign their query-answer pairs, we construct publicly verifiable SNARGs and IVC without a robustness assumption, and with oracle-free setup and verification. Public parameters and proofs have length poly(lambda,S,log T). For deterministic computations with oracle query and answer lengths poly(lambda,log T), we remove the dependence on S, obtaining public parameter and proof lengths poly(lambda,log T). end{itemize} All our constructions have adaptive completeness and soundness. Sub-exponential hardness of LWE suffices for all constructions; polynomial hardness suffices in the deterministic signed-oracle setting when T is polynomially bounded in lambda. All cryptographic assumptions are required to hold even given access to the underlying oracle.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2824) | 2026-11-08
