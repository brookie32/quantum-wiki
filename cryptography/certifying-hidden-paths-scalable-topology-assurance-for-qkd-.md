---
title: "Certifying Hidden Paths: Scalable Topology Assurance for QKD Networks"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.11513"
summary: "arXiv:2610.11513v1 Announce Type: cross Abstract: Large-scale Quantum Key Distribution (QKD) networks rely on trusted repeaters, making the security properties of the selected communication path an es"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.11513v1 Announce Type: cross Abstract: Large-scale Quantum Key Distribution (QKD) networks rely on trusted repeaters, making the security properties of the selected communication path an essential part of end-to-end assurance. At the same time, network operators may be unwilling to disclose their internal topology. We present a topology-certification mechanism that lets a provider prove in zero knowledge that policy-compliant routes between two endpoints exist, without disclosing the routes in an individual presentation. Our main idea is to certify nodes and edges independently using multi-message signatures, rather than signing the complete graph as one object. For a route chosen in advance, proof size and cryptographic proving and verification work depend on its positions and attributes, independently of the overall network size, whereas route discovery and certification have separate graph-dependent costs. The construction hides the actual route length up to a public bound and sketches extensions to node-disjoint routes and monotonic additions within a graph epoch. We give a formal security model and conditional proofs of unforgeability and graph hiding for a generic construction. For a BBS-based construction, presentation-size estimates remain below 300,KiB at ell=m=n=50, and measured generation and verification times remain below 400,ms at ell=64 and m=n=8.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.11513) | 2026-10-09
