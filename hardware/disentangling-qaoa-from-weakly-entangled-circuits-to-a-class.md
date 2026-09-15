---
title: "Disentangling QAOA: From Weakly Entangled Circuits to a Classical QUBO Solver"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.15738"
summary: "arXiv:2609.15738v1 Announce Type: new Abstract: The role of entanglement in quantum optimization remains actively debated. To address this question, we focus on the fixed-parameter expanding-depth reg"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.15738v1 Announce Type: new Abstract: The role of entanglement in quantum optimization remains actively debated. To address this question, we focus on the fixed-parameter expanding-depth regime of the quantum approximate optimization algorithm (QAOA), where a compact two-parameter schedule is trained once on small instances and then applied as the problem size and circuit depth increase. To probe this regime beyond full state-vector simulation, we perform approximate matrix product state simulations for up to 50 qubits and 100 layers and quantify entanglement by the bond dimension. We observe an entangle--disentangle profile, with the peak bond dimension decreasing with depth and eventually saturating. This observation motivates an extreme approximation: projecting the state onto the product-state manifold (bond dimension one) after every two-qubit interaction. Based on this approximation, we introduce BOND-1, a quantum-inspired classical solver. Despite the drastic simplification, BOND-1 achieves cut ratios above 0.95 relative to the best known values on standard GSet MaxCut benchmarks with up to 20000 variables, and in some cases it matches those values. It achieves these results without per-instance optimization and has linear memory cost, while per-instance tuning can provide further improvement. These results show that, in this regime, a substantial fraction of the optimization power of QAOA survives even in the complete absence of entanglement. Our conclusions, however, are specific to this setting and do not imply that entanglement is unnecessary for quantum optimization in general.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.15738) | 2026-09-15
