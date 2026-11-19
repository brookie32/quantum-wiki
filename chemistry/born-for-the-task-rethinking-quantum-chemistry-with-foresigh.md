---
title: "Born for the Task: Rethinking Quantum Chemistry with Foresighted Agentic Computing"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.22897"
summary: "arXiv:2611.22897v2 Announce Type: replace-cross Abstract: Quantum chemistry relies on general-purpose software, whose generality leaves many large-scale calculations beyond practical resource budgets."
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.22897v2 Announce Type: replace-cross Abstract: Quantum chemistry relies on general-purpose software, whose generality leaves many large-scale calculations beyond practical resource budgets. Coding agents make task-specific programs cheap to write, but not efficient ones easy to find: whether a computational strategy is accurate and fast enough becomes clear only after it actually runs at the target scale. We introduce MakoBORN, a foresighted agentic computing framework that synthesizes high performance quantum chemistry programs on demand. MakoBORN anticipates the behavior of each strategy before execution, extrapolating its error from representative small systems and predicting its runtime from the target-scale workload and measured hardware throughputs. Building on these predictions, MakoBORN unfolds the preset schemes of existing packages into independently configurable algorithmic components, selects the fastest strategy within the error tolerance from the predicted accuracy-runtime Pareto frontier, and guides coding agents to compile it with component-level performance predictions. For a Hartree-Fock calculation with 50,024 basis functions, MakoBORN finishes in 1.41 h on a single CPU node, 77imes faster than the estimated runtime of a general-purpose baseline and still 9.8imes faster with development time included. On a single GPU, MakoBORN completes the ubiquitin calculation in 2.1 h, the same order of runtime as the GPU-accelerated package Mako on 64 GPUs, and shortens the B-DNA duplex calculation from an estimated two months to 8.1 h (173imes).

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.22897) | 2026-11-19
