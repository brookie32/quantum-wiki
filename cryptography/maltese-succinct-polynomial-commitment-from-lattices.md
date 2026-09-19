---
title: "Maltese: Succinct Polynomial Commitment from Lattices"
date: "2026-09-17"
updated: "2026-09-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2067"
summary: "Succinct polynomial commitment schemes are a key building block in succinct non-interactive arguments of knowledge (SNARKs). Existing succinct lattice-based polynomial commitment schemes take a 'split"
last_verified: "2026-09-19"
review_by: "2026-12-18"
stale: false
---

Succinct polynomial commitment schemes are a key building block in succinct non-interactive arguments of knowledge (SNARKs). Existing succinct lattice-based polynomial commitment schemes take a "split-and-fold" strategy making use of homomorphism to compress proof size to O(ext{polylog} N) for polynomials of size N. Prior works either (1) incur superlogarithmic verifier work (e.g., O(sqrt{N})), (2) incur concretely large proof sizes and verifier work (e.g., hundreds of MB), or (3) rely on non-standard lattice assumptions. We proprose a new succinct polynomial commitment scheme Maltese that operates over a Merkle tree commitment of the lattice-based Ajtai hash function. We employ a folding strategy and propose new sum-check-based reductions for managing norm growth of the tree commitment over folding rounds. Maltese is secure under the standard Module-SIS assumption and produces opening proofs of 335KB for multilinear polynomials of size N=2^{30}; proofs are around 300imes smaller than prior work with polylogarithmic verifier complexity but between 2-6imes larger than prior work with larger verifier complexity or stronger structured assumptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2067) | 2026-09-17
