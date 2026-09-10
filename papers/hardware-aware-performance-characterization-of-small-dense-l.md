---
title: "Hardware-Aware Performance Characterization of Small Dense Lindblad Propagation for Near-Term Quantum Control"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.18052"
summary: "arXiv:2603.18052v2 Announce Type: replace Abstract: Dense Lindblad propagation at the Hilbert-space sizes of near-term transmon control (d = 3, 9, 27) sits in a regime where cache boundaries, launch o"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2603.18052v2 Announce Type: replace Abstract: Dense Lindblad propagation at the Hilbert-space sizes of near-term transmon control (d = 3, 9, 27) sits in a regime where cache boundaries, launch overhead, and fixed latency decide which hardware is useful, not peak arithmetic rate. This paper characterizes that regime on two x86 CPUs, two NVIDIA GPUs, and a low-cost FPGA. Each implementation is stated as an algorithm in d with an idealized cost built from separately measured ceilings, and the measured gaps are attributed to specific mechanisms: thread fork/join, the strided read of the propagator, PCI Express (PCIe) transfers, and propagator re-upload. An end-to-end gradient-ascent (GRAPE-style) benchmark against released QuTiP 5.2.3 shows that fast propagation does not imply fast control optimization: the C path wins by up to two orders of magnitude at d = 3 but loses at d = 27, where the dense LU solve inside the Pade propagator build takes over 90% of the cost. The FPGA contributes a deterministic-latency operating point, 95 cycles per step at a stress-characterized 108 MHz with zero cycle spread over 1000 trials, and its Q1.15 fixed-point drift is measured on the device. The results are a map of operating regimes for the measured grid, with the propagator build, not propagation, as the dominant cost at the largest size.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.18052) | 2026-09-10
