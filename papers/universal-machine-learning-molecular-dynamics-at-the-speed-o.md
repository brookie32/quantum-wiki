---
title: "Universal Machine-learning Molecular Dynamics at the Speed of Empirical Potentials"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.19041"
summary: "arXiv:2608.19041v1 Announce Type: new Abstract: No interatomic potential has offered universality across chemistry, near-first-principles accuracy and the speed of empirical potentials at once. Here w"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.19041v1 Announce Type: new Abstract: No interatomic potential has offered universality across chemistry, near-first-principles accuracy and the speed of empirical potentials at once. Here we introduce DPA4C, an equivariant potential whose architecture and compressed CUDA operators are co-designed under deployment constraints to pursue accuracy and efficiency together. Five variants spanning a 49-fold parameter range form the high-throughput end of the measured accuracy--throughput frontier. The largest variant approaches the accuracy of the MACE-Omat models at about two orders of magnitude higher measured throughput. The most compact reduces the energy, force and stress errors of the fastest existing universal MLIP by 61.4%, 48.1% and 34.3% at 1.92 times its saturated throughput. All five variants complete multimillion-atom simulations on a single GPU and run molecular dynamics for 2.048 billion atoms on 1,024 16-GB NVIDIA V100 GPUs at 83.3--91.2% weak-scaling efficiency. Compared with the MEAM empirical potential, DPA4C-Nano reaches 1.8 and 2.5 times the saturated throughput in single-GPU scans on the same V100 hardware for diamond carbon and FCC copper, respectively. DPA4C therefore brings quantum-trained universal accuracy into a regime of speed and system size previously associated with empirical potentials.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.19041) | 2026-08-20
