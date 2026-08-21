---
title: "Demons on a Budget: Adaptive Measurement Placement at the Entanglement Phase Transition"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.19248"
summary: "arXiv:2608.19248v1 Announce Type: new Abstract: Monitored quantum circuits exhibit a measurement-induced phase transition between volume-law and area-law entanglement as a function of the measurement "
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.19248v1 Announce Type: new Abstract: Monitored quantum circuits exhibit a measurement-induced phase transition between volume-law and area-law entanglement as a function of the measurement rate p. Prior work places measurements at random locations and treats the rate as the control parameter. We instead fix the measurement budget and vary the placement process, comparing random placement against hand-designed and learned policies in brickwork random Clifford circuits at matched budget. First, placement geometry matters more than placement information. A deterministic contiguous sweep cuts the half-cut entropy by a factor of 3.4 relative to random placement, while equal-coverage unstructured placement and a greedy policy with full state access do far worse. The effect is carried by spatial order alone: measuring the k least recently measured sites gives 4.14 pm 0.06 bits with random tie-breaking and 1.29 pm 0.04 bits with position-ordered tie-breaking. Second, the sweep eliminates the transition rather than shifting it. Tripartite mutual information crossings recede as p^* propto 1/L, the steady-state entropy saturates at an L-independent ceiling near 0.46/p, and data for 64 le L le 512 collapse onto the form S = p^{-1} f(pL) predicted by a ballistic regrowth argument. Third, in stabilizer dynamics every outcome is deterministic or a fair coin flip, so the record's Shannon entropy is exactly countable; the sweep dominates the entropy-versus-record-cost frontier while paying the same roughly one bit per measurement as random placement. Policies trained by cross-entropy and proximal policy optimization do not find the sweep: score-based policies parameterize which sites to measure, not the order in which degenerate scores are resolved, and the effect lives in that order. The phase diagram of monitored dynamics is a property of the placement process, not only of the measurement rate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.19248) | 2026-08-21
