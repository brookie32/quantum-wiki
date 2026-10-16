---
title: "monoprop: Scaling Pauli and Majorana propagation via Anticommutation Indices"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.21000"
summary: "arXiv:2610.21000v1 Announce Type: new Abstract: We introduce monoprop, an open-source, massively parallel operator-propagation framework for fermion and qubit bases. For N qubits or modes, existing co"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.21000v1 Announce Type: new Abstract: We introduce monoprop, an open-source, massively parallel operator-propagation framework for fermion and qubit bases. For N qubits or modes, existing codes represent each of the K tracked operator terms (Pauli strings or products of Majorana operators) as a 2N-bit string, testing each for anticommutation with the gate at O(KN) cost per gate. Here, we introduce the anticommutation index which rapidly looks up the terms anticommuting with a gate. A local gate changes only the terms that touch its sites, and when terms are truncated to act on few sites, only a fraction sim1/N touch any given qubit or mode, and we use this to prove the time per gate scales as O(K/N). This counterintuitive result tells us that for a fixed number of terms, increasing the number of sites can make things faster. We demonstrate this numerically, and show monoprop scales almost ideally to 8192 cores, tracking 9.5imes10^{10} terms. Beyond propagation, we present memory-efficient surrogate graphs, which record one propagation and replay it at new angles, for fast energy re-estimation and parameter gradients, and an efficient method for finding energy-minimising gates and optimal angles for simulating adaptive quantum-chemistry circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.21000) | 2026-10-16
