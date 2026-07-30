---
title: "Precise 2D electric field density simulations for superconducting quantum devices"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.26242"
summary: "arXiv:2607.26242v1 Announce Type: new Abstract: Dielectric loss due to two-level systems is a limiting factor for superconducting qubit relaxation times. These losses arise mostly from nanometer-scale"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.26242v1 Announce Type: new Abstract: Dielectric loss due to two-level systems is a limiting factor for superconducting qubit relaxation times. These losses arise mostly from nanometer-scale interfacial defect regions in superconducting devices with planar dimensions of microns to millimeters, thus making it resource intensive to accurately simulate the electric field density in these regions with traditional electromagnetic solvers. In this work, we demonstrate a fast boundary integral equation solver that allows precise simulation of electric field density in these thin regions, showing a speedup of around two orders of magnitude over traditional solvers, with relative errors around 10^{-7} for a ten-minute solution runtime. By computing participation ratios through Green's first identity without squaring the electric field, our approach is less susceptible to the field singularities near conductor corners. We apply this solver to a basic untrenched coplanar waveguide cross-section, showing that the common assumption of participation ratio linearity with dielectric constant holds well for some interfaces and not others; in particular, while the metal-air (MA) top and corner follow this linear relationship strongly, the MA sidewall does not. We then compare isotropic and anisotropic etching, showing that the MA sidewall and the metal-air-substrate triple junction are the most strongly affected. We are currently leveraging this solver to explore geometries that will uniquely isolate the participation ratios of the different dielectrics. Finally, we are working to combine this solver framework with a full 3D microwave solver to accurately calculate participation ratios for the thin dielectrics that are known sources of loss in superconducting qubits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.26242) | 2026-07-30
