---
title: "Parity Push Post-Selection with Soft Parity Constraints for Quantum LDPC Codes"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.23759"
summary: "arXiv:2611.23759v1 Announce Type: new Abstract: Post-selection lowers the logical error rate of a quantum error-correcting code by rejecting unreliable shots. For a code with K logical observables, th"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23759v1 Announce Type: new Abstract: Post-selection lowers the logical error rate of a quantum error-correcting code by rejecting unreliable shots. For a code with K logical observables, the logical gap, a standard post-selection criterion, involves 2^K logical classes, and existing approximations to it suffer from a non-convergence error floor or a shielding effect. We introduce a decoder-agnostic post-selection strategy for quantum low-density parity-check (qLDPC) codes, called parity push post-selection (PPPS), which re-decodes a shot once per logical observable with a push toward the opposite parity. Each push adds one check node and one variable node to the Tanner graph of the detector error model, and we accept a shot only when every re-decoding returns a solution in the original logical class. We show that, with degenerate maximum-likelihood decoding, PPPS accepts a shot exactly when the logical gap exceeds the push strength lambda. Applied with the Relay-BP decoder to the [[72,12,6]] bivariate bicycle code at p=10^{-3} and the [[144,12,12]] code at p=3imes10^{-3} under circuit-level depolarizing noise, PPPS lowers the logical error rate by factors of about 50 and 75, respectively, at rejection rates near 1%. We observe that PPPS rejects failures that prior post-selection strategies cannot reject, and thus shows improved performance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.23759) | 2026-11-19
