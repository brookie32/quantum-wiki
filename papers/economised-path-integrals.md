---
title: "Economised path integrals"
date: "2026-08-06"
updated: "2026-08-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2607.06414"
summary: "arXiv:2607.06414v3 Announce Type: replace Abstract: The Hessian of the ring polymer spring potential in the standard Trotter path integral is a Pimes P symmetric circulant matrix with a centroid eigen"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

arXiv:2607.06414v3 Announce Type: replace Abstract: The Hessian of the ring polymer spring potential in the standard Trotter path integral is a Pimes P symmetric circulant matrix with a centroid eigenvalue of zero. All such matrices commute and are diagonalised by the same bead to normal mode transformation matrix, and their eigenvalues contain lceil P/2rceil-1 degenerate pairs by symmetry. However, this still leaves some freedom to improve on the Trotter approximation: one can optimise the remaining lfloor P/2rfloor independent non-zero normal mode frequencies to fit the exact quantum mechanical radii of gyration of harmonic ring polymers with frequencies in the range 0leomegaleomega_{rm max}, where omega_{rm max} is the maximum physical frequency in the problem of interest. The optimisation involves solving a simple least squares problem for the optimum (economised or "Eco") internal mode frequencies. The remainder of the calculation then proceeds in the same way as a Trotter path integral calculation. An example application to hexagonal ice shows that the convergence of the Eco path integral is comparable to that of the 4th order Suzuki-Chin path integral, but with purely 2nd order Trotter effort. There is no need to calculate the projected Hessians that arise in the Suzuki-Chin method by finite differences, there is no need to develop any new estimators for observables, and once the Eco frequencies have been calculated the implementation of the Eco path integral involves changing just a few lines of a Trotter path integral code. To provide a more impressive example we have implemented the Eco method in GPUMD and used it to converge the (negative) thermal expansion coefficient and the constant pressure heat capacity of MOF-5 with a machine-learned neuroevolution potential.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2607.06414) | 2026-08-06
