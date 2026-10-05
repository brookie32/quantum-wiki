---
title: "Efficiently and Reliably Measuring Information Processing Capacity in Dynamical Systems via Kernels"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03281"
summary: "arXiv:2610.03281v1 Announce Type: new Abstract: Information Processing Capacity (IPC) is a powerful system-agnostic metric for quantifying a dynamical system's computational capability and is widely u"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03281v1 Announce Type: new Abstract: Information Processing Capacity (IPC) is a powerful system-agnostic metric for quantifying a dynamical system's computational capability and is widely used in quantum reservoir computing. However, standard IPC suffers from severe computational limitations. Computing IPC involves estimating how well the system can reconstruct, via linear regression, an (in principle) infinite family of orthogonal polynomial functions of delayed inputs. In practice, this evaluation must be made finite, so we need only to consider polynomials up to a chosen maximum degree. Moreover, the computational complexity for computing IPC grows combinatorially with the considered maximum degree and delay. Here, we introduce Kernel-IPC (KIPC), a scalable framework that uses kernel methods to compute the total IPC without explicitly enumerating basis functions. This allows us to account for the full (infinite) basis (without degree truncation). We also provide a null-hypothesis test for statistically comparing the KIPC of two dynamical systems. We validate KIPC on an echo state network and demonstrate its utility for quantum reservoir computing on a disordered spin chain.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03281) | 2026-10-05
