---
title: "Flip a Failure into a Success: Improved Bit Flipping Decoding for QC-MDPC Codes"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1616"
summary: "Quasi-Cyclic Moderate-Density Parity-Check (QC-MDPC) codes are a family of error correcting codes admitting parity-check matrices composed of sparse circulant blocks. QC-MDPC codes have been used for "
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Quasi-Cyclic Moderate-Density Parity-Check (QC-MDPC) codes are a family of error correcting codes admitting parity-check matrices composed of sparse circulant blocks. QC-MDPC codes have been used for the design of BIKE, one of the finalists in the NIST competition for the standardization of post-quantum cryptography. Decoding of QC-MDPC codes with cryptographically relevant parameters is intrinsically bound to fail, resulting in a decoding failure rate (DFR) that is nonzero. To achieve INDistinguishability under Adaptively Chosen Ciphertext Attacks (IND-CCA2), the DFR must not exceed 2^{-lambda}, with lambda being the security parameter. QC-MDPC codes are customarily decoded with a Bit Flipping (BF) algorithm. Especially at very low DFR values, error patterns having a large intersection with near-codewords (which are vectors corresponding to columns of the parity-check matrix, up to some shift) are the main cause of decoding failures. In this paper, we show how a BF decoder can be tweaked to exploit the knowledge about near-codewords. Since error vectors that cause decoding failures are likely making the decoder converge to the closest near-codeword (i.e., to the near-codeword with the largest amount of overlapping positions with the error vector), we exploit such a harmful but predictable behavior: we let the decoder recognize, and consequently correct, syndromes of near-codewords. This modification comes with a very mild computational overhead and can be applied to any BF decoder. As a concrete application, we focus on BIKE parameters for NIST security category 1. We show that a recently proposed BF variant called extsf{BF}ext{-}extsf{Max} outperforms significantly the two decoders used by BIKE within the NIST competition, achieving a significantly lower DFR with a comparable computational complexity.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1616) | 2026-08-05
