---
title: "SAFE ma-QAOA: Surrogate-Assisted and Fine-Tuning Enhanced Multi-Angle QAOA with Parameter Distillation"
date: "2026-07-22"
updated: "2026-07-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.23377"
summary: "arXiv:2605.23377v2 Announce Type: replace Abstract: The multi-angle Quantum Approximate Optimization Algorithm (ma-QAOA) extends the Quantum Approximate Optimization Algorithm (QAOA) by assigning a la"
last_verified: "2026-07-22"
review_by: "2026-10-20"
stale: false
---

arXiv:2605.23377v2 Announce Type: replace Abstract: The multi-angle Quantum Approximate Optimization Algorithm (ma-QAOA) extends the Quantum Approximate Optimization Algorithm (QAOA) by assigning a larger number of independent variational parameters, thereby increasing expressivity and improving performance at low circuit depths. However, this larger parameterization makes training more difficult and requires repeated circuit evaluations for gradient-based optimization. In this work, we propose the Surrogate-Assisted and Fine-tuning Enhanced (SAFE) framework. SAFE first uses Low-Weight Pauli Propagation (LWPP) as a classical surrogate for pre-training ma-QAOA parameters before exact optimization. SAFE then applies parameter distillation, which removes angles that remain near zero after surrogate pre-training. Finally, SAFE performs exact fine-tuning by optimizing the remaining active parameters using the exact energy objective. We evaluate SAFE on instances of the Sherrington-Kirkpatrick model, two-dimensional square-lattice spin glass, and Max-Cut. SAFE with distillation provides the strongest overall results relative to exact-only: (i) a 64.3 percent reduction in active parameter count and (ii) a 94.5 percent reduction in estimated QPU workload. Within the SAFE workflow, adding distillation further reduces the optimizer steps to the near-optimal regime by 44.4 percent relative to without distillation. These results provide evidence that SAFE ma-QAOA can accelerate convergence to high-quality solutions while reducing the required quantum resources for exact fine-tuning, offering a resource-efficient route toward expressive ma-QAOA on NISQ hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.23377) | 2026-07-22
