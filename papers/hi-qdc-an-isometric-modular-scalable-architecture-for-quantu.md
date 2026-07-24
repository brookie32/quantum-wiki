---
title: "HI-QDC: An Isometric Modular Scalable Architecture for Quantum Data Centers"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.20633"
summary: "arXiv:2607.20633v1 Announce Type: new Abstract: Server-centric quantum data-center architectures offer scalability by distributing communication tasks across QPUs rather than concentrating complexity "
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.20633v1 Announce Type: new Abstract: Server-centric quantum data-center architectures offer scalability by distributing communication tasks across QPUs rather than concentrating complexity in a centralized switching core. However, scaling such architectures increases the path length, the number of Bell-state measurements, and the loss of end-to-end fidelity. We ask whether the path diversity of a server-centric topology can be converted into a mechanism for preserving not only rate, but also fidelity. We study this through end-to-end purification as a fidelity-restoration mechanism. First, in a black-box model, we determine the minimum number of raw end-to-end Werner-state copies, each carrying the degraded Werner parameter of a distance-ell path, that purification must consume to recover a single copy matching an elementary link, comparing recursive 2-to-1 and optimized nested r-to-1 purification. Second, we instantiate these requirements in a probabilistic BCube architecture, whose edge-disjoint path diversity supplies the raw copies. Because purification imposes a lower bound on input fidelity, no path redundancy can raise the output below this threshold, which limits scaling. To address it we present the Hop-Independent Quantum Data Center (HI-QDC), an isometric, modular, scalable architecture in which purification transforms end-to-end entanglement across a module into an effective link-level resource for the inter-module topology. Our results identify the regimes in which a BCube module, under end-to-end purification, preserves both the fidelity and the yield of an elementary link. The module then hides its internal hop count and acts as an effective elementary link for a higher-level network. Thus topology supplies the path multiplicity purification requires, while purification converts it into fidelity recovery, enabling recursively scalable quantum data-center networks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.20633) | 2026-07-24
