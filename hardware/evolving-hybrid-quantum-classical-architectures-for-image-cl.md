---
title: "Evolving Hybrid Quantum-Classical Architectures for Image Classification"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03220"
summary: "arXiv:2610.03220v1 Announce Type: cross Abstract: Hybrid quantum classical neural networks integrate parameterized quantum circuits (PQCs) with established deep learning architectures, but their perfo"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03220v1 Announce Type: cross Abstract: Hybrid quantum classical neural networks integrate parameterized quantum circuits (PQCs) with established deep learning architectures, but their performance depends strongly on the choice of quantum circuit architecture, a choice that remains largely manual. Most existing approaches rely on hand-designed or fixed circuit ansatze, requiring circuit structure, gate composition, and qubit connectivity to be specified in advance with no guarantee that they suit the task. This limitation is especially acute in image classification, where quantum circuits must transform features extracted by classical networks while remaining compact enough for practical training, requirements that generic, task-agnostic ansatze are unlikely to satisfy simultaneously. We extend EXAQC, an evolutionary framework for automated quantum circuit discovery, to image classification. EXAQC evolves PQCs as intermediate processing modules while retaining classical feature-extraction and prediction layers. On MNIST, Fashion-MNIST, and CIFAR-10, EXAQC achieves 98.42%, 90.62%, and 85.47% accuracy, respectively, while using comparable gate counts to other quantum architecture-search methods. Against classical networks, evolved hybrid models maintain comparable accuracy with substantially fewer trainable parameters, reaching 85.68% on CIFAR-10 with over 25imes fewer parameters than a 10-layer CNN. Encoding choice also matters: rotation-based encodings (RX, RY, U3) outperform amplitude encoding by 22-25 points on CIFAR-10. These results demonstrate that automated circuit discovery yields compact quantum modules that can replace larger classical components in vision architectures while retaining competitive accuracy.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03220) | 2026-10-05
