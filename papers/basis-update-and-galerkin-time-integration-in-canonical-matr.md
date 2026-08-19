---
title: "Basis-update and Galerkin time integration in canonical matrix-product-state form"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16994"
summary: "arXiv:2608.16994v1 Announce Type: new Abstract: Matrix product state algorithms must enlarge their bond spaces as entanglement grows and compress them to control cost. We formulate basis-update and Ga"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.16994v1 Announce Type: new Abstract: Matrix product state algorithms must enlarge their bond spaces as entanglement grows and compress them to control cost. We formulate basis-update and Galerkin (BUG) time integration as a sequence of canonical MPS sweeps for Hamiltonians represented as matrix product operators. We show when two natural basis updates produce the same trial space and when transporting coefficients between successive bases preserves the represented state. Under these conditions, the existing first-order error bound for uncompressed tree-tensor-network BUG also applies to the alternating-endpoint MPS schedule. We verify the uncompressed implementation against an independent six-site calculation. We then compare BUG with two-site TDVP for 16-site transverse-field Ising and Haldane-Shastry dynamics. At matched timestep and truncation settings, BUG performs fewer local exponential actions and has lower runtime. These settings do not produce equal accuracy. The runtime versus accuracy curves cross for the Ising model and are close for the Haldane-Shastry model. The comparison therefore identifies model-dependent trade-offs rather than a general advantage for either method.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16994) | 2026-08-19
