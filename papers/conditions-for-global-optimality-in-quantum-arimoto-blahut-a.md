---
title: "Conditions for Global Optimality in Quantum Arimoto-Blahut Algorithms"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.09731"
summary: "arXiv:2609.09731v1 Announce Type: cross Abstract: Generalized Arimoto--Blahut (AB) algorithms are widely used in information theory and quantum optimization, but monotonic objective decrease and numer"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.09731v1 Announce Type: cross Abstract: Generalized Arimoto--Blahut (AB) algorithms are widely used in information theory and quantum optimization, but monotonic objective decrease and numerical stabilization do not guarantee global optimality. We establish necessary and sufficient conditions for the global optimality of full-rank AB fixed points for convex differentiable objectives under linear constraints. An AB fixed point is globally optimal if and only if the AB update direction and the objective gradient differ by an element of the constraint normal space at that point. The same compatibility condition characterizes agreement between individual AB and mirror-descent (MD) updates, whereas pathwise equivalence requires it along the entire common trajectory. Thus, an AB algorithm may follow a trajectory different from MD and still reach the global optimum. We also develop a posteriori optimality certificates based on feasible directional derivatives, including finite-difference upper bounds on the objective gap that require only objective evaluations. For channel relative entropy between dephasing and depolarizing channels, we analytically identify the global minimizer as the unique full-rank AB fixed point, although pathwise equivalence fails. Numerical experiments illustrate convergence of AB and MD along different trajectories and validate the certificates. By contrast, an amplitude-damping example shows that a monotone AB iteration can stabilize at a suboptimal fixed point, whose nonoptimality is detected by the finite-difference certificate. These results provide structural and computable criteria for assessing global optimality in quantum AB algorithms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.09731) | 2026-09-10
