---
title: "Simulating Ionic Liquid Fragmentation in Electrospray Thrusters with Foundation Models"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.11558"
summary: "arXiv:2608.11558v1 Announce Type: new Abstract: Predicting the products of ionic-liquid impacts on extractor surfaces is important for electrospray-thruster lifetime analysis, yet available atomistic "
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.11558v1 Announce Type: new Abstract: Predicting the products of ionic-liquid impacts on extractor surfaces is important for electrospray-thruster lifetime analysis, yet available atomistic methods require a compromise between chemical fidelity and computational cost. Reactive force fields enable high-throughput sampling but do not explicitly resolve electronic charge redistribution and may miss relevant reaction pathways during impact, whereas mixed quantum--classical density-functional-theory molecular dynamics (DFT/MD) can capture charge redistribution and neutral-product formation at substantially higher computational cost. Pretrained atomistic foundation models have recently emerged as a potential route toward DFT-like chemical fidelity at considerably lower cost. Here, we benchmark two pretrained machine-learning interatomic potentials, MACE-MP-0 (medium) and MACE-POLAR-1, against DFT/MD and ReaxFF for geometry optimization of 1-ethyl-3-methylimidazolium tetrafluoroborate (EMI-BF_4) and for 10-100 eV impacts on a model Au extractor surface. The models reproduce several collision outcomes observed in DFT/MD, including ionic dissociation, high-energy covalent fragmentation, and, in particular, HF formation through neutralization-like chemistry that is not captured in the ReaxFF simulations. In the computational-performance benchmark, MACE-POLAR-1 and MACE-MP-0 (medium) completed each 2~ps trajectory in 5.12 and 2.54~min, respectively, corresponding to wall times approximately four orders of magnitude shorter than the DFT/MD reference under the reported benchmark conditions. These results support pretrained machine-learning potentials as a practical intermediate-cost approach for chemically resolved electrospray-impact simulations and motivate targeted fine-tuning with DFT data for broader applications in electrospray-thruster and electric-propulsion modeling.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.11558) | 2026-08-13
