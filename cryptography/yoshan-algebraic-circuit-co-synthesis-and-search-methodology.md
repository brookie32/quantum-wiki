---
title: "Yoshan: Algebraic-Circuit Co-Synthesis and Search Methodology of Hardware-Efficient S-Boxes"
date: "2026-10-14"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2488"
summary: "Choosing an S-box for a hardware-oriented cipher means balancing cryptanalytic quality (differential uniformity elta, linearity L, algebraic degree), circuit complexity (the number of AND gates and th"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

Choosing an S-box for a hardware-oriented cipher means balancing cryptanalytic quality (differential uniformity elta, linearity L, algebraic degree), circuit complexity (the number of AND gates and the AND depth D), and implementation cost (silicon area and, in masked designs, registers and fresh randomness). Under Boolean masking the non-linear gates dominate this cost and D sets the latency, so automated S-box searches have concentrated on quadratic permutations, which admit depth-1 circuits but make the algebraic degree of a cipher grow slowly. We present YOSHAN, a co-synthesis system that optimizes an S-box and its gate-level circuit together instead of fixing the lookup table first. It combines structural algebraic seeding (subfield towers, Feistel, Misty, and product-round Feistel constructions, affine wrappers, CCZ graph automorphisms, bilinear and shear seeds), cryptographically guided evolution of the circuit DAG by algebraic rewrites, a differentiable Piling-Up relaxation with Hungarian LSAP projection, and multi-level circuit optimization (SMT sub-DAG shaving, stage-preserving common-subexpression elimination, exact depth-1 SAT synthesis, and algebraic-structural inverse compilation) inside a quality-diversity archive across n in {5,6,7,8}. Every archived circuit is exported gate for gate to SystemVerilog and certified by exhaustive simulation and a Z3 miter. The archive holds 31,129 certified netlists covering 56 (n,elta,L,eg) profiles; three extended-affine invariants and an exact affine-equivalence solver split them into members of known classes (Category A) and permutations provably not extended-affine equivalent to any power map or to the cipher S-boxes we compare against (Category B, 15 benchmark classes mathsf{YSH}_{n,i}, 13 with stratified subspace-filtration degree spectra). All 30 reported S-boxes and their explicit inverses are synthesized gate-exactly in 45 nm CMOS, unmasked and as pipelined first-order DOM modules, and every benchmark circuit is traced to its seed and the search stage that shaped it. Results include a gate-exact AES-equivalent circuit at the optimal AND depth 3 (42 AND, 101 XOR) with an explicit depth-3 inverse (42 AND, 106 XOR), a 6-bit degree-5 permutation mathsf{YSH}_{6,5} (elta=6, L=24, boomerang uniformity eta=14) with 12 AND gates, a 5-bit quartic permutation mathsf{YSH}_{5,4} with 5 AND gates at depth 2 in both directions, and 8-bit degree-7 permutations with 28 and 18 AND gates. All forward and inverse circuits are compared with the best published implementations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2488) | 2026-10-14
