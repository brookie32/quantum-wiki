---
title: "Quantum simulation of real-time bosonic dynamics with binary and unary position encodings on superconducting and trapped-ion processors"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13079"
summary: "arXiv:2611.13079v1 Announce Type: new Abstract: Simulating a bosonic degree of freedom on qubit hardware requires discretizing its position space, and the qubit encoding of the resulting lattice deter"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13079v1 Announce Type: new Abstract: Simulating a bosonic degree of freedom on qubit hardware requires discretizing its position space, and the qubit encoding of the resulting lattice determines the circuits that realize its real-time dynamics. We compare binary and unary encodings of a position lattice on superconducting (IBM) and trapped-ion (IonQ) processors. Binary encoding applies the kinetic term through the quantum Fourier transform; unary encoding uses one qubit per site, single-qubit rotations for the potential and excitation-conserving exchange gates for the kinetic term. For a single degree of freedom the unary dynamics is a free-fermion problem, and its product formula compresses exactly into a nearest-neighbor circuit of fixed size. With about two hundred two-qubit gates, these circuits resolve tunneling in a symmetric double well on both processors, with the right-well probability falling from 0.97 to 0.06 on IBM and from 0.96 to 0.12 on IonQ, whereas binary product-formula circuits with several thousand two-qubit gates do not reproduce the transfer. Noiseless emulation indicates that this contrast reflects the compilation as well as the encoding: without the fixed-size optimization, a unary product formula that captures the transfer also requires several thousand two-qubit gates. Post-selection on the single-excitation subspace removes leakage, and because every energy eigenstate of the symmetric grid populates both wells equally, the measured population reversal bounds the coherence between energy eigenstates from below. Coupled-oscillator benchmarks, where inter-register interactions prevent this exact compression, show that the preferred encoding depends on the grid size and the evolution time.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13079) | 2026-11-11
