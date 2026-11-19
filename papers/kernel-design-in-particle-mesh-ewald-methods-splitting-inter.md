---
title: "Kernel Design in Particle Mesh Ewald Methods: Splitting, Interpolation, and Upsampling"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.23737"
summary: "arXiv:2611.23737v1 Announce Type: cross Abstract: For more than thirty years, particle mesh Ewald (PME) methods have dominated the computation of electrostatic interactions in molecular dynamics. A PM"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23737v1 Announce Type: cross Abstract: For more than thirty years, particle mesh Ewald (PME) methods have dominated the computation of electrostatic interactions in molecular dynamics. A PME method uses a splitting kernel to divide the interaction into a local part, summed within a cutoff, and a smooth part, computed on a grid with a spreading and interpolation (SI) kernel. The established methods use Ewald's Gaussian split with B-spline SI kernels, and the recent Ewald summation with prolates accelerates them severalfold by using a prolate spheroidal wave function (PSWF) for both kernels. Neither choice meets two needs of molecular dynamics: a smooth energy, which long simulations need in order to conserve it, and a low-order SI kernel that stays accurate on coarse grids and gains accuracy as the grid is refined. We present a framework for designing both kernels to meet these needs. For inverse powers from the Coulomb to the dispersion interaction, our splits make the local part smooth at the cutoff to any order while keeping the Fourier concentration of the smooth part close to optimal. We show that with analytic differentiation, the force error of a continuous SI kernel of fixed shape vanishes under grid refinement only if every particle, wherever it lies, gives the grid its exact charge and dipole moment. Our SI kernel for the Coulomb interaction ensures this by construction and is twice continuously differentiable. Compared with the B-spline of the same order, it needs fewer grid points by a factor of up to nearly five; on coarse grids, it mostly needs a lower order than the PSWF kernel. In simulations of liquid water over 100 million time steps, the new kernels reduce the energy drift of both the established and the PSWF kernels by about three orders of magnitude, with a smaller force error than either. Existing PME codes can adopt them by replacing only the two kernels and the Fourier multiplier.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.23737) | 2026-11-19
