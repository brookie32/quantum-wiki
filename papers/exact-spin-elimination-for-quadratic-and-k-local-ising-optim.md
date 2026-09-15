---
title: "Exact Spin Elimination for Quadratic and k-Local Ising Optimization"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2505.07163"
summary: "arXiv:2505.07163v2 Announce Type: replace Abstract: Ising solvers have a finite spin budget. Quadratization uses auxiliary spins to replace higher-order interactions by pairwise ones. We show that rem"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2505.07163v2 Announce Type: replace Abstract: Ising solvers have a finite spin budget. Quadratization uses auxiliary spins to replace higher-order interactions by pairwise ones. We show that removing spins while allowing more complex interactions can fit larger problems within the same spin budget and improve optimization. Walsh elimination minimizes over one spin at a time, writes the resulting interaction as a sum of spin products in the Walsh basis, and stores a rule for recovering the removed spin. Explicit resource limits control which eliminations are accepted. In a held-out test with the protocol frozen before instance generation and one annealing schedule shared by both formulations, mean observed success rises from 10.4% to 97.5% on sparse quadratic spin glasses and from 16.9% to 87.5% on three-body problems. Observed success increases on every instance with a verified reference minimum, and pooled time-to-solution estimates decrease by factors of about 34 and 11, respectively, with preprocessing included. For zero-field pairwise models on connected simple cubic graphs with more than four vertices, we prove that a fixed spin budget accommodates 50% larger inputs while retaining pairwise interactions, zero fields, residual degree at most six, and no increase in coupling count. These results establish exact spin elimination as a controlled trade between active-spin capacity and interaction complexity.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2505.07163) | 2026-09-15
