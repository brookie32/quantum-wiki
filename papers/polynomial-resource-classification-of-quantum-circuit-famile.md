---
title: "Polynomial Resource Classification of Quantum Circuit Familes via Classical Shadows"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25708"
summary: "arXiv:2604.25708v1 Announce Type: new Abstract: We compare four polynomial-resource measurement strategies, (I) Z-basis-only, (II) nearest-neighbor ZZ (NN), (III) multi-basis (Z, X, Y), and (IV) class"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25708v1 Announce Type: new Abstract: We compare four polynomial-resource measurement strategies, (I) Z-basis-only, (II) nearest-neighbor ZZ (NN), (III) multi-basis (Z, X, Y), and (IV) classical shadows, for classifying three quantum circuit families: IQP, Clifford, and Clifford+T. We find Z-only measurements outperform multi-basis and classical shadows across all qubit counts and all four classifiers evaluated, and the O(nqubits)-feature NN strategy matches Z-only to within 0.02 in Random Forest accuracy. The best result is a Random Forest accuracy of 0.91 at 4--5 qubits under Z-only (0.89 for NN, 0.85 for multi-basis, 0.67 for shadows). All four strategies collapse to near-chance accuracy (approx 0.33) above approximately 12 qubits under the quadratic shot budget shots = 16nqubits^2. These findings indicate that the discriminative signal between these circuit families is concentrated in local, nearest-neighbor Z-basis correlations, consistent with the diagonal gate structure of IQP circuits, and that additional Pauli correlator types or long-range correlations carry no compensating discriminative power for this task. We provide a formal theoretical framework showing that circuits with high diagonal fraction in a given basis concentrate their correlator structure in that basis, and that any deviation from the dominant basis incurs a provably higher estimator variance. These results establish that a quadratic shot budget is insufficient for reliable classification above approximately 12 qubits, but do not rule out the existence of a subquadratic or otherwise more efficient polynomial-resource strategy; whether any polynomial measurement protocol can classify these families at large qubit counts remains an open question.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25708) | 2026-04-29
