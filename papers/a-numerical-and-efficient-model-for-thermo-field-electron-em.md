---
title: "A numerical and efficient model for thermo-field electron emission calculations"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.07013"
summary: "arXiv:2610.07013v1 Announce Type: cross Abstract: As electron sources are reduced in size, fabricated in new materials, or pushed for performance, the analytical formulations for thermo-field electron"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.07013v1 Announce Type: cross Abstract: As electron sources are reduced in size, fabricated in new materials, or pushed for performance, the analytical formulations for thermo-field electron emission, namely Fowler-Nordheim and Murphy-Good equations and their JWKB-based extensions, are increasingly applied out of the range of conditions for which they were derived. We present GETELEC-3, an open-source code that replaces them with a direct numerical solution of the one-dimensional time-independent Schrodinger equation (1D-TISE). Several methods to solve the 1D-TISE have been implemented to test for speed, robustness, and solution's uncertainty. The Noumerov algorithm is found to be quickest, with the solution uncertainty below 1%, and together with an optimised kernel that advances all electron energies in parallel, the cost of calculating the current density is reduced to a few milliseconds - comparable to the JWKB evaluation. To further boost the calculation speed, especially in complicated barriers, a neural network has been trained on the residual of the logarithm of the semiclassical reference and it reproduces the current density better than 0.4% at a fraction of the computational cost. The code is developed for metals and semiconductors, accepts arbitrary potentials and density of states, and comes with a user-friendly interface and compiled executable to democratise rigorous electron emission calculations and data analysis.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.07013) | 2026-10-07
