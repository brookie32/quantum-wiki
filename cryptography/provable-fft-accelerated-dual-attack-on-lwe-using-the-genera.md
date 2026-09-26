---
title: "Provable FFT-Accelerated Dual Attack on LWE Using the General Dual Lattice"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2186"
summary: "The dual attack is a central tool for evaluating the security of the Learning with Errors (LWE) problem, which is the foundation of the lattice-based cryptosystems such as ML-KEM. Since the introducti"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

The dual attack is a central tool for evaluating the security of the Learning with Errors (LWE) problem, which is the foundation of the lattice-based cryptosystems such as ML-KEM. Since the introduction of FFT acceleration by Guo and Johansson (ASIACRYPT 2021) and subsequent optimizations in the MATZOV report, FFT-based dual attacks have achieved concrete security estimates for ML-KEM. However, these results rely on one specific independence heuristic that is known to fail in certain parameter regimes (CRYPTO 2023). Recent work by Pouly and Shen (EUROCRYPT 2024) initiated the study of provable dual attacks through explicit geometric analysis, but restricted the analysis to the orthogonal lattice, requiring approximately (mapprox2n) LWE samples. Qu and Xu (ASIACRYPT 2025) subsequently introduced modulus switching into the provable dual-attack setting, enabling evaluation over a smaller modulus, with a revised analysis given in their later version. More recently, a closely related ePrint revisited the concrete complexity estimates of these provable attacks after correcting the norm-bound formula used in the earlier analysis. In this work, we provide a provable correctness analysis of the Guo--Johansson-style FFT-based dual attack over the general dual lattice. By extending the analysis from the orthogonal lattice to L_q(mathbf{A}^{T}), where mathbf{y} is not restricted to mathbf{0}, we reduce the required number of LWE samples from mapprox2n to mapprox n while retaining the computational efficiency of FFT-based score evaluation. We further derive an explicit upper bound on the false-positive probability via an integral estimate for a geometric distinguishing event. For concrete complexity estimation, we follow the abstractions and cost models used in prior provable analyses while refining the probability-dependent treatment of the norm bounds. We obtain attack costs of 216, 317, and 426 bits for ML-KEM-512, ML-KEM-768, and ML-KEM-1024, respectively. Compared with the recomputed estimates of the previous best published provable dual attack, these represent reductions of 22, 30, and 52 bits, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2186) | 2026-09-23
