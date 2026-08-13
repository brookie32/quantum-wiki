---
title: "The optimization landscape of peaked-circuit generation"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.11890"
summary: "arXiv:2608.11890v1 Announce Type: new Abstract: Peaked circuits are random quantum circuits whose measurement returns one bitstring far more often than chance. They are a candidate route to verifiable"
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.11890v1 Announce Type: new Abstract: Peaked circuits are random quantum circuits whose measurement returns one bitstring far more often than chance. They are a candidate route to verifiable quantum advantage, and the bottleneck is classical generation. Aaronson and Zhang fix a random circuit, append a trainable brickwall of half that depth, and optimize it by gradient descent to raise the probability of one chosen output string. Their method plateaus at a size-dependent ceiling, which they attribute to a barren plateau. A dichotomy remains open: either the optimizer stops short, so a better algorithm would reach higher, or no efficient method exists. We map the landscape on which the answer depends. Across 18 instances per size at n = 8-16, at fixed and converged budgets, no fixed-base exponential, the law they fit, matches the optimizer's reach: at convergence the decay steepens from 1.16 to 1.295 per qubit through n = 16 (p = 0.011 frozen and 0.025 converged, on n = 8-14 alone), leaving their n = 50 estimate unsupported; at n = 16 they report more than we reach at any budget measured. One optimizer beats ours: L-BFGS-B ends 3.9 +/- 1.6% above converged Adam at n = 16, on three instances. That margin retires our hardness conjecture under its registered rule and leaves the rate untouched: every optimizer measured loses a factor 1.3 per qubit. The barren plateau is present and cannot explain that rate: the reach sits far above the Haar floor 2^-n, and the exact second-order amplitude data are depth-independent while the reach is not. Nor do solutions cluster at that floor: they are decorrelated yet path-connected by paths 10^2-10^3 above 2^-n whose floor falls from 0.73 to 0.23 of the endpoints. Path search is one-sided, so near-optimal clustering stays open. In the deep limit we prove no poly(n)-parameter family beats poly(n) 2^-n on average. What survives: a connected landscape and a shrinking reach.



## Related
- [[conditional-dependence-and-scrooge-ensembles-in-shallow-rand|Conditional dependence and Scrooge ensembles in shallow random quantum circuits]]
- [[hardness-and-complexity-transition-of-noisy-random-circuit-s|Hardness and Complexity Transition of Noisy Random Circuit Sampling]]
- [[unconditional-quantum-advantage-for-sampling-with-shallow-ci|Unconditional Quantum Advantage for Sampling with Shallow Circuits]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.11890) | 2026-08-13
