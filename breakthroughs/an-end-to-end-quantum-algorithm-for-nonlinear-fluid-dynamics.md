---
title: "An end-to-end quantum algorithm for nonlinear fluid dynamics with bounded quantum advantage"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.03758"
summary: "arXiv:2512.03758v2 Announce Type: replace Abstract: Computational fluid dynamics (CFD) is a cornerstone of classical scientific computing, and there is growing interest in whether quantum computers ca"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2512.03758v2 Announce Type: replace Abstract: Computational fluid dynamics (CFD) is a cornerstone of classical scientific computing, and there is growing interest in whether quantum computers can accelerate such simulations. The existing proposals for fault-tolerant quantum algorithms for CFD have almost exclusively been based on the Carleman embedding method, used to encode nonlinearities on a quantum computer. Here, we first identify several key challenges that must be addressed in order to establish quantum advantage using this method, including Carleman convergence, time-stepping requirements, condition-number scaling, and data extraction. Building on this analysis, we develop a novel algorithm for the incompressible lattice Boltzmann equation that addresses them, and provide its detailed analysis, including all potential sources of algorithmic complexity, as well as gate count estimates. We find that for an end-to-end problem, a modest quantum advantage may be preserved for selected observables in the high-error-tolerance regime. We establish a lower bound for the Reynolds number scaling of our quantum algorithm in dimension D at Kolmogorov microscale resolution with O(Re^{frac{3}{4}(1+frac{D}{2})} imes q_M), where q_M is a multiplicative overhead for data extraction with q_M = O(Re^{frac{3}{8}}) for the drag force. This upper bounds the scaling improvement over classical algorithms by O(Re^{frac{3D}{8}}). However, our numerical investigations suggest a lower speedup, with a scaling estimate of O(Re^{1.936} imes q_M) for D=2. Our results give robust evidence that small, but nontrivial, quantum advantages can be achieved in the context of CFD, and motivate the need for additional rigorous end-to-end quantum algorithm development.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.03758) | 2026-09-28
