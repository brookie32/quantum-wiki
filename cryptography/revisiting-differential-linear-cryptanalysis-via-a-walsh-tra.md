---
title: "Revisiting Differential-Linear Cryptanalysis via a Walsh-Transform Perspective"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2013"
summary: "Standard differential-linear (SDL) cryptanalysis has matured rapidly, now backed by the SDL connectivity table (SDLCT) framework, multi-round middle-part extensions, and automated CP-based search mode"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Standard differential-linear (SDL) cryptanalysis has matured rapidly, now backed by the SDL connectivity table (SDLCT) framework, multi-round middle-part extensions, and automated CP-based search models. The rotational differential-linear (RDL) variant lacks even an SDLCT counterpart, and the analogous combination of internal differentials with linear approximations, which we call internal differential-linear (IDL) cryptanalysis, has never been formulated. We unify SDL, RDL, and IDL in a single Walsh-transform framework on the difference transition function (DTF). Existing SDL machinery, including recent multi-round middle-part search models, transfers to RDL and IDL, yielding efficient correlation computation and distinguisher search. For ARX primitives, we derive a 2imes 2 matrix-product formula for the SDL and RDL correlations of a single modular addition. The formula exposes a rank-1 structure on the input-difference matrix that decouples the running product into independent factors, making a CP approximation with only linear inequalities and table lookups practical. This partially resolves the open problem of Niu et al. (CRYPTO 2022). We apply the framework to xoodoo-p, ascon-p, alzette, siphash, and specksixtyfour. For xoodoo-p, we obtain a 6-round RDL distinguisher and the first IDL distinguisher in the literature (both at 6 rounds). For ascon-p, the first RDL distinguisher (6 rounds). For alzette, an 8-round RDL distinguisher, doubling the previous 4-round best. For siphash, the longest known distinguisher (5 rounds). For specksixtyfour, the longest known SDL distinguisher (14 rounds).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2013) | 2026-09-14
