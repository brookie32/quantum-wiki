---
title: "Low-frustration block encodings by patch routing"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.32946"
summary: "arXiv:2610.32946v1 Announce Type: new Abstract: Block-encoding has emerged as a core primitive in many quantum algorithms, including quantum simulation. In this work, we design efficient and extensibl"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2610.32946v1 Announce Type: new Abstract: Block-encoding has emerged as a core primitive in many quantum algorithms, including quantum simulation. In this work, we design efficient and extensible methods for generating low-frustration block encodings of frustrated lattice Hamiltonians built from repeated local interaction patches through a technique we call "patch routing". We construct block encodings for a full Hamiltonian by first block-encoding a small local patch and then using a SWAP-style routing network to coherently apply the local patch encoding across the lattice. The expensive, local block-encoding cost is paid only once per query and is independent of lattice size, whereas the comparatively inexpensive routing network grows linearly with the lattice size, dominating at large sizes. Our method allows for a hierarchical structure in which larger patches can be block-encoded with small normalization factors, albeit at a higher (local, non-extensive) block-encoding cost, thereby reducing overall query complexity in an algorithm. We exploit symmetries and algebraic structures in local interactions to construct efficient block encodings, and we apply these techniques to the Heisenberg, Fermi-Hubbard, and honeycomb spin-liquid models. For a 120imes 120 square-lattice J_1-J_2 Heisenberg model near maximal frustration (J_2/J_1=0.4-0.6), our methods result in a 15-17imes reduction in the leading T cost per qubitized-QPE run (ignoring initial state preparation and overlap) relative to prior state-of-the-art Pauli LCU constructions. Corresponding reductions are approximately 3imes for the 120imes120 Fermi-Hubbard model at half-filling. For time evolution of the honeycomb spin-liquid model on 120imes120 unit cells, the leading cost is reduced by 5imes. Our framework provides a systematic way forward for larger and more accurate fault-tolerant simulations of real-world quantum systems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.32946) | 2026-10-26
