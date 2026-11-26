---
title: "Schism: Reconfigurable Scale-Up Domains for Distributed Quantum Computing"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.31193"
summary: "arXiv:2611.31193v1 Announce Type: cross Abstract: Switch-based quantum datacenters connect quantum processing units (QPUs) through photonic switches and shared Bell-state measurement (BSM) devices. Sh"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.31193v1 Announce Type: cross Abstract: Switch-based quantum datacenters connect quantum processing units (QPUs) through photonic switches and shared Bell-state measurement (BSM) devices. Sharing BSMs saves hardware, but fixed connectivity constrains access to these resources. Local communication can overload one rack's BSMs while others remain idle; reaching those idle resources incurs additional optical loss and retries through switches and quantum frequency converters (QFCs). Programs remain locked into this locality-contention tradeoff as their communication patterns change. We propose Schism, an architecture that lets programs dynamically change which QPUs share each BSM pool. Schism places BSM pools at aggregation switches and QFCs on their core-facing uplinks. Top-of-rack switches establish reconfigurable native-wavelength circuits from QPUs to these pools, forming scale-up domains bounded by the optical loss budget. Reconfiguration reshapes resource sharing across racks without moving QPUs or migrating quantum states. Our key insight is that QPU grouping jointly determines photon-path loss and contention for BSM resources: locality alone cannot identify the best grouping, and a grouping pays off only if its savings outweigh the delay of reconfiguring to it. We develop an optimization framework that combines graph partitioning with resource-constrained completion-time estimates and dynamic programming to select how QPUs share BSM pools and when those groupings reconfigure, between or within circuit phases. Our evaluation using SeQUeNCe with trapped-ion parameters shows that Schism achieves communication speedups of 4.9-7.3x across 11 workloads on 32 QPUs compared to Fixed Clos connectivity and 3.6-8.3x compared to SwitchQNet. Schism also outperforms a hypothetical network-wide switch by 1.35-1.38x on the eight workloads whose phases fit in a pool, and trails it by 1.1-1.75x on the other three.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.31193) | 2026-11-26
