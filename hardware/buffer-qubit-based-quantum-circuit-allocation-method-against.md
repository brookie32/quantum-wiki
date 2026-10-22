---
title: "Buffer-Qubit-Based Quantum Circuit Allocation Method Against Crosstalk Attacks"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.29050"
summary: "arXiv:2610.29050v1 Announce Type: new Abstract: Quantum Multi-Programming (QMP) enables the simultaneous execution of quantum circuits from multiple users on a single quantum chip in cloud quantum com"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.29050v1 Announce Type: new Abstract: Quantum Multi-Programming (QMP) enables the simultaneous execution of quantum circuits from multiple users on a single quantum chip in cloud quantum computing services. However, QMP is vulnerable to crosstalk attacks, in which a malicious user deliberately induces crosstalk to disrupt other users' computations. As a countermeasure, prior work has proposed the use of buffer qubits, which remain idle and are allocated between quantum circuits to suppress the effect of crosstalk. Nevertheless, to the best of our knowledge, such countermeasures have not been publicly reported in production quantum cloud software. In this paper, we extend the QMP of OQTOPUS, open-source software that is already in production use for operating real quantum computers, with a buffer-qubit-based circuit allocation method. Experiments on a real device characterize the attack effect in terms of energy relaxation and dephasing, showing that observable degradation appears in dephasing characteristics of qubits adjacent to the attacker circuit. Based on this result, we release the proposed method as part of OQTOPUS and confirm that the buffer qubits are correctly reserved around the allocated circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.29050) | 2026-10-22
