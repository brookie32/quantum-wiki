---
title: "Tensor Networks as an Explicit Interface for Quantum Block-Encodings"
date: "2026-08-06"
updated: "2026-08-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.00935"
summary: "arXiv:2510.00935v3 Announce Type: replace Abstract: Tensor networks (TNs) give explicit classical descriptions of structured finite linear maps, while block-encodings (BEs) are the standard quantum ac"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

arXiv:2510.00935v3 Announce Type: replace Abstract: Tensor networks (TNs) give explicit classical descriptions of structured finite linear maps, while block-encodings (BEs) are the standard quantum access model for such maps. We establish TNs as a universal data interface for quantum algorithms: any explicitly specified TN for an arbitrary finite linear map compiles directly to an explicit qubit BE, with no penalty on the selected-block round trip under faithful compression. Along a chosen sweep, the compiler handles local non-unitarity by exact local dilations and aggregates the resulting post-selection conditions online using logarithmically many additional flag qubits. The chosen sweep incurs three exact, sweep-dependent costs (the accumulated scale, the frontier memory, and the number of genuinely dilated local steps), which the main theorems are stated in terms of. In the bounded-local explicit arithmetic model, this yields linear-time compilation to linear-size circuits with constant-size local gadgets, and hence a constant-factor size correspondence between bounded-local TNs and bounded-local BEs. The same construction gives a selected-block round trip BE->TN->BE: a BE canonically yields a TN for its selected block rather than for an arbitrary unitary extension, which can then be compressed or approximated classically before recompilation. Faithful Schmidt-rank compression transfers monotonically (the scale cost and frontier memory cannot increase, with operator error bounded by the discarded weight), while arbitrary restructuring admits no general scale guarantee, a limitation we show is unavoidable. As consequences and limits of this scale accounting, we characterize exact scale optimality, show that bridge-hourglass forests admit scale-optimal sweeps after exact recursive local bond compression, and prove that certifying unrestricted exact scale optimality is already hard for diagonal MPOs on a path unless P=NP.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.00935) | 2026-08-06
