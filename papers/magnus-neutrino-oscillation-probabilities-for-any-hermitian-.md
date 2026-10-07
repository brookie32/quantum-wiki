---
title: "Magnus: neutrino oscillation probabilities for any Hermitian Hamiltonian, any number of flavors, and any matter profile"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.07159"
summary: "arXiv:2610.07159v1 Announce Type: cross Abstract: Interpreting neutrino oscillation measurements requires computing the probability that a neutrino born with one flavor is detected with another. In va"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.07159v1 Announce Type: cross Abstract: Interpreting neutrino oscillation measurements requires computing the probability that a neutrino born with one flavor is detected with another. In vacuum and in matter of constant density, this probability has exact formulas. Where the density varies along the path, as in the Earth, the Sun, or a supernova, it does not. There, the usual approaches either replace the profile by constant-density steps, whose error falls only as the square of their width, or integrate the evolution equation with a general-purpose solver, which must shorten its steps to meet a tighter tolerance. Both become slow at high accuracy, yet an analysis needs the probability at many energies, directions, and parameter values. Each new experiment or model often requires writing and validating a new solver. We present Magnus, an open-source Python code that avoids these limitations. It uses the Magnus expansion, whose error falls as a high power of its step width and whose cost is set by how fast the density varies, not by how many oscillations the path holds. Magnus accepts any density profile, any number of flavors, and any Hermitian Hamiltonian, such as those of non-standard interactions, sterile neutrinos, Lorentz-invariance violation, and pseudo-Dirac neutrinos. Where a cheaper route exists, it takes it automatically. For example, where the density varies slowly, as in the Sun, it follows the instantaneous eigenstates and applies the expansion only at resonances. Besides oscillating probabilities, Magnus returns phase-averaged ones, which describe solar and astrophysical neutrinos. A typical probability takes a few milliseconds, and batched scans are one to two orders of magnitude cheaper per point. Among the public codes we compared, Magnus is the fastest at high accuracy on a varying profile. Magnus shifts the effort of studying a new experiment or model from writing a solver to specifying its physics.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.07159) | 2026-10-07
