---
title: "Integer Linear Programming Decoder for Abelian and Non-Abelian Topological Codes"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.18512"
summary: "arXiv:2608.18512v1 Announce Type: new Abstract: Topological orders (TOs) are widely used as quantum error-correcting codes, with anyon excitations serving as error syndromes. For certain Abelian TOs, "
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.18512v1 Announce Type: new Abstract: Topological orders (TOs) are widely used as quantum error-correcting codes, with anyon excitations serving as error syndromes. For certain Abelian TOs, decoding can be performed by independently matching particle-antiparticle pairs of each species. However, matching-based decoders cannot handle more general fusion rules in either Abelian or non-Abelian TOs, nor account for noise that correlates different anyon species. While clustering decoders are more broadly applicable, they typically neglect anyon data and fusion properties, leading to poor performance in practice. In this work, we introduce a fundamentally different decoder for arbitrary TOs based on integer linear programming (ILP). The ILP formulation linearizes the error-correction problem through the introduction of auxiliary variables and encodes fusion rules as linear constraints. Classical optimization then identifies the minimum-weight error configuration. As concrete examples, we determine error-correction thresholds for three TOs: the Abelian Z_2 TO under depolarizing noise, where charge and flux errors are correlated; the Abelian Z_3 TO, which does not admit a pairwise matching decoder; and the non-Abelian D_4 TO under noise channels that generate all anyon species. We demonstrate the versatility of the ILP decoder by showing a clear performance advantage over most existing decoders in all three cases. We further extend the method to incorporate noisy syndrome measurements and propose a just-in-time variant for continuous error correction. Our results establish ILP as a natural framework for handling correlated errors and general anyon fusion rules, and as a powerful and flexible general-purpose decoder for incoherent anyon noise in arbitrary TOs, with applications to fault-tolerant quantum computation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.18512) | 2026-08-20
