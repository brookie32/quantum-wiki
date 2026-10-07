---
title: "Learning consistent molecular mechanics force fields from first principles"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.08020"
summary: "arXiv:2610.08020v1 Announce Type: new Abstract: Classical force fields (FFs) remain the workhorse for large-scale simulations even as machine-learned interatomic potentials (MLIPs) approach ab initio "
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.08020v1 Announce Type: new Abstract: Classical force fields (FFs) remain the workhorse for large-scale simulations even as machine-learned interatomic potentials (MLIPs) approach ab initio accuracy. They decompose total configuration energies into simple effective interactions whose parameters are traditionally assigned based on atom or bond types, enabling efficient simulations but also limiting their ability to adapt across configurations. Recent machine learning approaches have improved the accuracy and transferability of bonded parameters in these FFs by inferring them as functions of local atomic environments, but still rely on empirical nonbonded parameters for practical simulations. In this work, we introduce a unified approach, exttt{grappa-fullFF}, which learns both bonded and nonbonded parameters consistently and simultaneously from ab initio reference data. By incorporating physically inspired regularization via supervision of the electrostatic potential and an architecture that facilitates charge equilibration, our model recovers accurate electric response properties, achieves state-of-the-art accuracy on geometry optimization benchmarks, and reproduces the conformational sampling of both classical and existing machine-learned FFs, without relying on externally assigned nonbonded parameters.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.08020) | 2026-10-07
