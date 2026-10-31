---
title: "Optimality and Efficiency of Higher-Order Rank-Based Side-Channel Attacks against Inner Product Masking Schemes"
date: "2026-10-29"
updated: "2026-10-31"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2676"
summary: "Higher-Order Spearman Coefficient Analysis (HO-SPA) is of particular interest in non-profiling Side-Channel Attacks (SCA) due to its effectiveness against monotonic nonlinear leakage. However, the opt"
last_verified: "2026-10-31"
review_by: "2027-01-29"
stale: false
---

Higher-Order Spearman Coefficient Analysis (HO-SPA) is of particular interest in non-profiling Side-Channel Attacks (SCA) due to its effectiveness against monotonic nonlinear leakage. However, the optimal form, effective order combinations, and performance of HO-SPA (or its variants) remain underexplored. This work systematically revisits HO-SPA in the presence of Boolean Masking (BM) and Inner Product Masking (IPM). Specifically, we propose a new variant of HO-SPA, called HO-ASPA (Higher-Order Adjusted Spearman Coefficient Analysis), and derive the optimal form of HO-ASPA for two-share BM and IPM across a wide range of order combinations under the Hamming weight (HW) leakage model. We first derive the optimal form of HO-ASPA by extending the Spearman Coefficient Analysis to higher-order moments, while preserving the centered-product combination of the share leakages. We then establish an upper bound on the maximal correlation induced by the rank transformation and characterize the relationship between the signal-to-noise ratio and the optimal correlation coefficient in the rank-domain, and extend these analyses to IPM. To enable a fair comparison, we also derive the optimal forms of Higher-Order Correlation Power Analysis (HO-CPA) and HO-ASPA for both BM and IPM under the Least-Significant-Bit (LSB) leakage model. Our analysis highlights a key distinction: unlike HO-CPA, where higher orders often outperform the lowest feasible order, HO-ASPA shows no significant performance gap between higher-order and lower-order attacks. Moreover, under the HW leakage model, our HO-ASPA not only aligns with existing results and succeeds in counteracting the security order amplification, but also significantly outperforms Kruskal-Wallis Analysis (KWA)-based attacks at various order combinations. We further validate the effectiveness of the proposed HO-ASPA through simulated and real-world experimental evaluations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2676) | 2026-10-29
