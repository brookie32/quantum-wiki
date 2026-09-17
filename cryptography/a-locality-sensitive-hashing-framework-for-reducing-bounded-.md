---
title: "A Locality-Sensitive Hashing Framework for Reducing Bounded Distance Decoding to EDCP"
date: "2026-09-16"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2055"
summary: "Bounded Distance Decoding (BDD) is a fundamental primitive in both code- and lattice-based post-quantum cryptography. Prior work of Regev (FOCS~2002) and Brakerski, Kirshanova, Stehle and Wen (PKC~201"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Bounded Distance Decoding (BDD) is a fundamental primitive in both code- and lattice-based post-quantum cryptography. Prior work of Regev (FOCS~2002) and Brakerski, Kirshanova, Stehle and Wen (PKC~2018) connected lattice BDD and Learning With Errors (LWE) to the Extrapolated Dihedral Coset Problem (EDCP), but these reductions rely heavily on geometric structure and do not naturally extend to coding-theoretic metrics. We present a general quantum reduction from BDD over finite Abelian groups equipped with translation-invariant metrics to EDCP, requiring only the existence of an appropriate locality-sensitive hash family. Instantiating this framework yields new reductions for decoding in the Hamming metric, rank metric, and the p-Lee metric (which coincides with the standard Lee metric when p = 1). For the Hamming and rank metrics, our reductions only yield a non-negligible number of EDCP states in parameter regimes where known decoding algorithms are already efficient. However, we recover the LWE-to-EDCP reduction within our framework by combining known equivalences between lattice CVP/BDD in the ell_p norm and p-Lee metric decoding.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2055) | 2026-09-16
