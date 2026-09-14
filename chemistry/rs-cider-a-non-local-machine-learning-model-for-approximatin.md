---
title: "RS-CIDER: A non-local machine learning model for approximating screened hybrid functionals"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.13139"
summary: "arXiv:2609.13139v1 Announce Type: cross Abstract: Screened hybrid functionals such as HSE06 improve the description of band gaps, charge localization, and redox energetics relative to semilocal approx"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.13139v1 Announce Type: cross Abstract: Screened hybrid functionals such as HSE06 improve the description of band gaps, charge localization, and redox energetics relative to semilocal approximations, but their explicit Hartree-Fock exchange term is computationally costly for large, periodic systems, especially in plane-wave basis set calculations. Here we present RS-CIDER, a machine-learned non-local exchange functional that approximates the short-range Hartree-Fock exchange term in HSE06 by explicitly fitting both ground-state energies and single-particle energy levels. RS-CIDER combines scale-invariant semilocal and non-local density descriptors and can be evaluated self-consistently without explicitly applying the short-range Hartree-Fock exchange operator. RS-CIDER shows close agreement with HSE06 for molecular reaction energies and solid-state band gaps. Further tests across distinct materials show agreement between RS-CIDER and HSE06 for local magnetism, Cu-O phase competition, polaron localization, and neutral-defect energetics. For an Fe olivine, chemistry-specific fine-tuning recovers the HSE06 Li intercalation voltage. A timing benchmark shows that RS-CIDER reduces the measured per-SCF-step wall time by more than an order of magnitude relative to HSE06. Together, these molecular and solid-state results establish RS-CIDER as an efficient self-consistent machine-learned surrogate for HSE06.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.13139) | 2026-09-14
