---
title: "Fermion lattices can be simulated by same-size qubit lattices with O(1) interaction overhead"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.12600"
summary: "arXiv:2605.12600v2 Announce Type: replace Abstract: Local interactions among electrons underlie many complex properties of correlated materials. While the Jordan-Wigner transformation can preserve thi"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2605.12600v2 Announce Type: replace Abstract: Local interactions among electrons underlie many complex properties of correlated materials. While the Jordan-Wigner transformation can preserve this locality along one spatial dimension, interactions along the remaining dimensions typically incur substantial overhead. We show how to simulate all geometrically local interactions on an N-site two-dimensional fermion lattice with no asymptotic overhead in the number of interactions and no space overhead. The primary overhead of our method is circuit depth, which on a qubit lattice matches that of fermionic swap networks, scaling as O(sqrt{N}), but reduces to O(log N) on reconfigurable qubit arrays and to O(1) in lattice-surgery-based surface-code architectures. This is enabled by dynamically reorienting the Jordan-Wigner transformation to switch the lattice dimension along which locality is preserved. Furthermore, we study fermion routing, as required for the simulation of non-local interactions. When using qubit lattices, we reach resource scaling that asymptotically matches that of qubit routing, whilst on fully connected qubit devices, a depth scaling arbitrarily close to O(log N) is reached. This allows the fermionic fast Fourier transform to be implemented on qubit lattices with asymptotically optimal resource scaling under these locality constraints. Notably, all of our constructions naturally extend to d-dimensional lattices. Beyond scaling improvements, we show explicit examples of our method, including Fermi-Hubbard-model simulations of the square-, Lieb- and kagome lattice and the fermionic fast Fourier transform.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.12600) | 2026-09-28
