---
title: "When Do Tensor Product Paths Matter? A Group-Theoretic Analysis of Equivariant Interatomic Potentials"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.21683"
summary: "arXiv:2611.21683v1 Announce Type: new Abstract: Tensor-product (TP) layers in equivariant interatomic potentials encode angular interactions through symmetry-allowed paths. Yet local site symmetry can"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.21683v1 Announce Type: new Abstract: Tensor-product (TP) layers in equivariant interatomic potentials encode angular interactions through symmetry-allowed paths. Yet local site symmetry can make an allowed path carry no signal after neighbor aggregation. We call this effect Aggregation Cancellation. In a scalar-input first layer, equal-species neighbors on a complete site-symmetry orbit share scalar and radial factors, reducing their angular contribution to a spherical-harmonic orbit sum. If the restricted degree-l representation has no trivial component, this sum and the corresponding path vanish for any learned radial weight. For an ideal O_h octahedral orbit, this removes the l_edge=1,2,3 classes. Beyond the first layer, the factorisation no longer holds, so cancellation is no longer guaranteed; we instead ask whether affected paths remain less important on average. We test the two levels separately in NequIP: matched-radius TiO_6 probes examine first-layer cancellation, whereas a within-model CaTiO_3 comparison and six OMat24 models examine the importance bias. We then rank paths on training frames, choose the pruning fraction on validation frames, and evaluate frozen masks on held-out tests. At the highest evaluated fraction (60% of 174 paths), force mean absolute error (MAE) changes are 1.42%, 0.04%, and 1.83% for CaTiO_3, OMat24 O_h-cubic, and OMat24 low-symmetry data, respectively. The masks imply 67.12-71.94% potential TP-operation reduction and 59.77% potential edge multilayer perceptron (MLP) reduction; these are structural proxies, not measured speedups. The results connect local symmetry to path redundancy and pruning robustness in NequIP; transfer to other architectures remains open.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.21683) | 2026-11-18
