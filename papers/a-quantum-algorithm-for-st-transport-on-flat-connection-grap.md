---
title: "A Quantum Algorithm for st-Transport on Flat Connection Graphs"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40231"
summary: "arXiv:2609.40231v1 Announce Type: new Abstract: We study a generalization of undirected st-connectivity to graphs whose edges carry quantum operations. Let G=(V,E) be an undirected graph on n vertices"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40231v1 Announce Type: new Abstract: We study a generalization of undirected st-connectivity to graphs whose edges carry quantum operations. Let G=(V,E) be an undirected graph on n vertices in which each edge {u,v} is labeled by a unitary U_{uv}inC^{kimes k}, with U_{vu}=U_{uv}^agger. We assume the labels form a flat connection: the ordered product of labels along any path between a pair of vertices u and v is independent of the path. Equivalently, the connection is pure gauge, i.e., gauge-equivalent to the trivial connection; such graphs are exactly the consistent connection graphs of spectral graph theory and the noiseless instances of group synchronization. Consequently, whenever s and t are connected, transporting a state from s to t defines a unique unitary U_s(t). Given states |psi_srangle,|psi_trangleinC^k and an oracle that returns the neighbours of a vertex while coherently applying the corresponding edge unitaries, the st-transport problem is to decide whether s and t are connected and, if so, to estimate the squared overlap between U_s(t)|psi_srangle and |psi_trangle to additive error arepsilon. When k=1 and all labels are trivial, this is exactly undirected st-connectivity. We give a bounded-error quantum algorithm for st-transport that runs in time widetilde{O}(n/arepsilon) and uses O(log n+log k+log(1/arepsilon)) space. We do this by designing a transducer and applying a Metropolis-Hastings reweighting to the input graph. We also prove an Omega(n) quantum query lower bound that holds even when s and t are promised to be connected, so for constant arepsilon our algorithm is optimal up to polylogarithmic factors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40231) | 2026-10-01
