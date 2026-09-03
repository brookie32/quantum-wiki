---
title: "DMRG using Belief Propagation"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.02361"
summary: "arXiv:2609.02361v1 Announce Type: new Abstract: Tensor networks have attracted much attention as a powerful tool for modeling quantum many-body systems. Their contraction is a significant challenge, h"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02361v1 Announce Type: new Abstract: Tensor networks have attracted much attention as a powerful tool for modeling quantum many-body systems. Their contraction is a significant challenge, however, especially in highly connected networks, as memory requirements become prohibitive and the optimal contraction order is increasingly hard to find. The belief propagation (BP) algorithm has emerged as an alternative to exact contraction. Being formulated in a graph-agnostic way, it offers great flexibility, but its accuracy suffers in the presence of loops. In this work, we combine BP with the DMRG algorithm to solve ground-state problems, thereby extending DMRG to higher dimensions and arbitrary lattices. We demonstrate the viability of BP-DMRG on the transverse-field Ising model on a 2imes 2 hexagonal lattice, finding that it produces states with a fidelity between 0.9 and 0.99 to the true ground state, and energy estimates with a relative error between 10^{-2} and 10^{-3}. Additionally, BP-DMRG can find ground states on randomly generated lattices, with fidelity improving as the transverse field increases. We conclude with a discussion of the limitations we encounter when using belief propagation, highlighting that the TFI tensor network operators lead to larger errors during BP iterations in BP-DMRG.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.02361) | 2026-09-03
