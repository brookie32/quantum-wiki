---
title: "Solving Sparse SDPs in Sublinear Time: A Classical Algorithm Inspired by the Quantum OR Lemma"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40302"
summary: "arXiv:2609.40302v1 Announce Type: new Abstract: We give the first sublinear-time classical solvers for sparse semidefinite programs in the bounded-radius regime, without low-rank assumptions or Froben"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40302v1 Announce Type: new Abstract: We give the first sublinear-time classical solvers for sparse semidefinite programs in the bounded-radius regime, without low-rank assumptions or Frobenius norm dependence on the constraint matrices. For constant precision and bounded primal and dual radii, prior quantum algorithms of Brandao et al. (2019) and van Apeldoorn and Gilyen (2019) achieved widetilde{O}(sqrt{n}+sqrt{m}) dependence on matrix dimension n and constraint number m. Compared with the widetilde{O}(mn) runtime of existing classical methods, this suggests a quartic quantum speedup when m approx n. Beyond a usual Grover speedup, this separation relies on the Quantum OR lemma, whose sample-reuse mechanism decouples the cost of Gibbs-state preparation from constraint search. We show that this reuse mechanism is classically realizable for sparse SDPs. Our main technical contribution is a classical procedure for simultaneously estimating many expectation values with respect to a sparse Hamiltonian's Gibbs state. This combines randomized Lanczos filtering with an efficient sampling-based estimator. We also introduce a stochastic online-learning framework for SDP solving, substantially improving accuracy-dependence over standard oracle-based MMWU approaches. Let s denote the the input matrix sparsity and gamma:=Rr/arepsilon capture dependence on the primal (R) and dual (r) radii as well as target accuracy (arepsilon). When gamma^2leqmin{m,n/s}, our solver runs in time widetilde{O}left(nsgamma^{4.5}+msgamma^2right). For gamma=O(1), this is widetilde{O}left((n+m)sright) and sublinear in the O(mns) input size. Similar to the quantum algorithms, this matches known lower bounds with respect to m and n, up to logarithmic factors. This implies that, with respect to dimensions m and n, there is no super-quadratic quantum advantage for generic sparse SDP solving.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40302) | 2026-10-01
