---
title: "Quantum Topological Data Analysis Beyond Betti Numbers: Complexity Hardness & An Algorithm for Torsion Witness"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.28112"
summary: "arXiv:2609.28112v1 Announce Type: new Abstract: Recent advances have revealed an interplay between quantum computing and topological data analysis (TDA). Most quantum TDA has focused on Betti numbers,"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.28112v1 Announce Type: new Abstract: Recent advances have revealed an interplay between quantum computing and topological data analysis (TDA). Most quantum TDA has focused on Betti numbers, which characterize the connectivity and ``holes'' of a dataset. Homology, however, contains additional information in the form of torsion: a nontrivial cycle can become trivial after being repeated finitely, revealing global constraints on how cycles combine and wrap around one another. Beyond applications in biomolecular studies, torsion appears in physical settings including homological quantum rotor codes, discrete charges, and gauge sectors. We study torsion from both classical and quantum perspectives. Given a graph G and its clique complex K = Cl(G), we first prove that, for fixed r and prime p, deciding whether H_r(K,Z) contains p-torsion is NP-hard. As a corollary, when a homological rotor code is specified by G, deciding whether the code has a finite-dimensional logical sector of a given order is NP-hard. We discuss related problems, including the Bockstein homomorphism, Smith normal form, lattice saturation, and cohomology. Second, for a finite set of primes P, we develop a quantum algorithm that serves as a one-sided torsion witness. For fixed r, it outputs WITNESS or INCONCLUSIVE, i.e. WITNESS certifies that either H_r(K,Z) or H_{r-1}(K,Z) contains p-torsion for some pin P while INCONCLUSIVE makes no claim about its presence or absence. We identify a regime in which the algorithm achieves a near-quadratic quantum speedup over the corresponding classical algorithm under the same input model. Our NP-hardness result complements recent hardness results for estimating Betti numbers, adding a complexity-theoretic perspective to quantum TDA. Together, these results demonstrate that integral homology, beyond its Betti numbers, can be computationally challenging.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.28112) | 2026-09-24
