---
title: "Optimal transducers using symmetries"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02133"
summary: "arXiv:2610.02133v1 Announce Type: new Abstract: Transducers (Belovs, Jeffery and Yolcu, 2024) are a quantum computing framework describing a quantum algorithm as a unitary converting an input state in"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.02133v1 Announce Type: new Abstract: Transducers (Belovs, Jeffery and Yolcu, 2024) are a quantum computing framework describing a quantum algorithm as a unitary converting an input state into a target state using a catalyst, an auxiliary vector that is left unchanged. They are a powerful tool in quantum algorithm design, especially in the context of quantum query complexity: feasible points of the (dual) adversary semidefinite program directly translate into transducers and the optimal transduction complexity is equal to the adversary bound, i.e. the Las Vegas complexity, which is known to characterize bounded-error quantum query complexity. Moreover, contrary to bounded-error algorithms, transducers compose exactly, which limits overheads due to controlling errors in algorithms constructed by composition. Constructing efficient, let alone optimal, transducers in terms of quantum query complexity nevertheless remains a hard task since it still requires solving the adversary SDP and constructing the unitary to obtain an explicit algorithm. In this paper, we show how using the symmetry group of state-conversion problems simplifies both steps. First, using a symmetrization argument, we prove an optimal catalyst can always be chosen covariant under a representation of the symmetry group. Second, we prove that the transducer intertwines two different representations of the group and can thus be chosen block diagonal in the isotypic decomposition of the Hilbert space. Using those methods, we then derive optimal transducers, with optimal constants, for different widely used quantum algorithmic primitives, such as unstructured search, amplitude amplification and amplitude estimation. Our approach extends previous work on the use of representation theory to compute adversary lower bounds (H{o}yer, Lee, and {v S}palek, 2007; Ambainis, Magnin, Roetteler and Roland, 2011) to the systematic construction of optimal algorithms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02133) | 2026-10-02
