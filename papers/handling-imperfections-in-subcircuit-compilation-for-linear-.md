---
title: "Handling Imperfections in Subcircuit Compilation for Linear Optical Quantum Computing"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.13379"
summary: "arXiv:2609.13379v1 Announce Type: new Abstract: Linear Optical Quantum Computing (LOQC) is emerging as a promising technology in large-scale quantum computing. Corresponding devices, including linear "
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.13379v1 Announce Type: new Abstract: Linear Optical Quantum Computing (LOQC) is emerging as a promising technology in large-scale quantum computing. Corresponding devices, including linear optical circuits, are rapidly growing in size and fabrication precision. However, even with improved quality, the circuits still exhibit imperfections leading to photon loss or phase noise that vary across the circuit. Already small deficiencies can have a vast impact on both accuracy and efficiency. For computations that do not require the entire linear optical circuit, so-called subcircuits, one can choose where to perform the computation, opening optimization opportunities that are addressed by subcircuit compilation. Current compilers spread the subcircuit's computation across the entire circuit, connecting the same input and output ports, thereby failing to fully exploit the optimization opportunities. However, given the subcircuit's reduced size compared to the entire circuit, one can keep its implementation localized and intentionally route photons to connect good input and output ports. This, however, is a highly non-trivial task, as numerous options must be weighed against one another, and the quality of the solution is influenced by a wide range of hardware parameters. In particular, the reflectivities of imperfect beam splitters can lead to photon losses during routing, which must be traded off against losses at the input and output ports due to imperfect transmission rates. Since current compilers do not account for these effects, we propose the first efficient subcircuit compilation method that optimizes for the coincidence rate, the probability of successfully measuring all desired photons, by handling hardware imperfections. Our evaluations demonstrate significant improvement over existing methods in robustness against phase noise and significantly increased coincidence rates across all benchmarks of up to plus 33.2%.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.13379) | 2026-09-15
