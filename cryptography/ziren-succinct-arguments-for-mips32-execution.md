---
title: "Ziren: Succinct Arguments for MIPS32 Execution"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2330"
summary: "A succinct argument for machine execution convinces a verifier that a program compiled for a real instruction set ran correctly, with a proof far shorter than the execution and a check far cheaper tha"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

A succinct argument for machine execution convinces a verifier that a program compiled for a real instruction set ran correctly, with a proof far shorter than the execution and a check far cheaper than replaying it. We present Ziren, a production zkVM for MIPS32: it proves 77 user-mode integer instructions of MIPS32r2 and has proved Ethereum mainnet blocks end to end in production. Ziren is a CPU-less chip architecture: each executed instruction is one row of its opcode's chip. Each shard is proved by one lookup argument for all of its buses and one zerocheck for all of its constraints, and the claims on its tens of thousands of columns of differing heights are reduced by a jagged sumcheck to a single evaluation, opened by one batched WHIR proof. A recursion tree composes the shard proofs under an enumerated allowlist of verifying keys, and the determinism of 57 of the core machine's 62 chips (all but three preprocessed tables and two SHA-256 control chips) is extracted mechanically, as Lean 4 theorems, from the same constraint description the prover evaluates. On a configuration that precedes four later changes, proving throughput reaches up to 7.3 MHz on one NVIDIA RTX 5090 and scales horizontally across GPUs, reaching 24 MHz on four. Each proof stage of the analysed schedule has more than 100 bits of interactive soundness, and 93.5 bits of composite security over a block's tree of about 150 proofs. The end-to-end statement is conditional: it assumes round-by-round knowledge soundness of every node, compatibility of the composed extractors, that the recursion programs, which are not extracted, enforce the compose relation, and a property of the cross-shard digest to which we assign no value; identifying the trace with an execution also needs determinism of the two SHA-256 control chips and real-row exhaustiveness. All 104 extracted determinism theorems are proved in Lean 4: a propagation analysis derives every output column, and the derivation is replayed as step lemmas over gadget theorems proved once.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2330) | 2026-10-04
