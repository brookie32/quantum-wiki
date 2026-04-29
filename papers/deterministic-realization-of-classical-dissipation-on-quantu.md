---
title: "Deterministic Realization of Classical Dissipation on Quantum Computers"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25429"
summary: "arXiv:2604.25429v1 Announce Type: cross Abstract: Lattice Boltzmann (LB) on quantum devices must reconcile unitary gate evolution with the dissipative collision step. In the multiple-relaxation-time ("
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25429v1 Announce Type: cross Abstract: Lattice Boltzmann (LB) on quantum devices must reconcile unitary gate evolution with the dissipative collision step. In the multiple-relaxation-time (MRT) class, we work in the common setting of modewise diagonal moment relaxation, elta m_r'=lambda_r,elta m_r with lambda_rin[-1,1] (overrelaxation if lambda_r<0). Embedding that contraction in a unitary by block encoding or a linear combination of unitaries (LCU) typically yields subunitary success probability that decays multiplicatively across modes, sites, and time, a key bottleneck for quantum LB. For the dissipative MRT block alone we give a block-encoding-free construction: a signed two-rail population encoding, then a completely positive trace-preserving (CPTP) map (per-rail amplitude damping with survival |lambda_r| and, if lambda_r<0, a rail SWAP) so that, after the decode, the map agrees with classical MRT relaxation exactly (expectations of the rail number operators, common encoding--decode scale). Trace preservation gives success probability 1 for that substage. The main result is the dissipative MRT block; construction of the equilibrium moment vector~m^{eq}=Mf^{eq} (prescribed~f^{eq}, host moment matrix~M; notation as in Section~ref{subsec:generic-mrt}), moment transforms, streaming, and boundaries are composed with it as in a standard host pipeline and lie outside the scope of the formal theorem. Hybrid and fully coherent encodings, adaptive scales, Carleman-based context, and a one-rail no-go in the same nonnegative population framework are in the main text. Audits of the open-channel map on a long LBM collide-stream simulation and on stencil-free inputs both match the target to machine precision.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25429) | 2026-04-29
