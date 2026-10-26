---
title: "Mikros: Bitwidth-Aware SNARKs over Extensions of Small Fields"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2646"
summary: "Provers for succinct non-interactive arguments of knowledge (SNARKs) perform arithmetic over a large field for soundness, even when the witness entries are a few bits wide, which inflates both prover "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Provers for succinct non-interactive arguments of knowledge (SNARKs) perform arithmetic over a large field for soundness, even when the witness entries are a few bits wide, which inflates both prover time and memory usage. Recent work makes individual SNARK components bitwidth-aware, so that a lower witness bitwidth means faster proving and lower memory usage, but these techniques cover only part of the prover and exploit the structure of specific fields, typically binary ones. We introduce Mikros, a framework for end-to-end bitwidth-aware SNARK construction based on algebraic vector packing. We pack vectors of length (N=mkappa) over a base field (F) into length-(m) vectors over a degree-(kappa) extension field (E), which turns length-(N) relations over (F) into length-(m) relations over (E) and makes existing linear-time extension-field protocols bitwidth-aware. This technique thus unifies bitwidth-aware inner-product proofs, Hadamard-product proofs, and polynomial commitment schemes, previously obtained by separate constructions, and yields the first bitwidth-aware grand-product proof, hence the first bitwidth-aware permutation argument. Composing them gives bitwidth-aware SNARKs for circuit satisfiability over extensions of arbitrary small fields. For a single instance of circuit satisfiability, the prover cost is proportional to the effective bitwidth, the combined bitwidth of the witness entries and the wiring-position encodings; across instances of the same circuit, the position encoding is amortized and the per-instance cost is proportional to the witness bitwidth. Although Mikros does not rely on binary-field structure, its prover is (2.19imes), (2.55imes), and (1.85imes) faster on batches of (256) SHA-256 compressions, Keccak permutations, and BLAKE3 compressions than Flock (Bunz etal, IACR ePrint 2026), the state-of-the-art bitwidth-aware SNARK over binary-extension fields.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2646) | 2026-10-26
