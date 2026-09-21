---
title: "fix uvt and fix pimd/uvt: A Unified LAMMPS Framework for Constant-Potential Constant-Temperature Molecular Dynamics"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.21935"
summary: "arXiv:2609.21935v1 Announce Type: new Abstract: Accurate simulations of electrochemical interfaces require the simultaneous treatment of constant-potential conditions, nuclear quantum effects, and suf"
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2609.21935v1 Announce Type: new Abstract: Accurate simulations of electrochemical interfaces require the simultaneous treatment of constant-potential conditions, nuclear quantum effects, and sufficient configurational sampling. Integrating these capabilities within a general and efficient molecular dynamics (MD) framework remains challenging. In this work, we implement fix uvt and fix pimd/uvt in LAMMPS for constant-potential classical MD and path integral molecular dynamics (PIMD), respectively. We organize the class hierarchy to reuse LAMMPS's existing Nose--Hoover chain thermostat routines and share nuclear propagation routines across PIMD integrators. A common interface connects these integrators to models that provide the electron-number derivative of the potential energy. We present three examples with accompanying input commands to guide users through constant-potential classical MD, thermostatted PIMD, and constant-potential PIMD, covering analytical models, liquid water, and electrochemical interfaces described by machine learning potentials. This work provides practical tools and guidance for large-scale constant-potential simulations incorporating nuclear quantum effects.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.21935) | 2026-09-21
