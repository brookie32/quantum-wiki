---
title: "Wigner Time: a data-oriented approach to experimental timeline creation for quantum science and technology"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "sensing"
tags: [sensing, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.06230"
summary: "arXiv:2609.06230v2 Announce Type: replace Abstract: Precisely timed, multi-device control in atomic, molecular and optical physics is provided by specialized real-time systems, which impose their own "
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2609.06230v2 Announce Type: replace Abstract: Precisely timed, multi-device control in atomic, molecular and optical physics is provided by specialized real-time systems, which impose their own terms on the description of the experiment: a program over a global clock, in which every stage boundary is an absolute time computed from everything preceding it. Such descriptions are tightly coupled -- changing one stage affects all later ones -- and are correspondingly hard to reuse, inspect, or move elsewhere. We introduce Wigner Time, a Python package in which the experimental procedure is instead represented as data: a table of timed updates, assembled by composing functions and referred to named points in the experiment rather than to absolute instants. Hardware enters only at a final conversion step, leaving the description readable and back-end agnostic. Wigner Time has run two cold-atom setups for more than two years, where replacing a hand-written real-time program improved the achievable temporal resolution five-fold; the design applies to any domain requiring precise multi-device timing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.06230) | 2026-10-08
