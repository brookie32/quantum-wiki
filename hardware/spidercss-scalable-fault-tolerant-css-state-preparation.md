---
title: "SpiderCSS: Scalable Fault-Tolerant CSS State Preparation"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03714"
summary: "arXiv:2610.03714v1 Announce Type: new Abstract: Fault-tolerant preparation of logical states is a critical primitive for the realization of large-scale fault-tolerant quantum computing. This paper int"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03714v1 Announce Type: new Abstract: Fault-tolerant preparation of logical states is a critical primitive for the realization of large-scale fault-tolerant quantum computing. This paper introduces SpiderCSS, a scalable compilation pipeline that generates highly-optimized, fault-tolerant state preparation circuits for arbitrary Calderbank-Shor-Steane (CSS) codes. Starting from an idealized specification of a CSS state, we use the ZX-calculus and fault-equivalent rewrites to construct a diagram that prepares the given state while preserving the fault tolerance of the initial ideal ZX-diagram. From this diagram, SpiderCSS constructs a fault-tolerant CSS-state preparation circuit using a modular construction that is CNOT-minimal both within each component and also in the way these components are connected together. By only using fault-equivalent rewrites, the final circuit is provably fault-tolerant without needing expensive verification. Monte Carlo simulations across a variety of CSS codes up to distance 15 show that SpiderCSS scales efficiently and constructs circuits with substantially reduced depth and qubit footprint compared to existing scalable and heuristic methods, while simultaneously achieving an average decrease of 33.7% in logical error rate and an increase of 9.5% in acceptance rate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03714) | 2026-10-05
