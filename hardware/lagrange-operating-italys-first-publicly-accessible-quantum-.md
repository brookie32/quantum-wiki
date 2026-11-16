---
title: "Lagrange: Operating Italy's First Publicly-Accessible Quantum Computer for Research and Education"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.21695"
summary: "arXiv:2604.21695v2 Announce Type: replace Abstract: We describe the design, implementation, and nine-month operational experience of the software management stack for Lagrange, an IQM Spark five-qubit"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2604.21695v2 Announce Type: replace Abstract: We describe the design, implementation, and nine-month operational experience of the software management stack for Lagrange, an IQM Spark five-qubit superconducting quantum computer jointly acquired by LINKS Foundation, Politecnico di Torino and the Italian National Institute of Metrological Research (INRiM), and managed by LINKS. Lagrange is, to our knowledge, the first quantum computer in Italy that is fully operational and accessible to students and researchers from multiple institutions under formal service agreements, and to the general public under commercial agreements. When installed in mid-2025, the IQM Spark hardware was delivered by the vendor with authentication only: no billing, project management or fair usage enforcement were provided. We developed a modular middleware layer that filled that gap without modifying any vendor client software, by intercepting API calls through a proxy that enforces project-based budgets, reservation-aware authorisation, and per-user fairness policies. The middleware adopts a plugin architecture that cleanly separates vendor-specific logic from site-specific policies, enabling reuse across different quantum hardware backends and deployment contexts. Since entering production in September 2025, the system has processed over 240,000 quantum jobs totalling more than 1 week of QPU execution time, with greater than 98% uptime. Notably, students at Politecnico di Torino regularly use the machine during both lectures and formal examinations -- a practice we believe to be unique in Europe. We report on the system architecture, the operational lessons learned, and the infrastructure choices that made this deployment possible.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.21695) | 2026-11-16
