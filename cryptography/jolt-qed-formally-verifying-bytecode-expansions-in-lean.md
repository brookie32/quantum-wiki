---
title: "Jolt-QED: Formally Verifying Bytecode Expansions In Lean"
date: "2026-09-22"
updated: "2026-09-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2157"
summary: "In this work, we formally verify using the Lean4 proof assistant, that jolt zk-VM's bytecode expansion process faithfully emulates a RISC-V CPU. Prior work translated the official Sail specification o"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

In this work, we formally verify using the Lean4 proof assistant, that jolt zk-VM's bytecode expansion process faithfully emulates a RISC-V CPU. Prior work translated the official Sail specification of RISC-V into Lean. We extend this model to define the Jolt ISA in Lean. We then write a transpiler to automatically extract Jolt’s bytecode expansions into Lean from their Rust definitions. Finally, we prove these expansions equivalent to their corresponding RISC-V instructions. Additionally, this lays the groundwork for proving the upstream components of Jolt are complete and sound.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2157) | 2026-09-22
