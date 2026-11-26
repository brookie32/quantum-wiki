---
title: "TyxonQ: A Workflow Layer for Quantum Computing in Chemistry"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.33883"
summary: "arXiv:2611.33883v1 Announce Type: cross Abstract: Quantum computational chemistry is often framed around a hybrid quantum solver. In practical applications, however, bottlenecks to adoption also lie i"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33883v1 Announce Type: cross Abstract: Quantum computational chemistry is often framed around a hybrid quantum solver. In practical applications, however, bottlenecks to adoption also lie in the surrounding multiscale workflow. A molecular problem may combine classical molecular mechanics and dynamics, conventional electronic-structure calculations, and a quantum solver for selected orbitals or embedded fragments. This division of work is particularly relevant when a chemically important electronic subspace is strongly correlated. The size of the electronic Hilbert space and the qubit, noise, and circuit-depth constraints of noisy intermediate-scale quantum (NISQ) devices make active-space and embedding choices central to a feasible quantum calculation. The resulting energies and gradients must remain consistent with the surrounding classical simulation. We present TyxonQ, a workflow layer that connects these levels of treatment rather than addressing only the hybrid quantum algorithm. Four integration interfaces link PySCF-compatible energy/force scanners and embedding, solver adapters, simulator and hardware backends, and classical consumers. The implementation combines QM/MM and fragment embedding with conventional CCSD/FCI fragment solvers, variational and sampling-based quantum methods, and adapters for ASE, i-PI, OpenMM, LAMMPS (through i-PI), and MDI. We describe the contracts and audit coverage, and evaluate correctness, switching cost, reproducibility, and artifact portability on small chemistry workflows, distinguishing executed paths from source-level support. The purpose of TyxonQ is to support incremental integration of quantum calculations into existing computational chemistry workflows, including those used in industry, while retaining appropriate classical treatments elsewhere.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.33883) | 2026-11-26
