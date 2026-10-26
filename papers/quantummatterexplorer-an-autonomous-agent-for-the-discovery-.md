---
title: "QuantumMatterExplorer: An Autonomous Agent for the Discovery of Quantum Many-Body Phases of Matter"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.32001"
summary: "arXiv:2610.32001v1 Announce Type: new Abstract: Mapping the phase diagram of a new quantum Hamiltonian demands expert judgement at every step: which observables to measure, where in parameter space to"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2610.32001v1 Announce Type: new Abstract: Mapping the phase diagram of a new quantum Hamiltonian demands expert judgement at every step: which observables to measure, where in parameter space to compute, or how to separate genuine order from finite-size artefacts. We introduce QuantumMatterExplorer, an autonomous agent that takes only a Hamiltonian and its parameter ranges as input and returns a phase diagram obtained from its own numerical simulations. The agent is built on a large language model and is designed to reason over a long horizon, maintain a persistent written plan, and drive a set of computational tools, with density-matrix renormalization group (DMRG) calculations cross-checked against independent exact diagonalization. The agent combines a large language model with persistent planning, a library of expert computational-physics skills, and density-matrix renormalization group calculations validated against independent exact diagonalization. It adaptively selects quantities to evaluate, refines parameter scans, and performs finite-size analyses as evidence accumulates. After validating the approach on Hamiltonians with known transitions, we challenge it with a frustrated bilinear-biquadratic spin-1 chain with single-ion anisotropy, whose two-dimensional phase diagram was published only recently and is unlikely to appear in any training corpus. Given no hint about the expected physics, the agent proposes which observables to probe, and identifies candidate Neel, Haldane and dimerized phases, in broad agreement with the reference phase diagram. It also detects incommensurate correlations and infers the frustration-dependent geometry of the phase boundaries, all within an eight-hour compute budget. These results open a practical route to the autonomous computational discovery of new phases of quantum matter.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.32001) | 2026-10-26
