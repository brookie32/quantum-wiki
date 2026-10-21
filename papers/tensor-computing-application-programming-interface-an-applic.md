---
title: "Tensor computing application programming interface: An application-oriented, lightweight API for portable high-performance tensor network computations"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.23917"
summary: "arXiv:2512.23917v2 Announce Type: replace Abstract: Tensor networks (TNs) are a central computational tool in quantum science and artificial intelligence. However, the lack of a unified software inter"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2512.23917v2 Announce Type: replace Abstract: Tensor networks (TNs) are a central computational tool in quantum science and artificial intelligence. However, the lack of a unified software interface across tensor-computing frameworks severely limits the portability of TN applications, coupling algorithmic development to specific hardware and software back ends. To address this challenge, we introduce the Tensor Computing Application Programming Interface (TCAPI)---an application-oriented, lightweight API designed to enable framework-independent, high-performance TN applications, currently specified for exttt{C++} and exttt{Python}. TCAPI provides well-defined type-system conventions that abstract tensor objects, together with a minimal yet expressive set of core functions for essential tensor manipulations and tensor linear-algebra operations, with operation semantics shared across language specifications. Through numerical demonstrations of representative tensor-network applications implemented in exttt{C++} using TCAPI, we show that code written against TCAPI can be migrated seamlessly across heterogeneous hardware and software platforms while achieving performance comparable to native framework implementations. We further provide open-source implementations of TCAPI based on extit{Cytnx} and extit{ITensor} in exttt{C++}, and on extit{NumPy} in exttt{Python}, demonstrating its practicality and ease of integration with existing tensor-computing frameworks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.23917) | 2026-10-21
