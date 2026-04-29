---
title: "Simon's Algorithm for the Even-Mansour Cipher on Quantum Hardware"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25509"
summary: "arXiv:2604.25509v1 Announce Type: new Abstract: Simon's algorithm is a polynomial period-finding algorithm that has been used to exploit the algebraic structure of specific symmetric ciphers, showing "
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25509v1 Announce Type: new Abstract: Simon's algorithm is a polynomial period-finding algorithm that has been used to exploit the algebraic structure of specific symmetric ciphers, showing that exponential speedups in their cryptanalysis are theoretically possible. While the theoretical framework for an attack using Simon's algorithm on the Even-Mansour cipher is well-established, practical implementations on noisy intermediate-scale quantum (NISQ) hardware remain limited. This paper presents a proof of concept quantum cryptanalysis of the Even-Mansour cipher using Simon's period-finding algorithm on NISQ hardware. For N = 3 and N = 4, we successfully demonstrate secret key recovery for N-bit constructions on the ibm_miami processor. Our experiments also identify a scaling limitation in the classical pre-processing stage: The DORCIS circuit optimization tool encountered a memory bottleneck at N = 5, preventing the generation of optimized circuits for larger key lengths. Our results suggest firstly that Simon's algorithm is effective for the Even-Mansour cipher for short bit lengths on current quantum hardware. Secondly, while DORCIS is effective for the small-scale S-boxes for which it was designed, there remains a need for the investigation of more scalable and efficient synthesis tools capable of handling larger and more general permutations in the context of Even-Mansour ciphers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25509) | 2026-04-29
