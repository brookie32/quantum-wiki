---
title: "A Physics-Informed Neuro-Fuzzy Framework for Quantum Error Attribution"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.21253"
summary: "arXiv:2602.21253v3 Announce Type: replace Abstract: As quantum processors scale beyond 100 qubits, distinguishing software bugs from stochastic hardware noise becomes a critical diagnostic challenge. "
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2602.21253v3 Announce Type: replace Abstract: As quantum processors scale beyond 100 qubits, distinguishing software bugs from stochastic hardware noise becomes a critical diagnostic challenge. We present a neuro-fuzzy framework that addresses this attribution problem by combining Adaptive Neuro-Fuzzy Inference Systems (ANFIS) with physics-grounded feature engineering. We introduce the Bhattacharyya Veto, a hard physical constraint grounded in the empirically characterized weak-noise floor of the device, with CPTP contraction guaranteeing one-sided soundness that prevents the classifier from attributing topologically impossible output distributions to noise. Validated on IBM's 156-qubit Heron r2 processor (ibm_fez) across 105 circuits spanning 17 algorithm families, the framework achieves 89.5% effective accuracy (+/- 5.9% CI). The system implements a safe failure mode, flagging 14.3% of ambiguous cases for manual review rather than forcing low-confidence predictions. We resolve key ambiguities - such as distinguishing correct Grover amplification from bug-induced collapse - and identify fundamental limits of single-basis diagnostics, including a Z-basis blind spot where phase-flip errors remain statistically invisible. This work establishes a robust, interpretable diagnostic layer that prevents error mitigation techniques from being applied to logically flawed circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.21253) | 2026-09-04
