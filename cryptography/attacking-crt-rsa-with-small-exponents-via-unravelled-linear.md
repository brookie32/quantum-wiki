---
title: "Attacking CRT-RSA with Small Exponents via Unravelled Linearization"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2109"
summary: "We develop a new Coppersmith lattice attack on balanced CRT-RSA with small CRT exponents d_p, d_q using unravelled linearization. The new attack matches the practical effectiveness of the Takayasu–Lu–"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We develop a new Coppersmith lattice attack on balanced CRT-RSA with small CRT exponents d_p, d_q using unravelled linearization. The new attack matches the practical effectiveness of the Takayasu–Lu–Peng attack (JoC 2019) while using lattices of roughly half the dimension. In contrast to their attack, for which there is a noticeable gap between the theoretical predictions and experimental results, our theoretical estimates closely match the experimental results for all tested parameter sets. Our analysis further shows that the asymptotic bound remains d_p,d_q<N^{0.122}, so the new attack does not achieve the asymptotic improvement anticipated by Takayasu, Lu, and Peng. Nevertheless, performing LLL reduction on lower-dimensional lattices substantially reduces the running time, allowing us to attack much larger d_p,d_q in practice. Furthermore, through elegant variable substitutions, we extend our attack to two most significant bit (MSB) leakage models, obtaining the first attack exploiting MSB leakage of p+q and an improved attack exploiting MSB leakage of d_p,d_q. In both models, the asymptotic bounds improve as the amount of leakage increases and recover the Takayasu–Lu–Peng bound in the absence of leakage.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2109) | 2026-09-19
