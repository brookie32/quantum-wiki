---
title: "Topological State-Aware Simulation Framework for Inter-Satellite Twin-Field QKD Networks"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.12659"
summary: "arXiv:2608.12659v1 Announce Type: new Abstract: Inter-satellite links (ISLs) are the mandatory backbone for global quantum networks. While Twin-Field Quantum Key Distribution (TF-QKD) successfully sur"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.12659v1 Announce Type: new Abstract: Inter-satellite links (ISLs) are the mandatory backbone for global quantum networks. While Twin-Field Quantum Key Distribution (TF-QKD) successfully surpasses linear rate-loss bounds, its extreme phase sensitivity makes it highly vulnerable to dynamic, non-IID (Independent and Identically Distributed) orbital environments. In composable finite-key analyses governed by the Generalized Entropy Accumulation Theorem (GEAT), traditional adaptive post-selection heuristics either violate strict independence conditions or incur massive second-order penalties that collapse the secret key rate. To overcome this, we introduce a reference-only topological post-selection oracle. By modeling the constellation as a Cellular Sheaf and applying Topological Data Analysis (TDA), our protocol derives a public acceptance event (Omega) exclusively from classical beacon telemetry. To rigorously validate this mechanism, we develop a modular simulation framework equipped with stochastic noise injection and an explicit GEAT security ledger. Simulations across 2,000-5,000 km ISL separations compare the same Hodge-Koopman gate with TDA disabled and enabled. At 2,000 km, the median conditional candidate rates are 2.14 imes 10^{-6} and 5.87 imes 10^{-7} bit per emitted pulse, respectively; both configurations return zero at 3,000-5,000 km. TDA is active in all 4,788 evaluated windows, but does not extend the positive-candidate range in this scenario. These exported rates are conditional numerical candidates: the full protocol-level composable-security proof remains incomplete and the certified composable rate is therefore zero throughout.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.12659) | 2026-08-14
