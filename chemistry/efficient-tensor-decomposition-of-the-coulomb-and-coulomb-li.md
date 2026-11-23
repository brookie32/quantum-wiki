---
title: "Efficient Tensor Decomposition of the Coulomb and Coulomb-like Potentials and Its Application to Probing Molecular Geometries Using a Quantum Computer"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.26740"
summary: "arXiv:2611.26740v1 Announce Type: new Abstract: We present an efficient canonical polyadic decomposition of the Coulomb and Coulomb-like potentials in real-space grid representations suited to quantum"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.26740v1 Announce Type: new Abstract: We present an efficient canonical polyadic decomposition of the Coulomb and Coulomb-like potentials in real-space grid representations suited to quantum computing applications. By decomposing the matrix elements of Coulomb-like potentials into low-rank Cartesian components, we achieve O(N^{1/3}) T-gate scaling per Coulomb term, where N is the number of grid points (basis functions) per electron, while maintaining high accuracy. This opens a path to significantly reducing the number of basis functions (i.e., qubits) required compared to previous methods by utilizing improved representations of the Coulomb potential that converge faster with grid spacing. The decomposition is also valid for certain pseudopotentials, which can decrease the cost significantly compared to previous work. This efficient decomposition enables the application of block-encoding techniques at larger grid spacings than with previous decompositions, and can therefore be used for algorithms that do not require high energy accuracy. We apply this decomposed Coulomb potential to hydrogen atom energy levels, the helium ground-state energy, and the Hartree-Fock potential energy curve of LiH, and show that modest basis sizes achieve semi-quantitative to quantitative accuracy. As an example of where these faster-converging Coulomb representations can be used on a quantum computer, we discuss their application to probing low-energy molecular geometries, and we estimate the resulting reduction in the cost of real-time evolution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.26740) | 2026-11-23
