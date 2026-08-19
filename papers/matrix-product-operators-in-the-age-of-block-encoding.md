---
title: "Matrix Product Operators In The Age of Block Encoding"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.19083"
summary: "arXiv:2606.19083v2 Announce Type: replace Abstract: We develop a block-encoding compiler that treats matrix product operators as compressed, virtual-path linear combination of unitaries programs. The "
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2606.19083v2 Announce Type: replace Abstract: We develop a block-encoding compiler that treats matrix product operators as compressed, virtual-path linear combination of unitaries programs. The compiler constructs conditional exttt{PREP} and local exttt{SELECT} stages directly from a parent matrix product operator, establishing tensor networks as structured quantum intermediate representations that can be efficiently compiled to block-encoded circuits. We apply the construction to real-time evolution in the Heisenberg chain and two perturbed Heisenberg-family models. Across the regimes studied, the compressed, approximately unitary propagator MPOs retain mild bond dimension and LCU normalization. Relative to an LCU that explicitly lists the (O(N^K)) Pauli-product branches of an order-(K) truncated Taylor polynomial, our virtual-transition implementation replaces combinatorial branch enumeration by a circuit complexity scaling as (O(alpha_{rm MPO}Nhi^2)), approaching (O(Nhi^2)) when (alpha_{rm MPO}) remains mild. We numerically characterize how truncation order, bond-dimension budget, and system size affect approximation error, normalization, and compiler cost. These results demonstrate how classically compressed tensor-network representations can serve as quantum compiler intermediate representations for block encoding and opens new avenues to accelerate quantum algorithms.



## Related
- [[matrix-product-operator-dualities-in-integrable-lattice-mode|Matrix-product operator dualities in integrable lattice models]]
- [[exact-and-efficient-circuit-construction-for-block-encoding-|Exact and Efficient Circuit Construction for Block Encoding Matrix Polynomials]]
- [[symmetry-enriched-topological-order-in-tensor-networks-defec|Symmetry-enriched topological order in tensor networks: Defects, gauging and anyon condensation]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.19083) | 2026-08-03
