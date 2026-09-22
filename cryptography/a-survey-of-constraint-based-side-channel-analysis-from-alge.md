---
title: "A Survey of Constraint-Based Side-Channel Analysis: From Algebraic Attacks to Exact Probabilistic Inference"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2125"
summary: "Over the last fifteen years, side-channel analysis (SCA) against implementations of both classical and post quantum cryptography has undergone a quiet but fundamental change of paradigm: from treating"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Over the last fifteen years, side-channel analysis (SCA) against implementations of both classical and post quantum cryptography has undergone a quiet but fundamental change of paradigm: from treating leakage as evidence to be combined with an algorithm’s structure into a system of exact equations to be solved, to treating it as evidence to be combined into a joint probability distribution to be queried. This survey gives a systematic account of that evolution through four paradigms: Algebraic SCA (ASCA), which encodes leakage as hard Boolean or algebraic constraints and solves the resulting system with SAT or Gröbner-basis solvers; Tolerant/weighted Algebraic SCA (TASCA), which relaxes hard constraints into pseudo-Boolean costs and recovers a maximum-a-posteriori key via combinatorial optimization; Soft Analytical SCA (SASCA), which retains leakage as full likelihood functions attached to a factor graph and approximates the posterior with loopy belief propagation; and Exact SASCA (ExSASCA), which replaces the uncertified approximation of loopy belief propagation with exact inference on a knowledge-compiled tractable probabilistic circuit. Our central contribution is a single Bayesian factor-graph formulation under which all four paradigms are shown to be different representations of the same leakage-augmented joint distribution combined with different inference queries and solvers: we prove, in a precise but lightweight sense, that ASCA is the zero-temperature limit of TASCA, that TASCA is a maximum-a-posteriori restriction of SASCA’s model, and that ExSASCA is SASCA with its approximate solver replaced by an exact one on the identical graphical model. Building on this formulation, we develop a taxonomy that organizes the literature along a representation axis (hard, weighted, probabilistic) and a solver axis (satisfiability, combinatorial optimization, approximate message passing, exact tractable inference), survey the concrete attack literature in each paradigm on both AES and NTT-based post-quantum schemes (Kyber, Dilithium, Falcon/FN-DSA), and analyze the computational and security trade-offs of each approach, including its implications for what a security evaluator may soundly conclude from a failed attack. We close with open problems at the current frontier of tractable probabilistic inference for cryptographic implementation security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2125) | 2026-09-20
