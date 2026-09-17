---
title: "New Pseudorandom Correlation Functions and Exponent VRFs from DCR"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2030"
summary: "Pseudorandom correlation functions (PCFs) allow two parties to expand short correlated keys into an unbounded, locally evaluatable source of correlated randomness. In this paper, we give the first con"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Pseudorandom correlation functions (PCFs) allow two parties to expand short correlated keys into an unbounded, locally evaluatable source of correlated randomness. In this paper, we give the first constructions of PCFs for correlated oblivious transfer (COT) and vector oblivious linear evaluation (VOLE) correlations over Z_M for an arbitrary modulus M, with reasonable concrete efficiency. Our construction comes with a lightweight, two-round distributed setup protocol, and relies solely on the decisional composite residuosity (DCR) assumption. As part of our security analysis, we introduce a new family of extended power DDH problems over subgroup indistinguishability groups, and give a novel master theorem showing that this is implied by standard DCR. This suffices to prove security of our PCF based on DCR, and also implies that prior constructions relying on related power-DDH style assumptions in composite groups can be based on DCR alone. We further extend our construction to obtain a PCF for oblivious linear evaluation (OLE) and general degree-two correlations over F_2. As an application of our PCF for VOLE, we derive a designated-verifier exponent-verifiable random function (eVRF), where the publicly verifiable output is the VRF output in the exponent. As an independent contribution, we additionally give a publicly verifiable eVRF from an offline/online variant of homomorphic secret sharing. Both of these constructions have much shorter proof sizes than prior work.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2030) | 2026-09-14
