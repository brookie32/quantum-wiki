---
title: "Proven optimality for LABS with quantum-classical branch and bound"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.22688"
summary: "arXiv:2611.22688v2 Announce Type: replace Abstract: Low autocorrelation binary sequences (LABS) are the phase codes of pulse compression radar and the synchronization words of digital communication, a"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2611.22688v2 Announce Type: replace Abstract: Low autocorrelation binary sequences (LABS) are the phase codes of pulse compression radar and the synchronization words of digital communication, and finding the sequence of a given length whose aperiodic autocorrelations have the smallest sum of squares is a hard binary optimization problem. The quantum optimization methods tested on LABS so far return good sequences, but they cannot show that a sequence is optimal or bound how far from optimal it may be. We show that a quantum optimization algorithm can deliver proven optimality. In our quantum-classical branch and bound, fixed-angle QAOA samples the Hamiltonians of the nodes of the search tree, its samples supply candidate sequences and the branching choice, and classical bounds prune the tree, so that the algorithm returns either a proof of optimality or, if it is stopped early, the best sequence found with a certified lower bound and gap. It works on the native quartic Hamiltonian without penalty terms, and its correctness does not depend on the sampler. With QAOA at depth p= 12 and at p= 1 and 1,000 shots per node, it proved the optima of all lengths from 2 to 30, where from length 27 on the root node is split without being sampled. Every run records both bounds against time, and its primal-dual integral measures its convergence. We claim no speedup.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.22688) | 2026-11-20
