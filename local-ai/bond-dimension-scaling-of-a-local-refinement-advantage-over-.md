---
title: "Bond-dimension scaling of a local-refinement advantage over hyperoptimized tensor-network contraction on Sycamore like topologies"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "local-ai"
tags: [local-ai, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25532"
summary: "arXiv:2604.25532v1 Announce Type: new Abstract: We identify a missing local-refinement stage in the cotengra tensor-network contraction pipeline and show that its impact grows monotonically with bond "
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25532v1 Announce Type: new Abstract: We identify a missing local-refinement stage in the cotengra tensor-network contraction pipeline and show that its impact grows monotonically with bond dimension on the connectivity graph of Sycamore-like topologies. Appending a nearest-neighbor interchange (NNI) search to the otengra{} output at matched 8-s wallclock yields a median predicted cost-model gap DeltafT at n{=}500 that grows monotonically and approximately linearly in hi, from sim!15~bits at hi{=}2 to sim!116~bits at hi{=}16 (Fig.~ref{fig:chi_sweep}), with the refiner winning on 25/25 seeds at every tested hi. Two control families -- random 3-regular and QAOA p{=}2 interaction graphs -- show median |DeltafT| leq 0.71~bits across both controls at every hi, with refiner win rate falling toward chance as hi grows; the signal is topology-specific, not a generic refinement-budget effect. An ablation establishes that refinement itself, not the four-axis Pareto acceptance rule, drives the gain (|DeltafT| lesssim 0.1 bits between scalar and Pareto arms at hi{=}2). The Sycamore-circuit envelope (App.~ref{em:sec:results:syccirc}) reports the corresponding refinement on actual random circuits at depths m in {4, 6, 8, 10, 12}, where the refiner wins on 5/5 instances at every depth. The advantage is therefore largest precisely in the bond-dimension regime relevant to physical contraction.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25532) | 2026-04-29
