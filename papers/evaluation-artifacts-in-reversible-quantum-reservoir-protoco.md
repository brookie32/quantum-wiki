---
title: "Evaluation artifacts in reversible quantum reservoir protocols: a withdrawal of our own claims, and an entangled channel that survives the controls"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.12303"
summary: "arXiv:2603.12303v2 Announce Type: replace Abstract: This replaces v1 of this manuscript, which reported that a quantum reservoir autoencoder on reset-noise channels suppresses shot-noise sensitivity b"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2603.12303v2 Announce Type: replace Abstract: This replaces v1 of this manuscript, which reported that a quantum reservoir autoencoder on reset-noise channels suppresses shot-noise sensitivity by ten orders of magnitude and that a two-phase protocol reconstructs unseen inputs at MSE ~ 10^-4. We withdraw both claims. Under one consistent evaluation the suppression reverses sign: reset channels degrade the reconstruction 144x, the apparent gain being an in-sample number compared with an out-of-sample one. The two-phase target is an element-wise map with a public key, invertible in closed form without training at MSE = 7.4x10^-16, and a polynomial using no quantum features matches or beats the full model in all 14 conditions. We trace these to four evaluation artifacts; the fourth also affects the companion work relied on here, whose latent code never leaves its input-independent initialization, so substituting a constant changes nothing. We then report a construction passing the same controls: an entangled channel between two reservoir halves, injected on one side and read out on the other, decoded by a readout calibrated once and applied to unseen messages. Over 32 realizations the held-out error is below chance in 31-32 (permutation p<10^-4) while a shuffled control stays at chance, and non-Clifford resources prove necessary. A decoder-free response-Gram spectrum exposes an access threshold invisible to the decode error, though not a universal one: its median spans f^*=0.20-0.50, growing with the number of multiplexed components. Linear visibility is necessary yet insufficient, diverging from decodability at finite input amplitude-itself a design variable worth an order of magnitude. A variational ansatz trained to convergence on the same task is beaten by the fixed untrained circuit by 2.6-3.6x. We close with the controls, seed convergence and untrained baselines included, separating transport from interpolation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.12303) | 2026-08-14
