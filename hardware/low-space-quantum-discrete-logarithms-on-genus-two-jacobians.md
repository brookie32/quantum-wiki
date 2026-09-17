---
title: "Low-Space Quantum Discrete Logarithms on Genus-Two Jacobians"
date: "2026-09-16"
updated: "2026-09-17"
source: "agent"
category: "hardware"
tags: [hardware, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2057"
summary: "Generic divisor-addition formulas use little arithmetic workspace but fail on exceptional inputs. We prove a randomized reduction that makes such formulas usable in quantum phase computation. Over any"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Generic divisor-addition formulas use little arithmetic workspace but fail on exceptional inputs. We prove a randomized reduction that makes such formulas usable in quantum phase computation. Over any finite abelian group of odd order, two independent public group seeds make each child pair in a complete balanced addition tree independent and uniform for every fixed input. A bound on the density of exceptional pairs then controls both the total failure probability and the error of the randomized quantum channel. We apply the reduction to an odd prime-order subgroup of size r in a genus-two Jacobian over mathbb F_q, where q is an odd prime and the model is a monic quintic with zero quartic coefficient. An integer lift of weighted Mumford arithmetic, a phase-only terminal polynomial, and an independent shifted Legendre symbol give useful-sample probability 1-O(L/q) on the exact domain mathbb Z_r^2 when r=Theta(q^2), where L is the number of tree leaves; this bound assumes exact preparation and Fourier readout. Explicit height certificates, streaming CRT reconstruction, and clean modular primitives yield a sampler using 10n+o(n) logical qubits, including both scalar registers, for n=lceillog_2qrceil. The model permits intermediate measurements, reset, and classical feedforward. For the Gaudry--Schost instance over mathbb F_{2^{127}-1}, a 16-bit window gives an analytic allocation of 1{,}923 qubits, 37.2% below the matched 3{,}063-qubit Chen-derived allocation. Its capped-run bound is below 2^{60} Toffoli gates, with rotation synthesis charged separately. A 32-bit window reduces the allocation to 1{,}618 qubits at substantially greater table and gate cost. The construction therefore provides an explicit space--time tradeoff.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2057) | 2026-09-16
