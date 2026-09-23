---
title: "Pauli propagation enables fast classical simulation of strongly correlated quantum systems"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.21651"
summary: "arXiv:2511.21651v3 Announce Type: replace Abstract: Ground state energy estimation for strongly correlated quantum systems remains a central challenge in computational physics and chemistry. While ten"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2511.21651v3 Announce Type: replace Abstract: Ground state energy estimation for strongly correlated quantum systems remains a central challenge in computational physics and chemistry. While tensor network methods like DMRG provide efficient solutions for one-dimensional systems, higher-dimensional problems remain difficult. Here we present a variational double bracket flow (vDBF) algorithm that leverages Pauli Propagation, a technique originally developed for classical simulation of quantum circuits, to efficiently approximate ground state energies. By combining greedy operator selection with coefficient-based fluctuation truncation and energy-variance extrapolation, we obtain sub-1% relative errors for Heisenberg and Hubbard lattices of up to 128 qubits. For a 10imes10 Heisenberg lattice (100 qubits), vDBF obtains accurate results in approximately 2 minutes on a single CPU thread, compared to over 50 hours on 64 threads for DMRG. Accurate results are also obtained for systems that are difficult for quantum Monte Carlo: on the maximally frustrated 8imes8 J_1-J_2 lattice and the hole-doped 8imes8 Hubbard model, the tightest thresholds extrapolate to within a few tenths of a percent of the best published variational estimates. We further test vDBF on the 84-qubit pi-valence active space of hexabenzocoronene, where the most reliable extrapolated correlation energies agree with DMRG to within 1%. These results demonstrate that classical simulation techniques developed in the context of quantum advantage benchmarking can provide practical tools for many-body physics.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.21651) | 2026-09-23
