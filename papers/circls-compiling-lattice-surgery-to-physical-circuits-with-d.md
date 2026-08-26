---
title: "CircLS: Compiling Lattice Surgery to Physical Circuits with Dynamic Allocation"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.23819"
summary: "arXiv:2608.23819v1 Announce Type: new Abstract: In fault-tolerant quantum computing, lattice surgery (LS) is one of the leading ways to realize logical operations, and the Pauli product measurement (P"
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2608.23819v1 Announce Type: new Abstract: In fault-tolerant quantum computing, lattice surgery (LS) is one of the leading ways to realize logical operations, and the Pauli product measurement (PPM) is the basic instruction of LS-based computing. Compilers on the PPM sequence, however, stay at the logical level rather than the physical circuit level. This is because the lowering is complicated: PPMs differ widely from each other, and each must be realized on the physical circuit without breaking fault tolerance. CircLS lowers the PPM sequence to a Stim circuit through linear-time stabilizer construction rules. This completes the pipeline from a quantum program through the PPM sequence to a Stim circuit, on which the compiled program can be verified at the circuit level and its logical error rate (LER) measured. Based on the lowering, we develop a compiler that allocates data patches dynamically: each patch is allocated at its first use and freed at its last use, and the freed tiles are reused as ancilla paths. CircLS reduces the allocated spacetime volume by 5.5imes and the LER by 14imes against the prior toolchain producing runnable circuits. CircLS is open source at https://github.com/John-YuehanZhang/CircLS.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.23819) | 2026-08-26
