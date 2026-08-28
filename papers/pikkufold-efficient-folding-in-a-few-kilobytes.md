---
title: "PikkuFold: Efficient Folding in a Few Kilobytes"
date: "2026-08-26"
updated: "2026-08-28"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1809"
summary: "Folding is a powerful technique for constructing efficient succinct proof systems, especially for computations that are expressed in a streaming fashion. We present PikkuFold, a new lattice-based fold"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Folding is a powerful technique for constructing efficient succinct proof systems, especially for computations that are expressed in a streaming fashion. We present PikkuFold, a new lattice-based folding protocol that improves upon state-of-the-art folding schemes such as SALSAA (ePrint 2025/2124) and Cyclo (EUROCRYPT 2026). One folding step communicates 5.5 KB beyond the commitments to its fresh inputs, against geq 30 KB for Cyclo and geq 60 KB for SALSAA for similar instances, while keeping prover time comparable and the verifier in the millisecond range. At the heart of our construction are layered random projections, whose algebraic structure makes them fast to verify and whose final image is short enough to send to the verifier directly, cutting out the cost of auxiliary commitments. We use those techniques to replace the extensive and restrictive range proofs of Cyclo, while still achieving only a small additive increase in the accumulator norm across multiple folds. PikkuFold is the first lattice-based construction that does not require any in-protocol commitments beyond those of the fresh inputs. Such commitments are the heavy part of a folding transcript: every prior lattice-based scheme commits to a decomposed or otherwise transformed witness during the fold, immediately increasing the communication by dozens of kilobytes. On top of that, we provide two contributions of independent interest, applicable beyond the context of folding schemes: (i) a Johnson-Lindenstrauss theorem for biased ternary matrices modulo q with certified concrete constants, which replaces the heuristic parametrisation of prior works, and (ii) a thorough analysis of the short-challenge sampler with fixed Hamming weight and operator-norm rejection, offering a wide range of parameter sets. Using this sampler as a drop-in replacement would lead to immediate improvements in a wide family of lattice-based protocols.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1809) | 2026-08-26
