---
title: "Warm-Start Quantum Computation for Energy Readout and State Preparation"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.12485"
summary: "arXiv:2610.12485v1 Announce Type: new Abstract: Estimating a ground-state energy and preparing a ground state both split into a front-end that supplies an approximate state |hirangle and a back-end th"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.12485v1 Announce Type: new Abstract: Estimating a ground-state energy and preparing a ground state both split into a front-end that supplies an approximate state |hirangle and a back-end that reads or refines it. We argue, and measure at every step, that the only thing crossing that split is the front-end's spectral weight distribution p_n=|langle E_n|hirangle|^2 over the eigenstates of the problem Hamiltonian H_P. Everything downstream is priced in it, so the front-end is a swappable module, and we swap it seven times without altering anything to its right. We call the arrangement WARP. Four back-ends spend that distribution. A readout (A) samples g(t)=langlehi|e^{-iH_Pt}|hirangle on the device and extracts true eigenvalues by classical signal processing, returning an energy below the variational bound of the state it was handed, from a signal 50imes shorter than a Fourier transform needs. Three routes spend the same account on a state instead. An adiabatic schedule (B) has a minimum gap set by the overlap; a discrete amplification (C) is cheaper in depth but must halt at an index the overlap fixes, so it needs a measured value and not a bound; a recursion (D) of depth O(3^m) raises the question of whether it can be run at all. The interactions are the substance. On stretched N_2 a sample-based diagonalisation reports a variational bound 79 mHa high, fifty times outside chemical accuracy; reading the state it has already prepared returns E_0 to 1.4imes10^{-6} Ha, three orders of magnitude inside it, and needs no new front-end and no new circuit. And because the weights price everything, they must be measurable when scarce, so we beat a weak reference against a strong one and recover overlaps four orders of magnitude below the shot-noise floor. We map the operating envelope throughout, and state the limitations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.12485) | 2026-10-12
