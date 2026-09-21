---
title: "Shock-Capturing Quantum Algorithm for the Linear Advection Operator"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.21153"
summary: "arXiv:2609.21153v1 Announce Type: new Abstract: The linear advection operator is an ubiquitous building block in fluid and plasma problems. We develop a quantum algorithm for enacting the operator. Wh"
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2609.21153v1 Announce Type: new Abstract: The linear advection operator is an ubiquitous building block in fluid and plasma problems. We develop a quantum algorithm for enacting the operator. When the advection velocity is constant in space, our algorithm is exponentially more efficient per time step than classical and avoids spurious oscillations near steep gradients. The algorithm is most cleanly illustrated using the one-dimensional advection equation on a uniform spatial grid with periodic boundary conditions, which can be extended to higher dimensions. The algorithm uses a first-order upwind scheme, which captures discontinuities in the wave envelope but is not unitary. We embed the non-unitary upwind scheme using Linear Combinations of Unitaries (LCUs), and develop an efficient quantum gate decomposition of the upwind unitary, which performs one step of advection using O(n^2) two-qubit gates, where N=2^n is the number of spatial grid points, as opposed to a classical computer which costs O(N). Although LCUs introduces a small bounded probability of failure per time step, we show that the accumulation of failures does not lead to exponential-in-time complexity as one would naively expect. Moreover, when LCUs fails, we develop a probabilistic scheme to recover from the failure state, which avoids a full restart of the simulation. The failure recovery scheme uses quantum Fourier transform (QFT) and effectively achieves quantum indefinite integration of an unknown quantum state. The recovery, which can itself fail, is more efficient than a full restart if the wave envelop is well-resolved to include only low Fourier modes. We emulate our scheme classically and demonstrate small problems on Quantinuum's trapped-ion qubits. Our quantum algorithm provides a subroutine for physics simulations that involve linear advection.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.21153) | 2026-09-21
