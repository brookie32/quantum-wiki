---
title: "Estimating Irving-Kirkwood pressure profiles from per-atom virial and density profiles: a closure for the contour-dependent term in planar liquid films"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.41906"
summary: "arXiv:2610.41906v1 Announce Type: new Abstract: The local pressure tensor of an inhomogeneous fluid is not unique. Two tangential profiles are in common use in planar simulations: the Irving-Kirkwood "
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41906v1 Announce Type: new Abstract: The local pressure tensor of an inhomogeneous fluid is not unique. Two tangential profiles are in common use in planar simulations: the Irving-Kirkwood (IK) profile, which requires a dedicated pass over every pair of atoms for every slab, and the per-atom virial (PAV) profile, which molecular-dynamics codes produce at negligible cost and coincides with the Harasima contour. The two differ by the derivative of a pair quantity, P_T^IK - P_T^PAV = dQ/dz. We show that, for Lennard-Jones free-standing films, Q(z) can be predicted from the density profile and the bulk radial distribution function of the coexisting liquid: under the closure rho2(r1,r2) ~ rho(z1) rho(z2) g(r12), with a pair-local interpolation of g between its liquid and dilute limits, Q is a double integral of rho(z) against a kernel built from u'(r) g(r). The estimator P_T^IK,est = P_T^PAV + dQ/dz is tested against IK profiles measured on the same trajectories for 20 films (thicknesses 7-25 sigma, three cutoff radii, two temperatures): the root-mean-square residual is 0.001-0.002 epsilon/sigma^3, against 0.010-0.021 for the uncorrected profile, and Q, the amount that the contour choice transfers between the two interfaces of a film with non-equivalent surfaces, is recovered to within 0.6% of the surface tension. Applied to the normal component, the same closure removes 83-92% of the spurious structure of the per-atom zz profile, a test that needs no IK run. Its mixture form is validated on three two-component films with an adsorbate unequally distributed between their faces, where it resolves the tension of each face; a clean face recovers the tension of the pure film.



## Related
- [[estimating-the-disjoining-pressure-of-liquid-nanofilms-from-|Estimating the disjoining pressure of liquid nanofilms from molecular dynamics simulations via implicit treatment of the bulk liquid phase]]
- [[molecular-insights-into-gas-nanofilms-confined-between-bulk-|Molecular Insights into Gas Nanofilms Confined Between Bulk Liquid Phases]]

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.41906) | 2026-11-02
