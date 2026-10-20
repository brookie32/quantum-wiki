---
title: "Concrete LDVR Attacks with Fewer Signers"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2554"
summary: "We improve the concrete parameters of the attacks on the low-dimensional vector representation (LDVR) problem by Rodríguez García and Tessaro (ePrint 2026/2126), whose attack on canonical evaluation p"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

We improve the concrete parameters of the attacks on the low-dimensional vector representation (LDVR) problem by Rodríguez García and Tessaro (ePrint 2026/2126), whose attack on canonical evaluation points uses 5{,}020 signers. By combining their Chinese remainder theorem construction with a generalized birthday search over many challenges, we obtain a concrete attack with 488 signers and 173 corruptions over the Curve25519 scalar field. In 64 batches of 2^{25} challenges, the search finds solutions for six distinct challenges. We compare the counts measured at each stage of the search with predictions from an explicit heuristic model. For adversarially chosen evaluation points, we build on the binary attacks of Rodríguez García and Tessaro and give a construction that attains the optimal LDVR success probability for every oracle query budget when 2le nle253 and t_c=t in the uniform oracle model. At 228 signers and 114 corruptions, our implementation finds a successful subset using SHA-512 challenges after a cumulative total of 360.13 million queries across two runs, taking 168.60 seconds in total. We also give an explicit set of 256 evaluation points for which an efficient subset search attack using 128 corruptions succeeds with probability at least 51.92% per uniform challenge. For both canonical and adversarially chosen evaluation points, we analyze the query complexity and report measured and estimated running times.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2554) | 2026-10-19
