---
title: "Fast and Sure-ious Quantum Process Tomography"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39941"
summary: "arXiv:2609.39941v1 Announce Type: new Abstract: Quantum process tomography (QPT) protocols are often designed by lifting quantum state tomography (QST) protocols through the Choi-Jamiolkowski isomorph"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39941v1 Announce Type: new Abstract: Quantum process tomography (QPT) protocols are often designed by lifting quantum state tomography (QST) protocols through the Choi-Jamiolkowski isomorphism, at the cost of an extra step enforcing the trace-preserving (TP) constraint. Existing approaches fall into two classes. The folklore partial normalization, which sandwiches the density estimate between inverse square roots of its input marginal, has a closed form but is used as a heuristic, its only analyses being asymptotic and losing a factor polynomial in the dimension. Projection-based methods are principled but have no closed forms and scale poorly with dimension. We resolve this dichotomy by showing that the partial normalization is the exact projection onto the Choi states of quantum channels in fidelity (equivalently in Bures or purified distance). Consequently, any QST algorithm with guarantees in fidelity lifts to a QPT algorithm that inherits its sample complexity, through a single closed-form congruence that preserves the Choi rank and is computed in Kraus form without any eigendecomposition of Choi dimension. We lift two single-copy protocols and prove that the non-adaptive one (Fidelity Projected Least Squares) recovers the Choi rank and reaches infidelity arepsilon from a number of channel uses proportional to 1/arepsilon. Numerically, for channels of low Choi rank, it improves on the state-of-the-art projected least squares in accuracy, and by orders of magnitude in the time and memory of the TP-regularization step and of the returned estimate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39941) | 2026-10-01
