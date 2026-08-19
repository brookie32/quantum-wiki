---
title: "New Methods and Frameworks for Quantum State Preparation in Modern Quantum Systems"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16937"
summary: "arXiv:2608.16937v1 Announce Type: new Abstract: This thesis studies exact, deterministic preparation of arbitrary dense n-qubit states, the data-loading step in quantum signal and image processing. It"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.16937v1 Announce Type: new Abstract: This thesis studies exact, deterministic preparation of arbitrary dense n-qubit states, the data-loading step in quantum signal and image processing. It derives two syntheses built on the Digital Signal-induced Heap Transform (DsiHT): the QsiHT Fast Path Real Synthesis and the QsiHT Fast Path Complex Synthesis. Both are benchmarked against ten configurations spanning the UCR, isometry, multiplexor, Schmidt/SVD, QSD, and heap-transform families. Several of those are realizations through Qiskit builders or compiler optimization, not from-scratch reimplementations. The n=3 noisy comparison spans ibm_fez, ibm_kingston, and ibm_marrakesh, three 156-qubit IBM Heron r2 processors, where single-submission nine-method jobs permit within-session family-wide Benjamini-Hochberg-corrected comparisons. The frontier-versus-QSD separation reproduces within one calibration on every device, but the within-frontier order does not reproduce across devices or calibration days. A deep-circuit n=8 run on ibm_fez shows the executed-count ordering re-emerge outside the run-to-run spread on the complex target. Depth was not isolated from mapping, gate composition, calibration, or session effects. All methods are exact to machine precision and differ only in cost. Under noise the coarse error tier tracks the executed (routed) two-qubit count, separating the Theta(2^n) frontier from QSD's Theta(4^n) and nothing finer. Both syntheses realize the deployed Qiskit StatePreparation floor of 2^n-n-1 CNOTs, undercutting every other from-scratch method on the as-built CNOT axis. The Real Synthesis serves real (sign-bearing) targets and holds the lowest classical build cost among the exact loaders at large register sizes, through one fast Walsh-Hadamard pass. The Complex Synthesis serves arbitrary complex targets and ties Qiskit's StatePreparation for the lowest simulated sampled error.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16937) | 2026-08-19
