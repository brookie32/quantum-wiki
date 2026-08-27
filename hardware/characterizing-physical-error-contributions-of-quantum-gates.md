---
title: "Characterizing Physical Error Contributions of Quantum Gates"
date: "2026-08-27"
updated: "2026-08-27"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2305.08916"
summary: "arXiv:2305.08916v3 Announce Type: replace Abstract: Large-scale quantum computation requires a reliable assessment of the main sources of error in the implemented quantum gates. To this aim, we provid"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

arXiv:2305.08916v3 Announce Type: replace Abstract: Large-scale quantum computation requires a reliable assessment of the main sources of error in the implemented quantum gates. To this aim, we provide a learning-based framework that extracts the contribution of each physical error source to the infidelity of a series of gates, together with an uncertainty estimate for every contribution. Crucially, the uncertainties provided by the underlying Gaussian Process Regression serve as a diagnostic of the assumed noise model itself: if the physical model does not fully explain the experimental observations, the framework signals this instead of returning a falsely precise error budget. We demonstrate the proposed budget learning procedure on a pair of qubits in a transmon array architecture, where we compute the error budgets of the native single- and two-qubit gates. For this purpose, we have also developed an advanced noise model based on the first-principles understanding of the error processes in current superconducting processors, including complex (e.g. non-Markovian) error sources. While the single-qubit budgets are reconstructed with high confidence, the same diagnostic reveals that even this detailed noise model does not fully capture the error dynamics of a state-of-the-art two-qubit gate --- quantitative evidence that uncertainty-aware error budgeting is necessary for the characterization of current quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2305.08916) | 2026-08-27
