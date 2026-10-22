---
title: "SALUS: Large-Scale Homomorphic Circuit Synthesis via Logic-Aware LUT Optimization"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2561"
summary: "Recently, growing interests are developed in optimizing fully homomorphic encryption (FHE) circuits to enable Boolean function evaluations over ciphertexts. While existing works utilize functional boo"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

Recently, growing interests are developed in optimizing fully homomorphic encryption (FHE) circuits to enable Boolean function evaluations over ciphertexts. While existing works utilize functional bootstrapping (FBS) to efficiently evaluate logic gates, the evaluation efficiency for large-scale circuits remains limited. Recent advances introduce a fast ciphertext conversion method, making it feasible to evaluate look-up tables (LUTs) over homomorphic multiplexer operation. In this work, we propose a new circuit synthesis framework, SALUS, which automatically generates and evaluates gate-level graphs over homomorphic LUTs given an input Boolean circuit. We apply the binary decision diagram (BDD) reordering method and multi-value refresh techniques to efficiently evaluate complex LUTs. Additionally, we propose a heuristic algorithm to merge LUTs in a given circuit into multi-output LUTs. In the experiments, we examine the efficiency of SALUS using a wide range of benchmark suites, including the EPFL and ISCAS benchmark circuits. We show that SALUS achieves a maximum reduction of up to 26× in computational latency compared to state-of-the-art homomorphic circuit synthesis method. Furthermore, we evaluate real-world applications, e.g., image filtering and matrix multiplication, and achieve an average speedup of 8.6× (with a maximum speedup of 24×) compared to the FBS-based method.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2561) | 2026-10-20
