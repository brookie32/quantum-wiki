---
title: "MASQ: Measurement-Adaptive Sampling for Near-Clifford Quantum Error Correction Circuits"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.22232"
summary: "arXiv:2611.22232v1 Announce Type: cross Abstract: Classical sampling of quantum error correction (QEC) circuits supports fault-tolerant protocol evaluation, but estimating rare logical failures requir"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.22232v1 Announce Type: cross Abstract: Classical sampling of quantum error correction (QEC) circuits supports fault-tolerant protocol evaluation, but estimating rare logical failures requires many independent shots. Frame-active-state simulators isolate non-stabilizer information in a dense active-state vector, yet dense-state processing remains exponential in the active width. This paper presents MASQ, an exact measurement-adaptive sampler for near-Clifford QEC circuits based on selective materialization of non-Clifford rotations. At each measurement boundary, MASQ materializes only rotations in a measurement-relevant closure capturing direct and indirect non-commuting dependencies, deferring the rest to limit active-state expansion. Stabilizer-assisted elimination further removes rotations certified to be invisible to all future measurements. A circuit-dependent schedule is computed once and shared across shots, while adaptive caching of conditional Born probabilities and batched execution reduce repeated sampling work while preserving the measurement-record distribution. Across 19 QEC benchmarks, MASQ reduces peak active width by up to 40 active virtual qubits and achieves up to 8,098-fold CPU throughput speedup over Clifft on multi-round circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.22232) | 2026-11-18
