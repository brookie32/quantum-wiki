---
title: "Sparse block encoding with low subnormalisation for quantum linear solvers on unstructured meshes"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.27915"
summary: "arXiv:2610.27915v1 Announce Type: new Abstract: Unstructured meshes are widely used in modelling and simulation in Computational Fluid Dynamics (CFD) due to their geometric flexibility. However, they "
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.27915v1 Announce Type: new Abstract: Unstructured meshes are widely used in modelling and simulation in Computational Fluid Dynamics (CFD) due to their geometric flexibility. However, they require an efficient block encoding circuit describing the system. Here, we present a new block encoding methodology for unstructured mesh solvers based on decomposing the system matrix into a sum of 1-sparse matrices. This block encoding is engineered to reduce subnormalisation even in the absence of structure by hiding the contribution of large matrix elements behind others. We investigate three methods of 1-sparse decomposition. Our circuit constructions can optionally take advantage of limited matrix bandwidth and repeated values. For example we consider digitisation (reduced precision), where the number of multiplexed rotation gates is equal to the number of non-unique matrix entries. We evaluate our methodologies using 2D and 3D CFD matrices for unstructured aerofoil meshes, structured cavity, and duct meshes, with and without matrix preconditioning. Our results show that we are able to achieve a block encoding with a near constant subnormalisation factor as the number of matrix preconditioning infill levels increases. This significantly reduces the subnormalised condition number and, in one case, reduces the degree of the QSP polynomial approximation to 1/x by 100,000. Reduced precision digitisation is shown to become more effective as the number of preconditioning infill levels is increased and, in one case, reduces the number of multiplexed rotations from 2,785,576 to 546 whilst maintaining an infidelity of 2.6imes10^{-5} relative to the classical solution. The effect of digitisation on QSVT solutions is demonstrated using 2D and 3D unstructured mesh aerofoil cases. Due to its flexibility and automatic applicability, we believe our 1-sparse decomposition block encoding can offer benefits to other quantum applications.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.27915) | 2026-10-21
