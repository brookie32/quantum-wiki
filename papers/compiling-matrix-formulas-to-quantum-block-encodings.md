---
title: "Compiling Matrix Formulas to Quantum Block Encodings"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.17756"
summary: "arXiv:2611.17756v1 Announce Type: cross Abstract: Realizing the promise of quantum applications such as chemistry or fluid dynamics requires building quantum circuits that efficiently encode and manip"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.17756v1 Announce Type: cross Abstract: Realizing the promise of quantum applications such as chemistry or fluid dynamics requires building quantum circuits that efficiently encode and manipulate exponentially large matrices. This process forces researchers to grapple with the reality that a matrix expressible as one equation on paper can map to thousands of bit-level quantum logic gates, historically written by hand. Even worse, it often ends with a discovery that the needed resources grow so quickly with matrix size that the quantum algorithm loses its asymptotic speedup. In this work, we present MARBLE, a language that automatically synthesizes an efficient circuit from the publication-style formula for the entries of a matrix. MARBLE algebraically rewrites programs into symbolic combinations of simpler matrices that have known circuit realizations. It analyzes costs of possible representations, notably the subnormalization term that dominates time complexity. It then emits an OpenQASM circuit and certifies whether its cost is poly-logarithmic in problem size, as required by quantum algorithms. When evaluated on quantum applications ranging from fluid dynamics to physical Hamiltonians, MARBLE matches or surpasses 37 of 39 published baselines. On the low end, it automatically matches many theoretically optimal circuits, and on the high end, it improves on a published construction in fluid dynamics by 10,487x in subnormalization. MARBLE produces exponentially smaller circuits than the leading tool FABLE, and it successfully compiles matrices whose dimensions exceed 2^100 within five seconds on a laptop.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.17756) | 2026-11-16
