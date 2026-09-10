---
title: "Towards Practical Privacy-Preserving SAT Solving"
date: "2026-09-08"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1918"
summary: "Privacy-preserving Boolean satisfiability (SAT) solvers allow multiple distrustful parties to solve the conjunction of their private formulas without revealing their inputs. Prior work on privacy-pres"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Privacy-preserving Boolean satisfiability (SAT) solvers allow multiple distrustful parties to solve the conjunction of their private formulas without revealing their inputs. Prior work on privacy-preserving SAT solvers, i.e., ppSAT (USENIX Security 2022), fails to solve formulas of practical size and complexity because it supports only the most basic SAT-solving algorithm. We bring privacy-preserving SAT solving closer to practicality by introducing ppCDCL. Through carefully orchestrated oblivious data structures and solver architecture, our new solver enables conflict-driven clause learning (CDCL) and efficient propagation, the two most important features of modern plaintext SAT solvers. Evaluation results show that ppCDCL outperforms ppSAT in both capability and efficiency. It solves significantly more instances: 98% vs. 65% on the Haplotype benchmarks and 84% vs. 28% on the larger, more diverse SATLIB benchmarks. Furthermore, it solves 36% of SATLIB instances within 1,000 seconds compared to only 4% for ppSAT.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1918) | 2026-09-08
