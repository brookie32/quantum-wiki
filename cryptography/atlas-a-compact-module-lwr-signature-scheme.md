---
title: "ATLAS: A Compact Module-LWR Signature Scheme"
date: "2026-10-03"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2323"
summary: "We present mathsf{ATLAS}, a lattice-based digital signature scheme built on the Fiat--Shamir with aborts paradigm, with security based on the hardness of the Module Learning with Rounding (mathsf{MLWR"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

We present mathsf{ATLAS}, a lattice-based digital signature scheme built on the Fiat--Shamir with aborts paradigm, with security based on the hardness of the Module Learning with Rounding (mathsf{MLWR}) problem. Unlike mathsf{Dilithium}'s mathbf{t} = mathbf{As}_1 + mathbf{s}_2 construction or mathsf{HAETAE}'s bimodal, hyperball-uniform instantiation, mathsf{ATLAS} derives its public key via deterministic rounding, mathbf{t} = lfloor frac{p}{q}mathbf{As}_1 rceil, eliminating the error term mathbf{s}_2 and the explicit noise sampling it requires. This reduces key-generation cost and secret-key storage, and removes a component that both mathsf{Dilithium} and mathsf{HAETAE} would otherwise need to support, while keeping mathsf{ATLAS} structurally close to mathsf{Dilithium} to inherit its well-studied design and cryptanalytic track record. mathsf{ATLAS} targets three classical security levels, 128, 256, and 512 bits, using the smallest feasible ring degree n and challenge weight kappa for each, with module dimensions (k,l) tuned per level. To our knowledge, this includes the first mlwr-based signature parameter set at the 512-bit level. mathsf{ATLAS} further adopts power-of-two moduli (e.g., q=2^{23}, p=2^{18}), replacing modular reduction with bitwise operations and removing rejection sampling from key parts of the scheme. Since such moduli preclude conventional NTT-based multiplication, we design a hierarchical Toom-Cook/Karatsuba decomposition with degree-8 schoolbook multiplication as its base case, accelerated via AVX2 vectorization and strided memory access. Finally, mathsf{ATLAS} supports both mathsf{SHAKE} and mathsf{KDF-SM3} as interchangeable symmetric back-ends, and we quantify the overhead of the mathsf{SM3}-based instantiation relative to mathsf{SHAKE}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2323) | 2026-10-03
