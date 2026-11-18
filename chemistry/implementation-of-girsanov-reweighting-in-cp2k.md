---
title: "Implementation of Girsanov Reweighting in CP2K"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2601.05419"
summary: "arXiv:2601.05419v2 Announce Type: replace Abstract: Dynamical reweighting of path measures is a powerful approach for accurately evaluating slow molecular processes using modified potential energy sur"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2601.05419v2 Announce Type: replace Abstract: Dynamical reweighting of path measures is a powerful approach for accurately evaluating slow molecular processes using modified potential energy surfaces used in enhanced sampling methods. Integrating this reweighting framework into the CP2K electronic-structure and molecular-dynamics (MD) software package delivers a robust and widely applicable tool for metadynamics, uncertainty quantification, and force-field optimisation based on both extit{ab initio} and classical MD simulations. Based on the Girsanov theorem for stochastic dynamical systems, the method is adapted to the Bussi-Donadio-Parrinello velocity-rescaling scheme. This scheme is accessible through the CSVR thermostat and can be interpreted as a Langevin OVRVO/OBABO update scheme requiring two random numbers per integration step. Comprehensive implementation details are provided, including a complete overview of the modified CP2K modules involved in the MD cycle and the computation of reweighting factors. The framework supports multiple sources of bias potentials, enabling reweighting via the PLUMED interface or CP2K-native external potentials and restraints. The feasibility of the implementation is demonstrated through rerun benchmarks, dynamical reweighting of Markov state models (MSMs) and computation of transport properties based on CP2K trajectories, showing excellent agreement with reference simulations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2601.05419) | 2026-11-18
