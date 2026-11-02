---
title: "A Hybrid Message-Passing and Electric-Field Representation for Electrostatic QM/MM Embedding with Machine Learning Interatomic Potentials"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41523"
summary: "arXiv:2610.41523v1 Announce Type: cross Abstract: Within a hybrid quantum mechanics/molecular mechanics approach a small region of a large atomistic system is described quantum mechanically, while the"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41523v1 Announce Type: cross Abstract: Within a hybrid quantum mechanics/molecular mechanics approach a small region of a large atomistic system is described quantum mechanically, while the rest of the system is represented by a classical force field. Despite this, the computational cost of the quantum calculation severely limits the accessible simulation and sampling time. Replacing the quantum calculation with a machine learning interatomic potential (MLIP) trained on quantum reference data can greatly increase the accessible simulation time. However, the accuracy and efficiency strongly depend on the specific way in which the MLIP incorporates information about the classical (electrostatic) environment. Here, we demonstrate that existing strategies based purely on features derived from an external electric field fail to distinguish certain environments, ultimately limiting their accuracy. As a solution, we propose an extension to the equivariant TensorNet architecture that mitigates this shortcoming by incorporating classical atoms close to the quantum region into the message-passing scheme, combined with features derived from the electric field for describing the environment farther away. We show that this combination achieves higher accuracy than either approach alone.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41523) | 2026-11-02
