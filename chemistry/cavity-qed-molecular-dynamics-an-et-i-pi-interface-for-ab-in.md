---
title: "Cavity-QED Molecular Dynamics: An eT-i-PI Interface for Ab Initio Cavity Born-Oppenheimer Dynamics and Joint Nuclear-Photon Path-Integral Sampling"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.09667"
summary: "arXiv:2611.09667v1 Announce Type: new Abstract: Simulating molecules in quantum electrodynamic (QED) cavities requires a consistent description of electronic response, nuclear motion, and electromagne"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2611.09667v1 Announce Type: new Abstract: Simulating molecules in quantum electrodynamic (QED) cavities requires a consistent description of electronic response, nuclear motion, and electromagnetic-field fluctuations. Here, I present Cavity-QED Molecular Dynamics, an interface connecting eT and i-PI for atomistic simulations of finite molecular systems coupled to a single photon mode. The code evaluates a self-consistent cavity Born-Oppenheimer Hartree-Fock (CBO-HF) energy surface and supports classical-nuclei dynamics under canonical (NVT) and microcanonical (NVE) ensembles, as well as canonical joint nuclear-photon path-integral sampling including nuclear quantum effects (NQEs). A fixed-displacement gradient correction provides nuclear and photon forces consistent with the same energy surface as the photon coordinate evolves independently. OpenMP threading, concurrent bead evaluations, and analysis utilities support practical simulations. Water-monomer benchmarks assess both dynamical propagation and equilibrium sampling. Energy-derivative checks and NVE timestep tests demonstrate consistent force evaluation and integration, while path integral molecular dynamics (PIMD) simulations with PILE-L thermostatting reproduce analytic finite-bead photon second moments, including their centroid and internal contributions, within sampling uncertainties. At the tested parameters, cavity coupling produces a small but statistically resolved increase in photon fluctuations, while changes in mean molecular geometry remain within sampling uncertainty. The resulting Cavity-QED Molecular Dynamics framework enables controlled investigations of how coupled quantum fluctuations of matter and the electromagnetic field influence molecular equilibrium properties within the CBO-HF approximation, providing a foundation for future studies of cavity-modified hydrogen bonding, vibrational spectra, and molecular polaritonic phenomena.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.09667) | 2026-11-09
