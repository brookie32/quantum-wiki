---
title: "LARK: Smaller and Faster Lattice-Based PRG"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3000"
summary: "A key challenge in designing practical lattice-based pseudorandom number generators (PRGs) is that such generators typically produce byte-oriented output, whereas lattice parameters do not necessarily"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

A key challenge in designing practical lattice-based pseudorandom number generators (PRGs) is that such generators typically produce byte-oriented output, whereas lattice parameters do not necessarily align with byte boundaries, creating a tradeoff between fully utilizing each computed value and maintaining efficient byte-oriented generation. To avoid additional packing overhead, LEAP (FSE 2025), a state-of-the-art lattice-based PRG built on Ring Learning with Rounding (RLWR), retains only the lowest eight bits of each RLWR value for byte-oriented generation and discards the remaining high-order bits. Consequently, this high-order information contributes neither to LEAP's output nor its security. We present LARK, a lattice-based pseudorandom generator that directly exposes the low-order byte as pseudorandom output and uses the discarded high-order information as security-relevant hidden uncertainty. This additional uncertainty allows LARK to meet its target security levels with smaller parameters, yielding compact keys and efficient implementations. To justify using the discarded high-order information as hidden uncertainty, LARK replaces LEAP’s RLWR-based output-generation component with one based on Ring Learning with Alternating Moduli (RLAM). For efficient polynomial arithmetic, we formulate RLAM as a ring analogue of the LAM problem introduced by Chen et al. (CRYPTO 2026), in which LWR rounding is replaced by direct reduction between coprime moduli. This modulus reduction introduces statistical bias, which LARK removes with lightweight masked rejection. We prove that LARK is pseudorandom under the decisional NTRU and RLAM assumptions. Compared with LEAP, LARK reduces key sizes by 42.85% and 68.00% at the 128-bit and 256-bit security levels, respectively, while consistently improving performance. LARK improves performance by up to 37.16% in plain C, 10.55% with AVX2, and 21.05% with AVX512. In particular, the AVX512 implementations achieve 0.90 and 0.91 cycles per byte at the two security levels, attaining sub-1 cycle/byte performance at both levels.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3000) | 2026-11-23
