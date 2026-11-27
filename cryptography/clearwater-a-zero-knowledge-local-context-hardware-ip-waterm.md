---
title: "ClearWater: A Zero-Knowledge Local-Context Hardware IP Watermarking Framework"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3035"
summary: "ClearWater embeds hardware IP watermarks during standard-cell placement in LLM-assisted flows and verifies detection without revealing the owner's key. Bounded fan-in contexts identify carrier pairs, "
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

ClearWater embeds hardware IP watermarks during standard-cell placement in LLM-assisted flows and verifies detection without revealing the owner's key. Bounded fan-in contexts identify carrier pairs, and keyed Poseidon2 determines their relative placement order. A Groth16 proof verifies agreement over an externally audited carrier table. In our testbench, routed AES, SHA-256, and ChaCha layouts retained every registered mark with no measured cell-area growth. Copied fragments retained matching bits even when too few survived to support a detection claim. For AES, verification took 16 milliseconds. The public carrier table dominated communication, while timing impact varied across designs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3035) | 2026-11-25
