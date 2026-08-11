---
title: "Dissipative continuation for ground-state preparation at chemical transition states"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.11603"
summary: "arXiv:2602.11603v3 Announce Type: replace Abstract: Simulating chemical reactions exhibits a pronounced unevenness in computational difficulty: while equilibrium reactant and product geometries are of"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2602.11603v3 Announce Type: replace Abstract: Simulating chemical reactions exhibits a pronounced unevenness in computational difficulty: while equilibrium reactant and product geometries are often tractable, transition-state (TS) geometries frequently display strong multi-reference character that challenges both classical solvers and coherent quantum state-preparation methods. We introduce a dissipative continuation protocol for preparing electronic ground states near TS geometries within a hybrid classical--quantum workflow. In the intended setting, classical electronic-structure methods supply an approximate TS geometry, a computationally motivated continuation path, and a locally compatible active-space representation along that path. Starting from a warm start at a tractable geometry on the same aligned path, the quantum routine transports the state toward the TS using orbital-gauge-aligned Hamiltonians and engineered dissipative cooling primitives that repeatedly contract population into the instantaneous low-energy sector. We prove that, for continuation paths satisfying a Lipschitz smoothness condition and a localized Eigenstate Thermalization Hypothesis (ETH)-motivated downward-drift condition within the relevant energy window, the ground state at the target geometry can be prepared to total energy error epsilon_E with total ideal cooling-step complexity widetilde{O}(C_{DK}^2 N_o^2 / epsilon_E). Here C_{DK} quantifies ground-state rotation along the aligned path. The corresponding logical gate count is obtained by multiplying this primitive count by the cost of implementing one dissipative step, which is polynomial in the block-encoding size of the Lindbladian under standard Lindblad-simulation algorithms. This identifies a structured regime in which dissipative continuation provides a conditional route to ground-state preparation at strongly correlated TS geometries.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.11603) | 2026-08-11
