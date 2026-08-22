---
title: "QuaILLL: Quaternion Ideal LLL and BKZ"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1755"
summary: "The current state of the art for cryptanalysis generic rank-2 module LIP schemes invokes an SVP oracle on the canonical real embedding, discarding the quaternionic structure made available by the redu"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

The current state of the art for cryptanalysis generic rank-2 module LIP schemes invokes an SVP oracle on the canonical real embedding, discarding the quaternionic structure made available by the reduction of rank-2 module LIP to the reduced-norm Principal Ideal Problem (nrd-PIP) over quaternion algebras (we note, that since writing, this is no longer the case for certain instances, such as Hawk). We address this gap by giving, to our knowledge, the first lattice reduction algorithms over quaternion rings applied in a cryptographic setting, and the first description of quaternion BKZ. We extend the celebrated LLL algorithm to leverage algebraic properties of quaternion orders and novel post-processing steps to design an LLL algorithm for lattices in not-necessarily-maximal orders. The strategy is to reduce over the Euclidean overlattice and then post-process, giving two routines: one returning a basis of a sublattice with the best bounds, the other a true basis of the original lattice at the cost of output quality. We further consider blocksize two BKZ as a generalisation of the LLL algorithm, and then extend this to arbitrary blocksize; utilising results on the shortness of Gauss and HKZ reduced bases and the relationship of successive minima for our specific sublattice. We then apply these algorithms to ideal lattices arising from nrd-PIP, including those instances given by rank-2 MLIP over cyclotomic fields such as Hawk, via a modification of the canonical embedding that preserves both dimension and quaternionic structure. This allows us to reduce a lattice basis of rank a constant factor of four smaller than the standard real embedding, improving basis bounds and asymptotic complexity in the generic setting.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1755) | 2026-08-20
