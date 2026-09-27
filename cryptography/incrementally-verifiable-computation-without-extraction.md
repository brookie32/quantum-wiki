---
title: "Incrementally Verifiable Computation without Extraction"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2219"
summary: "Incrementally verifiable computation (IVC) [Valiant, TCC '08] allows one to iteratively prove that a configuration x_0 reaches a configuration x_T via T repeated applications of a (possibly non-determ"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Incrementally verifiable computation (IVC) [Valiant, TCC '08] allows one to iteratively prove that a configuration x_0 reaches a configuration x_T via T repeated applications of a (possibly non-deterministic) machine M. An IVC scheme is fully succinct if the proof size is independent of both T and the size of the intermediate configurations. In this work, we develop a new indistinguishability obfuscation (iO)-based approach to IVC that avoids the extraction-based security analyses central to prior constructions. Assuming subexponential hardness of iO and one-way functions, we construct an adaptively sound fully succinct IVC scheme for deterministic computations. This yields the first IVC for deterministic computations that does not rely on algebraic assumptions. Under the same assumptions, we further obtain a fully succinct two-hop IVC scheme for mathsf{NP} with non-adaptive soundness, allowing one to prove that x_0 reaches x_2 via an intermediate configuration x_1. This is the first IVC scheme for mathsf{NP} achieving full succinctness. Our constructions are based on a new connection between IVC and secret sharing for s-t connectivity in graphs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2219) | 2026-09-25
