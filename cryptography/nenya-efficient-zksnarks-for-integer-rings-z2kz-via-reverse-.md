---
title: "Nenya: Efficient zkSNARKs for Integer Rings Z/2kZ via Reverse Multiplication-Friendly Embeddings"
date: "2026-10-28"
updated: "2026-10-31"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2672"
summary: "Zero-knowledge succinct non-interactive arguments of knowledge (zkSNARKs) are powerful cryptographic tools for certifying the correctness of computations with short proofs, fast verification, and zero"
last_verified: "2026-10-31"
review_by: "2027-01-29"
stale: false
---

Zero-knowledge succinct non-interactive arguments of knowledge (zkSNARKs) are powerful cryptographic tools for certifying the correctness of computations with short proofs, fast verification, and zero-knowledge privacy guarantees. However, most existing zkSNARK schemes support arithmetic only over finite fields defined by large primes or their extensions. This creates substantial overhead when proving computations written in high-level programming languages, which typically operate on fixed-width integer types such as 32-bit and 64-bit integers. In this paper, we introduce Nenya, the first practical SNARK scheme that supports native arithmetic over the integer ring Z/2^kZ. At the core of Nenya are new reductions from rank-1 constraint systems (R1CS) over Z/2^kZ to constraints over Galois rings via reverse multiplication-friendly embeddings (RMFEs). We also design a polynomial commitment scheme based on suitable classes of error-correcting codes, which supports well-formedness checks and packing rotations on committed witnesses essentially for free, resulting in sublinear verifier time. Experimental results demonstrate that Nenya achieves strong concrete performance. For a rank-1 constraint system of size 2^{25} for data-parallel computations over 32-bit integers, Nenya achieves a prover time of only 4.8 seconds. This is four orders of magnitude faster than the state-of-the-art SNARK scheme over Z/2^kZ, and only 1.06imes slower than a SNARK over a field with the same number of constraints. For general computation, the prover time of Nenya is 34.6 seconds. Moreover, for proving pixel-level image transformations that arise in media-provenance workflows, such as filtering that operates natively modulo 2^8, Nenya proves the same computation 12imes faster than a field-based SNARK.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2672) | 2026-10-28
