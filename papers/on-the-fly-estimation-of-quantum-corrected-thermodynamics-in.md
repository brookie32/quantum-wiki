---
title: "On-the-fly Estimation of Quantum-Corrected Thermodynamics in LAMMPS"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.37586"
summary: "arXiv:2610.37586v1 Announce Type: cross Abstract: We present a native implementation of the Two/Three-Phase Thermodynamics (xPT, x in {2,3}) method within the LAMMPS molecular dynamics framework, term"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.37586v1 Announce Type: cross Abstract: We present a native implementation of the Two/Three-Phase Thermodynamics (xPT, x in {2,3}) method within the LAMMPS molecular dynamics framework, termed FixXPT. xPT is an approach for obtaining absolute, quantum-corrected thermodynamics (entropy, enthalpy, free energy, heat capacity, diffusivity) from the density of states function, obtained from the velocity autocorrelation function of an equilibrium trajectory. FixXPT addresses non-trivial integration challenges, including atom reordering, compute scheduling, FFT backends, unit systems, and partitioning of atomic velocities into molecular modes. Two autocorrelators are provided: a Wiener-Khinchin FFT correlator with one cumulative window-end operation, and an in-line multi-tau correlator whose memory footprint grows only logarithmically with the window length, removing the principal scaling bottleneck for long analysis windows. The velocity history of each window is distributed across the MPI ranks, so the memory the fix adds to a node stays nearly constant as ranks are added and its cost falls with the number of GPUs. Replaying identical velocity frames through FixXPT and the stand-alone pyxPT post-processor reproduces every thermodynamic observable of well-sampled groups to within 0.1 to 0.5% across the full analysis-mode matrix; sparsely populated ionic species agree within their statistical uncertainty, and the multi-tau VACF converges monotonically to the FFT result as its buffer grows, from 0.8% to 0.1% drift across a 16-fold buffer sweep. The code is distributed as a drop-in LAMMPS package.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.37586) | 2026-10-28
