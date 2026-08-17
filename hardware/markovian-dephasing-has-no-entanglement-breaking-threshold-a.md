---
title: "Markovian dephasing has no entanglement-breaking threshold, and a fixed tolerance will report one anyway"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.08587"
summary: "arXiv:2604.08587v3 Announce Type: replace-cross Abstract: When modelling decoherence in a biological spin system it is tempting to seek a critical rate beyond which the channel is entanglement-breakin"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2604.08587v3 Announce Type: replace-cross Abstract: When modelling decoherence in a biological spin system it is tempting to seek a critical rate beyond which the channel is entanglement-breaking (EB) and quantum resources are gone. We show that for the two channel families in which such a model would be posed, no critical rate exists. For uniform dephasing at rate gamma the partial transpose of the Choi state has eigenvalue -e^{-gamma}/d, so the channel is non-PPT -- hence not EB -- at every finite gamma. Adding amplitude damping changes nothing: the qubit map's partial transpose stays negative at all finite rates. What does vanish at a finite rate is the coherent information, exactly where the qubit map turns antidegradable: the root of c^{2}=p, gamma_{Ic}=0.668 at kappa=0.1. Antidegradability survives tensor products, so the single-letter and regularised thresholds coincide: of the three properties usually conflated here, two share one finite boundary and the third has none. Our main object is the numerical mechanism that manufactures a threshold where there is none. A quantity that decays exponentially to zero without reaching it, tested against a fixed absolute cutoff, yields a "threshold" set by the cutoff: the PPT test gives gamma=5.49 at epsilon=10^{-10} and 6.58 at 10^{-12}, sliding by 0.55 per decade. We reported the first number in three now-retracted preprints. Preparing this paper we made the same error three more times -- most seriously in gamma_{Ic} itself, which a bisection against a 10^{-7} cutoff placed at 0.62 -- and we document all four instances, with the closed forms and code that avoid them.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.08587) | 2026-08-17
