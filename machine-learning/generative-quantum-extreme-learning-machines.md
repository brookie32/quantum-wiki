---
title: "Generative quantum extreme learning machines"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.37116"
summary: "arXiv:2610.37116v1 Announce Type: new Abstract: Training the circuit of a quantum generative model is hampered by barren plateaus, where gradients vanish exponentially with the number of qubits. In th"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.37116v1 Announce Type: new Abstract: Training the circuit of a quantum generative model is hampered by barren plateaus, where gradients vanish exponentially with the number of qubits. In the present work we propose a generative protocol based on the paradigm of quantum extreme learning machines, in which the circuit is never trained. A random latent vector is encoded into a quantum state, evolved with a fixed unitary and measured, and only a linear output layer is trained. The encoding of the latent variable determines the functions available to the model, while the unitary decides which combinations of them are seen by the trained layer. With the help of Pauli propagation we show that for a Clifford unitary each feature is a single product of sines and cosines of the encoded angles, so that a Clifford circuit, even a strongly entangling one, does not create new functions. Doping the circuit with T gates mixes these products and changes the nonstabilizerness of the state, but the space of functions remains the one fixed by the encoding. For brickworks of Haar-random two-qubit gates the features are no longer single products, and their variation with the latent variable decreases with the depth of the circuit. For the proposed encoding and for one- and two-dimensional distributions, generated both from expectation values and from single measurements, neither the entanglement produced by a Clifford reservoir nor the additional nonstabilizerness of Haar-random brickworks systematically improves the generator, and a reservoir with no gates at all is competitive with entangling circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.37116) | 2026-10-28
