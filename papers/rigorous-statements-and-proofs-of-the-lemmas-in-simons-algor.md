---
title: "Rigorous Statements and Proofs of the Lemmas in Simon's Algorithm for the Dihedral Coset Problem and Their Underlying Hypothesis"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1714"
summary: "In a recent preprint, Simon proposed a polynomial-time quantum algorithm for the Dihedral Coset Problem and rested the analysis on four lemmas. Three of them carry only proof sketches, and this paper "
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

In a recent preprint, Simon proposed a polynomial-time quantum algorithm for the Dihedral Coset Problem and rested the analysis on four lemmas. Three of them carry only proof sketches, and this paper gives each of those three a statement that admits a single reading together with a complete proof. Lemma 1 follows from an exact second-moment computation for the subset-sum counts, and it holds with probability tending to one in place of the constant originally claimed. The amplitude bound of Lemma 3 follows from an exact Parseval identity on the cube of measurement outcomes and holds at every threshold with no well-behavedness hypothesis, so that predicate leaves the argument entirely. For Lemma 4, we compute both balls-in-bins covariances exactly and find that the second carries a term a fixed ball count leaves out. The assumption that the distinguished group contains no faulty samples can also be dropped. The two branch amplitudes share a signed prefactor, so the counting estimates control their difference and not the ratio the lemma states. We prove the additive form and show that the closing argument consumes nothing more than that. A single hypothesis survives all of this. It asks that the partition into the two sides be fixed independently of the measured string, and the rule the algorithm gives for choosing that partition does not supply it. Establishing these four lemmas therefore does not by itself establish the correctness of the algorithm.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1714) | 2026-08-17
