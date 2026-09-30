---
title: "Exact SVP on Haar-Random Lattices at the Heuristic Sieving Exponents"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2271"
summary: "We give a Monte Carlo algorithm for exact Euclidean SVP on Haar-random lattices with arithmetic time (3/2)^{n/2+o(n)} and space (4/3)^{n/2+o(n)}, up to polynomial factors in the logarithmic condition "
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

We give a Monte Carlo algorithm for exact Euclidean SVP on Haar-random lattices with arithmetic time (3/2)^{n/2+o(n)} and space (4/3)^{n/2+o(n)}, up to polynomial factors in the logarithmic condition number of the input basis. The leading exponents match those of heuristic lattice sieving. For a set of lattices of Haar measure 1-o(1), the algorithm succeeds with probability 1-o(1) on every input basis. Our algorithm regenerates each sieve list by running a Markov chain on the nonzero lattice points in a smaller ball. The parent list supplies signed increments. Each step reports all admissible proposals and assigns each the same probability, with the remaining probability assigned to staying put. The resulting chain is symmetric and has uniform stationary distribution. Trajectories using independent transition randomness produce endpoints jointly close to independent uniform samples once the chain mixes. Matrix Chernoff bounds transfer a Laplacian gap from the full angular graph to the graph defined by the parent list. The main proof task is to establish the required graph estimates on Haar-random lattices. We do so by adapting Rogers's moment method to centered trace moments and lattice-point counts. Spherical filtering reports the complete proposal sets and the final short differences within the claimed bounds.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2271) | 2026-09-30
