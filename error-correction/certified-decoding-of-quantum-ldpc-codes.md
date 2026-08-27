---
title: "Certified decoding of quantum LDPC codes"
date: "2026-08-27"
updated: "2026-08-27"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.25545"
summary: "arXiv:2608.25545v1 Announce Type: new Abstract: Quantum low-density parity-check (qLDPC) codes reduce the qubit overhead of fault-tolerant quantum computation by an order of magnitude, but their decod"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

arXiv:2608.25545v1 Announce Type: new Abstract: Quantum low-density parity-check (qLDPC) codes reduce the qubit overhead of fault-tolerant quantum computation by an order of magnitude, but their decoding is harder than its classical counterpart: because many physical errors are equivalent up to stabilizers, the degenerate maximum-likelihood (ML) decoder must compare the probabilities of entire equivalence classes of errors, that is, partition functions, rather than single errors. The workhorse decoder BP+OSD sidesteps degeneracy heuristically and offers no guarantees. We treat degenerate decoding as probabilistic inference in an undirected graphical model: the probability of each logical class is the partition function of an unconstrained, strictly positive Markov random field over the code's check variables, a construction that generalizes the random-bond Ising mapping of the surface code to arbitrary CSS codes and to spacetime decoding with measurement errors and circuit-level noise. On this model we build two decoders. The first estimates all class partition functions by annealed importance sampling with common random numbers and attaches to every decision a certificate of optimality: a paired bootstrap test, or, composed with constant-factor estimators such as WISH, an exact optimality proof. The second is region-based: the Bethe free energy, whose bias cancels between classes, reproduces exact ML decoding on every tested surface-code instance at millisecond cost, and enlarging the regions to elimination clusters makes exact degenerate ML decoding of the [[72,12,6]] bivariate bicycle code feasible. Across surface codes and the bivariate bicycle codes [[72,12,6]] and [[144,12,12]], under code-capacity, phenomenological, and circuit-level noise, the sampling decoder matches or exceeds BP+OSD while certifying the bulk of its decisions, and the certificate flags exactly the syndromes on which any fast decoder should be distrusted.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.25545) | 2026-08-27
