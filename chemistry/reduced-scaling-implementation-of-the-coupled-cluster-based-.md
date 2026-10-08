---
title: "Reduced scaling implementation of the coupled cluster-based static embedding method, MPCC with density fitting"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.32884"
summary: "arXiv:2609.32884v2 Announce Type: replace-cross Abstract: An improved algorithm to implement our previously proposed static quantum embedding method MPCC (J. Chem. Phys. 161, 164107 (2024)) is present"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2609.32884v2 Announce Type: replace-cross Abstract: An improved algorithm to implement our previously proposed static quantum embedding method MPCC (J. Chem. Phys. 161, 164107 (2024)) is presented. It uses the density-fitting (DF) approximation for the electron-repulsion integrals (ERIs) across all layers of the embedding method: the low-level method, the screened interaction, and the high-level method. Additionally, an approximate factorized solution of the Sylvester equation is employed based on the Laplace transformation for the low-level method. To build the screened interaction, we have explored an approximate construction of it based on the distinguishable cluster approximation (DCA) by Kats and Manby (J. Chem. Phys. 141, 061101 (2014)), which amounts to neglecting certain higher-order exchange and ladder diagrams. Combining all these techniques, we have obtained an O(N^4) algorithm for the low-level method; a non-iterative N_{rm frag} O(N^4) algorithm for the screened interaction; and an iterative O(N_{rm frag}^6) algorithm for the fragment solver, where N_{rm frag} is the number of fragment orbitals and N is the total number of orbitals. The resulting low-scaling implementation of the MPCC method is applied to trans polyacetylenes, that is, C_{2n}H_{2n+2} molecules for chain lengths n=1-8, and the timing and accuracy of the method are compared to the original unfactorized implementation. Moreover, the approximations are further validated by applying the method to the potential energy surface of the e{O3} molecule. Finally, we apply the method to the selected molecules in the S22 dataset for which the performance of the MP2 method is known to be poor. The results demonstrate that the DF-based implementation of the MPCC method provides a significant reduction in computational cost while maintaining accuracy comparable to that of the original implementation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.32884) | 2026-10-08
