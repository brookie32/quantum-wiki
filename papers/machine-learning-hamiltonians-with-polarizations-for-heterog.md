---
title: "Machine Learning Hamiltonians with Polarizations for Heterogeneous Systems"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.36839"
summary: "arXiv:2610.36839v1 Announce Type: new Abstract: Machine learning Hamiltonians use local atomic structures to determine local Hamiltonian matrix elements without carrying out self-consistent calculatio"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.36839v1 Announce Type: new Abstract: Machine learning Hamiltonians use local atomic structures to determine local Hamiltonian matrix elements without carrying out self-consistent calculations. They have been used to study large systems and to carry out high-throughput screening for their electronic and optical properties. The prediction of the Hamiltonian is essentially the prediction of the electron electrostatic potential energy; however, for heterogeneous systems, this potential energy is often determined by faraway features, such as interface or surface dipoles, or even an applied voltage in a nanodevice. Thus, it cannot be determined by local atomic structures alone. In this sense, one needs to solve the electron electrostatic potential energy self-consistently using intrinsic atomic dipoles, the applied external potential energy, and polarizabilities. Fortunately, the intrinsic dipoles and polarizabilities are local properties, whereas the applied potential energy is a prescribed input. In this work, we propose DeepH-Polar, a physically informed machine learning Hamiltonian model that explicitly predicts intrinsic atomic dipoles and polarizability tensors and uses them to solve the electron electrostatic potential energy self-consistently. Benchmarks on polar GaN systems and crystalline-Si/amorphous-SiO_2 interfaces demonstrate improved Hamiltonian accuracy and reproduction of thickness-dependent electrostatic variations, as well as spatially nonuniform field-induced screening that models without polarization fail to capture. Our model also allows us to study nanoscale electronic devices. By iteratively solving the Hamiltonian eigenproblem and self-consistently updating free-carrier occupations and the electrostatic potential, we simulate an 8,194-atom gated semiconductor device.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.36839) | 2026-10-28
