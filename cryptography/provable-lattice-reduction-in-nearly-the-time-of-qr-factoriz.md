---
title: "Provable Lattice Reduction in Nearly the Time of QR Factorization"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2541"
summary: "We propose a deterministic lattice-reduction algorithm with bit complexity matching QR factorization up to logarithmic factors, and an implementation that uses fewer instructions than exttt{flatter} ("
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

We propose a deterministic lattice-reduction algorithm with bit complexity matching QR factorization up to logarithmic factors, and an implementation that uses fewer instructions than exttt{flatter} (CRYPTO 2023) in our benchmarks. The key technical innovations are iterative precision management, a finer-grained potential analysis, and a new representation for bases and transformations, all integrated into a recursive framework. We analyze the asymptotic behavior of our algorithm, and show that, for fixed reduction and output accuracy, the running time is widetilde O!left( n^omegaigl(1+logkappa_{rm col}(mathbf B)igr)right), where mathbf Binmathbb Z^{nimes n} is a nonsingular lattice basis and kappa_{rm col} is the optimally column-scaled spectral condition number. This gives a finer complexity than prior art, by allowing a tighter condition number kappa_{rm col}. Besides, through a new observation on the recursive structure, we demonstrate that the algorithm is free from heuristic assumptions. We compare our implementation with exttt{flatter} on q-ary, NTRU-like, scaled q-ary, and Coppersmith inputs. Our implementation uses fewer instructions in all 153 executions. The median ratios of exttt{flatter}'s instruction count to ours are 1.55 for ordinary q-ary inputs and 1.86 for NTRU-like inputs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2541) | 2026-10-19
