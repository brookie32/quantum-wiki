---
title: "Magic Secret Sharing: Threshold Control of Quantum Computational Power via GHZ Entanglement"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.16614"
summary: "arXiv:2605.16614v2 Announce Type: replace Abstract: We introduce Magic Secret Sharing (MSS), a quantum cryptographic primitive in which the secret is the computational capability of a quantum state ra"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2605.16614v2 Announce Type: replace Abstract: We introduce Magic Secret Sharing (MSS), a quantum cryptographic primitive in which the secret is the computational capability of a quantum state rather than its classical description. In the resource theory of magic, non-stabilizer states fuel universal quantum computation via non-Clifford gates; MSS distributes this resource with an (n-1,n) threshold structure using a pre-shared GHZ state and a single local phase gate P(phi) = diag(1, exp(i*phi)). Any individual party holds the maximally mixed state I/2, with Wigner distance C(I/2) = 0, so no local operation can yield non-Clifford computational advantage regardless of what operations are applied or what noise acts on the device. The authorised coalition reconstructs magic content C(phi) = (|sin(phi)| + |cos(phi)| - 1)/2 exactly, enabling a logical T gate via gate teleportation in multi-server blind quantum computation (BQC). Among diagonal parametric gates, phase gates are the unique class satisfying the security condition, characterised via an exact column-sum condition. The protocol is elevated to a one-sided device-independent (1SDI) setting via a steering inequality: the assemblage produced on the recipient's side certifies magic delivery without trusting the coalition's devices. We demonstrate the (2,3) instance on ibm_marrakesh (156-qubit IBM Heron): security (C(rho_Bob) < 10^-6, the linear-programming solver tolerance) holds in every run and is independently reproduced on a second qubit assignment, and state fidelity reaches 0.959-0.973 for the authorised party, with faithfulness confirmed for all four test values of phi to within 0.025 in magic content, a residual that depolarising noise alone accounts for.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.16614) | 2026-08-04
