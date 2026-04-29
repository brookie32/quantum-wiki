---
title: "Accelerated Surface Hopping via Scaling the Spin--Orbit Coupling: Opportunities for Machine Learning"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "applications"
tags: [applications, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2604.25603"
summary: "arXiv:2604.25603v1 Announce Type: new Abstract: Surface hopping (SH) methods are typically employed to simulate ultrafast nonadiabatic processes, but long timescales often remain beyond their reach. T"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25603v1 Announce Type: new Abstract: Surface hopping (SH) methods are typically employed to simulate ultrafast nonadiabatic processes, but long timescales often remain beyond their reach. To address this, accelerated SH scheme mitigate this limitation by scaling the driving forces of such process, either nonadiabatic couplings (NACs) in case of internal conversion or spin-orbit couplings (SOCs) for intersystem crossing. However, obtaining the actual time constant requires extrapolation from several ensembles of trajectories with different scaling factors. This introduces a significant computational demand, often restricting the number of trajectories per ensemble and, therefore, reducing the statistical confidence in the resulting time constant. In this work, we investigate the accelerated scheme using silaethylene (CH_2SiH_2) as a case study, evaluating various population fitting methods and extrapolation techniques. We trained machine learning models for potential energy surfaces (PESs) and NACs, and extended our rotate-predict-rotate approach to fit SOCs. These models demonstrate high performance, yielding populations within the confidence interval of the reference MR-CISD/SA-CASSCF(2,2) data; however, the extrapolation itself is highly sensitive to the fitted time constants, leading to discrepancies in the final time constant. Finally, we showcase and discuss how ML models can enhance the reliability of an accelerated SH scheme.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2604.25603) | 2026-04-29
