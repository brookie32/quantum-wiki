---
title: "Fault-tolerant quantum processor with minimal external control"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.23919"
summary: "arXiv:2611.23919v1 Announce Type: new Abstract: Contemporary classical information processors integrate tens of billions of transistors printed on a chip, yet are fully controlled through comparativel"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23919v1 Announce Type: new Abstract: Contemporary classical information processors integrate tens of billions of transistors printed on a chip, yet are fully controlled through comparatively few external wires. This is possible because data flows through hard-coded operations in step with a global clock and is steered by external instructions. Today's solid-state quantum processors are different -- every qubit receives instructions from outside the chip via its own dedicated control line, and error correction adds a further torrent of syndrome data that is transported off-chip. Here we show that the external control of a quantum chip can be greatly simplified. We propose a fault-tolerant architecture for universal quantum computation, inspired by modern classical processors, in which quantum information flows through a fixed, clocked device, propelled by local gates in a planar array. Our quantum processor receives an input stream of classical instructions via a small, constant number of external wires, each attached to a single qubit. Except for those few qubits coupled to external wires, all qubits evolve under a periodically-applied geometrically-local depth-3 circuit, which is fixed at the time the device is fabricated. Assuming a noiseless global clock (so that every operation is applied on schedule, though imperfectly), we establish an accuracy threshold theorem: For physical noise below a universal threshold -- afflicting every gate, measurement, and wire -- a chip with n physical qubits can run any quantum algorithm that uses~n/{sf polylog}(n/epsilon) logical qubits, where epsilon is the error rate per logical gate. Each logical gate takes time~n/{sf polylog}(n/epsilon); an alternative design, in which quantum operations remain strictly local and noisy, but on-chip wires broadcast noiseless classical signals instantaneously, reduces the time per logical gate to {sf polylog}(n/epsilon).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.23919) | 2026-11-19
