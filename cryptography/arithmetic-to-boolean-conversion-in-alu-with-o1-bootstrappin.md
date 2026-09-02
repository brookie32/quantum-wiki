---
title: "Arithmetic-to-Boolean Conversion in ALU with O(1) Bootstrapping via Overflow Cancellation"
date: "2026-08-31"
updated: "2026-09-02"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1840"
summary: "Arithmetic logic unit (ALU) can combine word-level arithmetic with bit-level logic on encrypted machine words. Triangle encoding provides a CKKS-based representation for leveled word arithmetic, but i"
last_verified: "2026-09-02"
review_by: "2026-12-01"
stale: false
---

Arithmetic logic unit (ALU) can combine word-level arithmetic with bit-level logic on encrypted machine words. Triangle encoding provides a CKKS-based representation for leveled word arithmetic, but its existing arithmetic-to-Boolean (A2B) conversion recovers only one window per bootstrapping. Consequently, converting an (ell)-bit message requires (Theta(ell)) sequential functional-bootstrapping on the critical path of each input ciphertext. We first extend Triangle encoding from binary to general digit bases, allowing a larger base to shorten each Triangle word and increase the number of packed words per ciphertext. We then introduce shared overflow cancellation. For block modulus (B=d^omega) and bounded overflow (lvert I_krvert<B/2), a period-(B) functional bootstrap evaluates the remainders at all selected boundaries simultaneously, while the corresponding quotients are recovered by affine arithmetic. At consecutive boundaries, the current remainder and the preceding quotient contain the same shifted overflow coefficient. Their difference cancels this coefficient exactly and yields (v_i=D_i+c_{i-1}-Bc_i,) which contains only the block value (D_i) and its adjacent carry bits. All such values are available before any carry is resolved. The sign of this value determines carry behaviors, which obtained by functional bootstrapping. The corresponding transfer rules compose associatively, thus parallel carry propagation resolves all carries with (O(lceillog_2 ell rceil)) leveled multiplication depth. After carry correction, a final multi-value functional bootstrap extracts the bits of all blocks in parallel. The resulting A2B conversion has three sequential functional bootstrap stages per input ciphertext, independent of (ell), and requires no cross ciphertext batching. We implement the proposed A2B conversion in OpenFHE and evaluate it for 64-, 128-, and 256-bit words. In a same-machine, single-threaded comparison with Gao--Zheng, base (d=2) achieves the lowest single ciphertext latency, yielding (2.55imes)--(6.25imes) speedups. Base (d=4) packs more words into each ciphertext and achieves the best amortized performance, yielding (4.00imes)--(8.71imes) speedups.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1840) | 2026-08-31
