---
title: "A Latency-Aware FPGA Architecture for SHAKE256 with Guarded Final-Block Construction: Targeting Post-Quantum XMSS Signatures"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2139"
summary: "The NIST SP 800-208 eXtended Merkle Signature Scheme (XMSS) profile XMSS-SHAKE256_10_256 repeatedly invokes SHAKE256 primitives, making field-programmable gate array (FPGA) accelerator latency sensiti"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

The NIST SP 800-208 eXtended Merkle Signature Scheme (XMSS) profile XMSS-SHAKE256_10_256 repeatedly invokes SHAKE256 primitives, making field-programmable gate array (FPGA) accelerator latency sensitive to Keccak permutation time and absorb/finalization-control overhead. Established round unrolling reduces permutation-side latency but leaves residual controller work. We propose SAFE Final-Block Construction (SAFE FBC), combining guarded SHAKE256-rate-aware eligibility, direct eligible final-block construction, and sequential-finalization bypass without modifying Keccak. A controlled 12-configuration study crosses four controller/finalization organizations with one-, two-, and three-round-per-cycle datapaths over nine XMSS-oriented cases: 96-byte F and pseudorandom-function (PRF) inputs, 128-byte H and PRFkeygen inputs, and selected message-hash cases around the SHAKE256 rate boundary. At every fixed depth, SAFE FBC reduces aggregate L2-final latency by 13 cycles versus the Structural Controller Decoupling (SCD) baseline; L2-final spans the first accepted AXI input beat to the final accepted AXI output beat. At three rounds per cycle, aggregate latency falls from 305 to 292 cycles, with no case regressing. F and ordinary PRF show the largest per-call gain, from 30 to 25 cycles (16.67%). Component measurements localize the saving to absorb/finalization control; Keccak permutation latency, squeeze latency, and input-transfer span remain unchanged. SAFE FBC complements unrolling, trading latency for substantial lookup-table/slice growth with very small flip-flop overhead.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2139) | 2026-09-21
