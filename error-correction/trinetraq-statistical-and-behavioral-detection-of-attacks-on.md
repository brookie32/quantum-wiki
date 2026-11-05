---
title: "Trinetra.Q: Statistical and Behavioral Detection of Attacks on the Quantum-Error-Correction Layer and Classical Control Stack of Quantum Computing Systems"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.05722"
summary: "arXiv:2611.05722v1 Announce Type: new Abstract: Most quantum-computer security work targets physical-layer attacks on qubits, while two surfaces remain inadequately defended: the quantum-error-correct"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.05722v1 Announce Type: new Abstract: Most quantum-computer security work targets physical-layer attacks on qubits, while two surfaces remain inadequately defended: the quantum-error-correction (QEC) syndrome-and-decoder pipeline, and the classical control and software stack that runs it. Tampering on these surfaces can corrupt a computation while the physical error rate appears normal, and can stay within a single-circuit integrity tolerance. We present Trinetra.Q, a detection layer of cooperating detectors, each monitoring a statistical or behavioral property of quantum-domain data against an envelope calibrated from honest operation, and raising an indication only on a statistically significant deviation. The detectors cover (A) QEC integrity over per-stabilizer firing rates, syndrome defect-count, and repeated-syndrome rate; (B) decoder confidence over the margin between minimum-weight error explanations in distinct logical classes; (C) behavioral output divergence, flagging crosstalk-class and novel attacks by their effect on a victim's output relative to a matched control; (D) control-stack tampering via known-answer canary circuits, built to be indistinguishable to a resident implant, with a cross-job consistency statistic; and (E) compilation/execution integrity. Each gates on significance, so honest operation raises no alarm. We evaluate in faithful simulation and on three production IBM Heron processors, and bound the physical attack surface with a systematic negative map: most physical-layer attacks return statistically null, the exception an implemented, measured within-job feed-forward covert-channel primitive. Every detector is also evaluated against an adaptive attacker with full knowledge of it. To our knowledge this is the first unified statistical-and-behavioral detection layer for the QEC layer and classical control stack of a quantum computing system, demonstrated on production hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.05722) | 2026-11-05
