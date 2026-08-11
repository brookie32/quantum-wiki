---
title: "Design Space of Self--Consistent Electrostatic Machine Learning Interatomic Potentials"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2603.14700"
summary: "arXiv:2603.14700v2 Announce Type: replace Abstract: Machine learning interatomic potentials (MLIPs) have become widely used tools in atomistic simulations. For much of the history of this field, the m"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2603.14700v2 Announce Type: replace Abstract: Machine learning interatomic potentials (MLIPs) have become widely used tools in atomistic simulations. For much of the history of this field, the most commonly employed architectures were based on short-ranged atomic energy contributions, and the assumption of locality still persists in many modern foundation models. While this approach has enabled efficient and accurate modelling for many use cases, it poses intrinsic limitations for systems where long-range electrostatics, charge transfer, or induced polarization play a central role. A growing body of work has proposed extensions that incorporate electrostatic effects, ranging from locally predicted atomic charges to self-consistent models. While these models have demonstrated success for specific examples, their underlying assumptions, and fundamental limitations are not yet well understood. In this work, we present a framework for treating electrostatics in MLIPs by viewing existing models as coarse-grained approximations to density functional theory (DFT). This perspective makes explicit the approximations involved, clarifies the physical meaning of the learned quantities, and reveals connections and equivalences between several previously proposed models. Using this formalism, we identify key design choices that define a broader design space of self-consistent electrostatic MLIPs. We implement salient points in this space using the MACE architecture and a shared representation of the charge density, enabling controlled comparisons between different approaches. Finally, we evaluate these models on two instructive test cases: metal-water interfaces, which probe the contrasting electrostatic response of conducting and insulating systems, and charged vacancies in silicon dioxide. Our results highlight the limitations of existing approaches and demonstrate how more expressive self-consistent models are needed to resolve failures.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2603.14700) | 2026-08-11
