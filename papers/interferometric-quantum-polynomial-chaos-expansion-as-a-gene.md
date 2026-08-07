---
title: "Interferometric Quantum Polynomial Chaos Expansion as a Generative Model for Calorimeter Shower Simulation"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.05405"
summary: "arXiv:2608.05405v1 Announce Type: new Abstract: We present the quantum polynomial chaos expansion, a generative algorithm in which a single circuit is the entire model, and we use it to learn calorime"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05405v1 Announce Type: new Abstract: We present the quantum polynomial chaos expansion, a generative algorithm in which a single circuit is the entire model, and we use it to learn calorimeter images. In a classical chaos expansion the randomness is the input and the coefficients are fitted. Here the randomness is still the only input, entering the circuit as rotation angles and re-uploaded at every block, so that each measured observable is a chaos expansion of the latent variables whose order equals the circuit depth, and what is fitted are the gate angles themselves. Expressivity therefore grows with depth rather than with classical coefficients, correlations between outputs arise only from entangling gates, and a single latent wire read by all qubits carries the collective mode of the data. Nothing fitted stands between the circuit and the sample, so switching the entanglers off is a setting of the model itself and provably yields independent outputs, and attribution of the learned correlations to individual gates becomes a measurement. Choosing between two measurement bases shot by shot sharpens attribution into certification, and the trained model violates the Bell bound obeyed by every classical generative model with local response, whatever its size. We train the model on Geant4 shower data, execute the identical circuit on a superconducting processor with its accuracy loss predicted in advance, prove a no-go theorem for the tail dependence of every smooth generator read out through expectation values, and identify the circuit primitive that removes this limit.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.05405) | 2026-08-07
