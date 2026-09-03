---
title: "A variational quantum eigensolver-based cutting plane framework for semidefinite programming problems"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.02139"
summary: "arXiv:2609.02139v1 Announce Type: new Abstract: Semidefinite programming plays a key role in optimization, with broad impact across control theory, machine learning, and combinatorial optimization. Al"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02139v1 Announce Type: new Abstract: Semidefinite programming plays a key role in optimization, with broad impact across control theory, machine learning, and combinatorial optimization. Although semidefinite programs are polynomially solvable, several commonly used algorithms rest on a linear-algebraic step whose running time grows cubically with the matrix dimension and which requires the matrix itself to be held in memory, at quadratic cost. In this study, we propose replacing it with a variational quantum eigensolver, whose qubit requirement is logarithmic in the matrix dimension, and present the first end-to-end implementation of such an approach within a cutting-plane framework, together with an operator-derived ansatz whose entanglement structure is read directly from the Pauli support of the candidate matrix. Evaluated on the control family of SDPLIB against an identical scheme driven by an exact eigendecomposition, the variational oracle produces valid cuts throughout, closing 32 to 82% of the initial optimality gap against a near-constant 75 to 82% for the exact oracle. Implementing and measuring the method end to end surfaces several effects not visible from theoretical analyses alone: where memory is actually consumed, how the padding required to fit a matrix onto a quantum register can mislead the variational optimizer, and why the candidate matrices prove dense in the Pauli basis, reducing the operator-derived ansatz to full entanglement. We report these findings and discuss their implications for near-term hybrid quantum-classical approaches.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.02139) | 2026-09-03
