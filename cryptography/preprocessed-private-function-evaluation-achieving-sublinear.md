---
title: "Preprocessed Private Function Evaluation: Achieving Sublinear Online Complexity for Lookup Tables"
date: "2026-08-07"
updated: "2026-08-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1631"
summary: "Private Function Evaluation (PFE) facilitates the secure computation of private functions on private inputs in an oblivious manner, ensuring that both the function and the inputs remain confidential t"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

Private Function Evaluation (PFE) facilitates the secure computation of private functions on private inputs in an oblivious manner, ensuring that both the function and the inputs remain confidential throughout the entire computational process. PFE has garnered significant attention due to its critical applications in various domains, such as privacy-preserving healthcare systems and privacy-preserving credit checks, where safeguarding the confidentiality of the function itself is of paramount importance. However, despite its broad applicability, existing PFE schemes often exhibit inefficiencies, even in relatively straightforward scenarios such as the evaluation of lookup tables. To mitigate these limitations, we propose a novel variant of PFE, termed Preprocessed Private Function Evaluation (PPFE), which leverages preprocessing techniques to significantly enhance the efficiency of online computations. Within this framework, we introduce a specialized construction tailored specifically for lookup table operations, achieving sublinear complexity during the online computation phase. The efficacy of the proposed approach is demonstrated through experimental evaluations. For a lookup table of size 2^{24}, the online computation time required to process a single query is about 3 milliseconds, representing a performance improvement of more than an order of magnitude compared to existing results. Furthermore, the proposed scheme exhibits strong scalability, effectively handling thousands of adaptive queries within the same framework.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1631) | 2026-08-07
