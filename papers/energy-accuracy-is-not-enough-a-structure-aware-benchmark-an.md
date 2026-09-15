---
title: "Energy Accuracy Is Not Enough: A Structure-Aware Benchmark and Evaluation Protocol for Quantum Architecture Search"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.04845"
summary: "arXiv:2607.04845v2 Announce Type: replace Abstract: Quantum architecture search for molecular ground-state estimation is commonly evaluated through energy accuracy, which does not describe circuit cos"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2607.04845v2 Announce Type: replace Abstract: Quantum architecture search for molecular ground-state estimation is commonly evaluated through energy accuracy, which does not describe circuit cost or the physical properties of the prepared state. We introduce HamQASBench, a structure-aware benchmark comprising eleven molecular Hamiltonians of up to fourteen qubits, selected using Hamiltonian and target-state properties and supplied with exact references. Its evaluation protocol combines energy accuracy and success rates with reference-relative circuit cost, local entropy profiles for non-degenerate targets, and state identification within degenerate ground subspaces. Experiments with five methods spanning four search paradigms reveal differences hidden by energy-only comparisons. On a near-product instance under the shallow search budget, the best outputs of all five methods reach chemical accuracy while using between two and sixty-two gates. Equal-energy outputs on a degenerate instance occupy distinct spin components. Local entropy profiles distinguish inaccurate outputs and show that entangling-gate counts need not reflect realized entanglement. Across the molecular instance ladder, product-state outputs can meet or miss chemical accuracy, motivating interpretation of success alongside target-state properties. These results support retaining energy as the task-success criterion while using circuit-cost and state diagnostics for more informative comparisons. The benchmark instances, references, evaluation implementation, and per-run data are released for reuse.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.04845) | 2026-09-15
