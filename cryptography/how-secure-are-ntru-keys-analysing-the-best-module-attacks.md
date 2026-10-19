---
title: "How Secure are NTRU+ Keys? Analysing the Best Module Attacks"
date: "2026-10-18"
updated: "2026-10-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2527"
summary: "A recent analysis of module-BKZ [Ducas–Engleberts–Perthuis, Asiacrypt'25] predicts subexponential speedups for lattice reduction on module lattices over cyclotomic fields whose conductor has small odd"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

A recent analysis of module-BKZ [Ducas–Engleberts–Perthuis, Asiacrypt'25] predicts subexponential speedups for lattice reduction on module lattices over cyclotomic fields whose conductor has small odd prime factors. This threatens NTRU+, the South Korean standard for key encapsulation, and related schemes; however, the short vectors one seeks to find are short in the coefficient geometry, whereas module-BKZ operates in the canonical geometry. We introduce relative canonical and relative coefficient embeddings, realising a module over a cyclotomic field K as a module over any subfield L, and characterise when the two agree up to scaling: exactly when the radicals of their respective conductors c and ell satisfy rad(c)/rad(ell) in {1,2}. Furthermore we quantify the distortion incurred in general when passing between embeddings, and hence identify the optimal subfield for module-BKZ and BKZ to use. Estimating the cost of the best attack with simulation-based models [Perthuis–Trenkić, PQCrypto'26], we find that the best module attack saves only 4–10 blocksizes, costing NTRU+ keys at most three bits of security in the Core-SVP model. We further extend the analysis of overstretched NTRU regimes [Ducas–Woerden, Asiacrypt'19] to the module setting, and find the fatigue point is reached sooner than with unstructured counterparts, though NTRU+ parameterisations remain safe.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2527) | 2026-10-18
