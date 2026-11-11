---
title: "Autonomous Optimization of Numerical Algorithms by an AI Agent: Application to Atomistic Simulation"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.13143"
summary: "arXiv:2611.13143v1 Announce Type: new Abstract: Coding agents built on large language models, run in automated improvement loops, can discover more efficient algorithms. We present AIOA, a framework t"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13143v1 Announce Type: new Abstract: Coding agents built on large language models, run in automated improvement loops, can discover more efficient algorithms. We present AIOA, a framework that brings this approach to the numerical algorithms of atomistic simulation: an agent improves an algorithm against a pre-specified metric in a loop guarded by verifiers it cannot alter. Applied to ASE, a widely used atomistic simulation library, AIOA targets two facets of an algorithm: its implementation, rewritten to run faster with unchanged results, and the method itself, redesigned to converge with fewer force evaluations. Agents made six kernels 22-24 times faster on average in Python with NumPy and SciPy. On unseen problems, optimizers from the best configuration needed 3.1-3.4 times fewer force evaluations than L-BFGS for structure relaxation and 4.6-17 times fewer than standard climbing-image nudged elastic band calculations for reaction paths. The agents' optimizers also contain two algorithmic components we did not find in the literature.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.13143) | 2026-11-11
