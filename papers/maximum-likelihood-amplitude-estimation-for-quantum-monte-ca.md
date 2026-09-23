---
title: "Maximum-Likelihood Amplitude Estimation for Quantum Monte Carlo Integration on Trapped-Ion Hardware: Convergence, Noise-Floor Saturation, Depth-Dependent Bias"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.25992"
summary: "arXiv:2609.25992v1 Announce Type: new Abstract: Quantum Amplitude Estimation promises to accelerate Monte Carlo integration by replacing the classical arepsilon propto N^{-1/2} sampling law with the H"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.25992v1 Announce Type: new Abstract: Quantum Amplitude Estimation promises to accelerate Monte Carlo integration by replacing the classical arepsilon propto N^{-1/2} sampling law with the Heisenberg-limited arepsilon propto N^{-1} scaling, but whether any part of that advantage survives on present-day hardware is an empirical question. We report a systematic experimental benchmark of a Maximum-Likelihood Amplitude Estimation QMC pipeline on IonQ trapped-ion processors, comprising 60 hardware trials on IonQ Forte-1 across five settings(5 & 9 qubits, 100-200 shots per depth, linear & exponential amplification schedules, ~113 device-hours), together with 100 trials on IonQ Aria-1 & Forte-1 noise models at 5, 9 & 19 qubits. The pipeline combines controlled-R_y rotational state preparation, Grover-based amplitude amplification and maximum-likelihood inference and is benchmarked against b_{max}^{-1}!int_0^{b_{max}}!sin^2!x,dx with b_{max}=pi/5 ,given results emerge. First, the noiseless limit it attains arepsilon propto N^{-0.88}, close to the Heisenberg-scaling reference, reducing the error 54-74x over a 133x increase in oracle calls. Second, scaling does not survive on hardware. Every noisy backend saturates at an error floor of (2-5)x 10^{-2}, with fitted exponents of 0.04-0.15 on Forte-1 linear schedules and alpha le!0 on the vendor noise models: beyond the optimal shallow depth, however, deeper amplification provides no sustained accuracy gain and instead returns to the noise floor. Forte-1 hardware also outperformed IonQ's own Aria-1 noise model at every depth m ge 2, indicating that vendor noise models are bad predictors of MLAE accuracy. The practical implication for UQ is that on current devices the useful operating point is a shallow, schedule-tuned amplification depth chosen so that the deepest circuit lands near p~1/2 not the deepest schedule the coherence budget allows.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.25992) | 2026-09-23
