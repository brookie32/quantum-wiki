---
title: "Variational Programs with Open Clocks"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.40988"
summary: "arXiv:2610.40988v1 Announce Type: new Abstract: Variational quantum algorithms leave the durations of Hamiltonian evolutions open for a classical optimizer to set. We present VHamilton, a minimal exte"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.40988v1 Announce Type: new Abstract: Variational quantum algorithms leave the durations of Hamiltonian evolutions open for a classical optimizer to set. We present VHamilton, a minimal extension of the Hamilton quantum programming language in which such durations are open clocks: one program denotes a family of Hamiltonian trajectories, and a valuation fills its clocks with exact dyadic times, so that each instance is an ordinary Hamilton program that compiles to circuits as before. Because the semantics stays exact and affine in the clocks, the Hamiltonian structure of a variational program remainsavail able for reasoning about every valuation at once. Equivalence becomes a finite calculation, which we mechanize in Agda for a fragment and use to prove the VHamilton form of the compiler rewrite "rzz(t) = cx; rz(t); cx" for every clock value. We then show what the same structure supports in a two-qubit chemistry eigensolver written in VHamilton and run through a Haskell prototype. It supports a fusion of commuting blocks, a closed form and an expressibility proof for the ansatz, and an exact split of the error between the precision of the target and that of the clocks, with a priori bounds. It also supports a coordinate search whose queries per sweep, fixed by the spectra of the generators, do not grow with the precision. On the benchmark this search reaches the numerically verified optimum of a grid of 134 million valuations in 53 energy queries. It finds the grid optimum in only 21 of 30 validation settings, however, so the gain is conditional, not a global-optimization guarantee.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.40988) | 2026-11-02
