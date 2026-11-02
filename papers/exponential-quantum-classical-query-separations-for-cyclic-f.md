---
title: "Exponential quantum-classical query separations for cyclic Forrelation"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41694"
summary: "arXiv:2610.41694v1 Announce Type: new Abstract: We study the randomized classical query complexity of cyclic Forrelation, a cyclic analogue of k-Forrelation [AA15, STOC'15; BS21, STOC'21]. Given k Boo"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41694v1 Announce Type: new Abstract: We study the randomized classical query complexity of cyclic Forrelation, a cyclic analogue of k-Forrelation [AA15, STOC'15; BS21, STOC'21]. Given k Boolean functions f_1,ldots,f_k:F_2^no{-1,1}, the goal is to estimate T_k=N^{-1}operatorname{Tr}(D_{f_1}H^{otimes n}dots D_{f_k}H^{otimes n}), where D_{f_i}=operatorname{diag}(f_i(x):xinF_2^n), H is the Hadamard gate, and N=2^n. This normalized-trace problem can be solved with k quantum queries in the DQC1 model. Its classical query complexity was left open in [JLS+26, FOCS'26], which conjectured a lower bound of widetilde{Omega}(N^{1-2/k}). We establish a nearly complete characterization of the nonadaptive classical query complexity of cyclic Forrelation. For even kge 4, we prove a tight bound of Theta_k(N^{1-2/k}) for constant additive error. For odd kge 5, we obtain a lower bound of Omega_k(N^{1-2/(k-1)}) and an upper bound of O_k(N^{1-2/k}). Surprisingly, k=3 admits a polylogarithmic-query nonadaptive classical algorithm, disproving the conjecture in this case. These results suggest an unexpected parity-dependent structure: the nonadaptive complexity may be governed by the independence number of the k-cycle, leading to the exponent 1-1/lfloor k/2rfloor, rather than the previously conjectured 1-2/k, which was motivated by a Fourier-growth heuristic. Finally, allowing adaptivity, we prove a lower bound of Omega(N^{1/4}) for every kge4. Although formally close to k-Forrelation, the cyclic structure leads to rather different classical behavior and requires different techniques. Our lower bounds are based on hidden-shift collision constructions, and our upper bounds follow from randomized sampling together with cycle-specific conditional-moment estimates. Our results provide a systematic understanding of its query advantages over classical computation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41694) | 2026-11-02
