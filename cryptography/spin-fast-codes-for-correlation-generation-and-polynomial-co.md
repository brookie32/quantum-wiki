---
title: "SPIN: Fast Codes for Correlation Generation and Polynomial Commitments"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2317"
summary: "Binary codes used in correlation generation and proof systems need strong distance, fast ordinary and transposed encoding, and regular memory access. We introduce Single-Permutation INterleaved (SPIN)"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Binary codes used in correlation generation and proof systems need strong distance, fast ordinary and transposed encoding, and regular memory access. We introduce Single-Permutation INterleaved (SPIN) codes, combining a blockwise outer encoder, one global interleaver, and a recursive inner. Our main result is a Structured SPIN family with rate 1/2 and O(N) bit operations for ordinary and transposed encoding at its native output lengths N. With probability 1-o(1) over the random choice of the code, its minimum distance exceeds 0.11N. The proof combines outer spectrum bounds with an analysis of structured support spreading and recursive state mixing. We formally verify these distance and rate guarantees in Lean. For finite lengths, a BCH-derived outer constituent and a fixed recursive inner give rate 1/2 and relative distance greater than 0.10, with setup-failure probability below 2^{-40}. We certify this bound at message lengths 2^{16}, 2^{18}, 2^{20}, 2^{22}, and 2^{24} using rigorous spectrum inequalities, without assuming the constituent's exact weight spectrum. For pseudorandom correlation generators (PCGs), SPIN's transposed encoder computes 2^{20} 128-bit correlation blocks in about 9.3,ms on one Ryzen 9 7950X thread after precomputation. This is approximately 3.4imes faster than the original rate-1/2 BAA codes of Kolesnikov et al. (CRYPTO 2026). Ordinary encoding has similar cost. With a precomputed code, libOTe's regular-noise Silent OT sender achieves 89.0 million hashed OTs per second on one core, in batches of 2^{18}. Timings exclude initial setup, base-correlation generation, and network transport. We also use SPIN in a Brakedown-style polynomial commitment scheme and integrate it into Flock. Commitment and one opening of 512,MiB take 509,ms on one core, with a 100-bit interactive fixed-matrix testing target; this excludes code-setup failure, extraction, and Fiat-shamir reductions. Within an optimized Flock implementation, replacing Ligerito with SPIN--Brakedown improves prover throughput by 1.63--2.29imes at the measured workloads, with larger proofs and slower verification. The comparison gives both backends the applicable shared implementation optimizations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2317) | 2026-10-02
