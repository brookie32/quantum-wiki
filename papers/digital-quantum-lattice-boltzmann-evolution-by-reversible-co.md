---
title: "Digital quantum lattice Boltzmann evolution by reversible compute and open-system reset"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.13953"
summary: "arXiv:2609.13953v1 Announce Type: cross Abstract: Turbulent fluid simulation is computationally demanding because nonlinear interactions couple a wide range of scales. Quantum computing offers another"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.13953v1 Announce Type: cross Abstract: Turbulent fluid simulation is computationally demanding because nonlinear interactions couple a wide range of scales. Quantum computing offers another computational model, but fluid evolution is nonlinear and dissipative whereas closed gate-based dynamics is linear and reversible. The lattice Boltzmann method (LBM) is an attractive discrete target because streaming is a local permutation, yet conventional collision reconstructs a nonlinear equilibrium and applies dissipative relaxation. We present a digital quantum lattice Boltzmann (QLBM) algorithm that keeps that nonlinear timestep in computational-basis registers. Each step writes the updated populations into a clean destination bank, uncomputes the workspace, and resets the obsolete source. The resulting channel is completely positive and trace preserving (CPTP), composes without intermediate measurement, and applies to any lattice Boltzmann stencil that can be evaluated reversibly into a clean bank. Forced D3Q19 homogeneous isotropic turbulence, in direct numerical simulation (DNS) and Smagorinsky large-eddy simulation (LES) at Reynolds number 15000 over one million lattice steps, shows statistical agreement in mass, energy budgets, spectra, and intermittency. The three-dimensional calculations use a digital-register emulator of the circuit. A separate D2Q9 implementation compiles the same contract to reversible gates and agrees bit-exactly with its integer twin. Two-bank storage and serial lattice depth limit near-term feasibility.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.13953) | 2026-09-15
