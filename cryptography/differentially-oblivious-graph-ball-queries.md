---
title: "Differentially Oblivious Graph Ball Queries"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2759"
summary: "A graph ball query returns all vertices within distance r of a source vertex. On N-vertex graphs with maximum degree at most Delta, ordinary breadth-first search answers such queries with O_{Delta,r}("
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

A graph ball query returns all vertices within distance r of a source vertex. On N-vertex graphs with maximum degree at most Delta, ordinary breadth-first search answers such queries with O_{Delta,r}(1) record accesses. These accesses depend on private edges and can reveal graph structure. Full obliviousness hides this dependence, but incurs substantial overhead. Differential obliviousness (DO) [Chan et al., SODA'2019] trades off between privacy and efficiency by relaxing full obliviousness to (arepsilon, elta)-differential privacy on the access traces of neighboring graphs. We study DO graph ball queries under three widely-adopted edge-level neighboring relations: add/delete, replacement, and 2-switch. Starting from padded adjacency records, we charge all observable accesses, including preprocessing. For fixed Delta,rge2, error probability 0<eta<1/2, and 0leeltale(1-2eta)/2, we prove an Omega_{Delta,r,eta}(1+Ne^{-arepsilon}) expected lower bound at every sufficiently large connected graph and every public source. For every fixed rge2, we give (arepsilon,0)-DO sampling algorithms with expected cost O_{Delta,r,eta}(1+Ne^{-arepsilon/C}) using constant size of hidden workspace, where C depends only on Delta,r and the neighboring relation. Especially, for r=2, we have C=1, which indicates that the algorithm achieves the tight bound under all three relations. Finally, we consider repeated queries on the same graph, where the cost of protected preprocessing can be amortized across queries. For fixed Delta,r,eta, we construct a linear-size reusable index with (arepsilon,0)-DO preprocessing and constant query cost. The expected preprocessing cost is linear in N when arepsilon exceeds a sufficiently large constant multiple of log N.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2759) | 2026-11-04
