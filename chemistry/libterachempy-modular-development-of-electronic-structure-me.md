---
title: "libterachem.py: Modular development of electronic structure methods with graphical processing units"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.02540"
summary: "arXiv:2610.02540v1 Announce Type: new Abstract: We present libterachem.py, a Python interface and method framework that facilitates development and prototyping of electronic structure methods while le"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.02540v1 Announce Type: new Abstract: We present libterachem.py, a Python interface and method framework that facilitates development and prototyping of electronic structure methods while leveraging TeraChem's optimized graphical processing unit (GPU) operations. Direct access to these building blocks and their intermediate quantities allows users to assemble and modify methods within Python while reusing the underlying GPU implementations. A layered architecture, programmable at both the operation level and the method level, supports numerical experimentation, composition of complete electronic structure methods with interchangeable components, and integration with external scientific libraries. We illustrate operation-level use with grid pruning for least-squares tensor hypercontraction and with exchange--correlation functionals supplied through LibXC and by the machine-learned Skala functional. We illustrate method-level use with dispersion corrections, periodic calculations, and geometry optimization with an external optimizer. Python-driven self-consistent-field calculations using libterachem.py incur no significant computational overhead compared to native TeraChem and preserve its multi-GPU scaling. A photoactive yellow protein QM/MM molecular dynamics application further demonstrates throughput comparable to native TeraChem in a workflow composed with external simulation libraries. These results establish libterachem.py as a platform for method development and interoperable molecular simulation that retains the performance of TeraChem's GPU operations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.02540) | 2026-10-05
