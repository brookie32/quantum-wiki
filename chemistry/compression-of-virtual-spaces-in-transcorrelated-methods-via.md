---
title: "Compression of virtual spaces in transcorrelated methods via singular value decomposition: application to the G2 set"
date: "2026-08-12"
updated: "2026-08-12"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.10658"
summary: "arXiv:2608.10658v1 Announce Type: new Abstract: We introduce a new singular-value-decomposition-based scheme for constructing small virtual spaces out of large basis sets for transcorrelated (TC) calc"
last_verified: "2026-08-12"
review_by: "2026-11-10"
stale: false
---

arXiv:2608.10658v1 Announce Type: new Abstract: We introduce a new singular-value-decomposition-based scheme for constructing small virtual spaces out of large basis sets for transcorrelated (TC) calculations, termed SVD-TC. This work builds on the recent finding that the residual basis error in the TC reference energy converges more slowly than that of the correlation energy. Within the new workflow, the post Hartree-Fock TC calculation is performed in a compressed virtual orbital subspace, obtained by projecting the canonical virtual orbitals from a large basis set onto a smaller basis set through singular value decomposition (SVD). This allows us to achieve the high accuracy allowed by the large basis, whilst the bottleneck steps - TC integral calculation and post-HF correlation method such as CCSD(T) - incur the cost of only a small virtual space calculation. The method therefore is highly efficient, whilst avoiding the composite nature of the reference correction method. Using the new scheme, we widen the scope of benchmark-quality TC results into more complex molecules than previously considered: using the G2-1 set of 55 molecules with first- and second-row atoms, we apply SVD-xTC-CCSD(T) to compute atomization energies. We compare our results against the near-exact semistochastic heat-bath configuration interaction (SHCI) reference values and experiment. We find that SVD-xTC-CCSD(T) delivers chemical accuracy already with triple-zeta basis sets. Finally, we use the quadruple-zeta results to analyze the accuracy of pseudopotentials within the TC method, and show that pseudopotential TC workflow provides faster basis-set convergence than all-electron TC. We also present timings for computing the atomization energies on G2-1 set, demonstrating the efficiency of our TC workflows.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.10658) | 2026-08-12
