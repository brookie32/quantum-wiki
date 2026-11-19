---
title: "Optimal Joint Bounds for Sparse Ground-State Energy Estimation and Ground-State Preparation"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.23387"
summary: "arXiv:2611.23387v1 Announce Type: new Abstract: Ground-state energy estimation (GSEE) and ground-state preparation (GSP) are fundamental problems in quantum computing. Given a Hamiltonian H with |H|le"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23387v1 Announce Type: new Abstract: Ground-state energy estimation (GSEE) and ground-state preparation (GSP) are fundamental problems in quantum computing. Given a Hamiltonian H with |H|le1 and a guiding state |psirangle with overlap at least gamma>0 with the ground space of H, the goal in GSEE is to estimate the ground-state energy of H to additive error elta with failure probability at most arepsilon, while in GSP it is to prepare a state with ground-space weight at least 1-arepsilon, given a gap lower bound Delta. Their costs are measured by quantum query complexity, i.e., the number of oracle calls needed to access H. Recent work proved optimal bounds Theta(log(1/arepsilon)/(gammaelta)) for GSEE and Theta(log(1/arepsilon)/(gammaDelta)) for GSP in the time-evolution and block-encoding models. However, these models do not directly account for the sparsity of H, measured by the maximum number s of nonzero entries in any row or column. In the sparse-access model, oracles instead return the locations and values of these entries. This introduces the additional parameter s, and it remained open how query complexity depends jointly on s, gamma, elta or Delta, and arepsilon. We resolve this by proving sparse-query lower bounds Omega(sqrt{s}log(1/arepsilon)/(gammaelta)) for GSEE and Omega(sqrt{s}log(1/arepsilon)/(gammaDelta)) for GSP, even for stoquastic Hamiltonians. We also show that these constructions recover the earlier time-evolution and block-encoding lower-bound scalings. We then give matching upper-bound algorithms in the reversible in-place sparse-location model. Thus, we obtain Theta(sqrt{s}log(1/arepsilon)/(gammaelta)) for GSEE and Theta(sqrt{s}log(1/arepsilon)/(gammaDelta)) for GSP, showing that sqrt{s} is necessary and sufficient and completing the joint dependence on all problem parameters.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.23387) | 2026-11-19
