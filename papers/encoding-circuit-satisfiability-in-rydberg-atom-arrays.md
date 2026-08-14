---
title: "Encoding Circuit Satisfiability in Rydberg Atom Arrays"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.12938"
summary: "arXiv:2608.12938v1 Announce Type: new Abstract: Rydberg atom arrays natively encode the maximum-weight independent set (MWIS) problem through the blockade mechanism, so the Boolean circuit satisfiabil"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.12938v1 Announce Type: new Abstract: Rydberg atom arrays natively encode the maximum-weight independent set (MWIS) problem through the blockade mechanism, so the Boolean circuit satisfiability problem (Circuit-SAT) can be brought onto the platform once it is reduced to MWIS. The conventional encoding of Circuit-SAT in the Rydberg atom array proceeds through conjunctive normal form (CNF) and incurs a substantial atom overhead. We introduce CAMERA (Circuit-SAT Atom-efficient MWIS Encoding for Rydberg Arrays), a method that provides MWIS encodings of Circuit-SAT instances on the king subgraph geometry of the array. CAMERA represents each logic gate as a compact weighted gadget and assembles the gadgets with a placement and routing compiler inspired by very large scale integration (VLSI) design. On random multi-gate benchmarks, the direct encoding route lowers the atom cost relative to the CNF route by an average factor of 22.4 pm 1.8. To demonstrate that the encoding extends from individual weighted gadgets to multi-gate arithmetic blocks, we compile a full adder and a multiplier, verifying each against its complete truth table by exact classical ground state calculations. We further showcase solving a representative Circuit-SAT instance end-to-end, from gate level compilation through a closed-system tensor-network simulation of a hardware-compatible annealing protocol on the encoded 30-atom instance to readout of a satisfying assignment. These results establish a complete encoding and simulation workflow as a proof of principle, and a concrete route toward solving a broader family of combinatorial problems on Rydberg atom arrays.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.12938) | 2026-08-14
