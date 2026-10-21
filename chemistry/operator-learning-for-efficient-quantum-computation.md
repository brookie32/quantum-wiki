---
title: "Operator learning for efficient quantum computation"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.20184"
summary: "arXiv:2606.20184v2 Announce Type: replace Abstract: An efficient implementation of quantum algorithms is often hindered by the lack of efficient primitives for operators and state preparation. This li"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2606.20184v2 Announce Type: replace Abstract: An efficient implementation of quantum algorithms is often hindered by the lack of efficient primitives for operators and state preparation. This limits both the ability of near-term quantum hardware to simulate complex problems and the potential of fault-tolerant algorithms to achieve practical quantum advantage. To address this, we propose a framework that maps discrete operators onto compact, structured quantum circuits. The resulting variational circuits can be tailored to the connectivity and long-range interaction of the target hardware. The learning process employs backpropagation together with a cost function that efficiently optimizes unitary operators and non-unitary --dense or sparse-- operators using only a single ancilla qubit for block encoding. Additionally, we introduce a regularization term that reduces the approximation error. The approach is validated for both quantum mechanical and engineering applications. In the former case, we learn propagators that arise in native quantum problems --such as quantum simulation and quantum chemistry-- and achieve improved resource scaling in comparison to standard Suzuki--Trotter expansions. In the latter case, we demonstrate the approach's ability to implement the second-order central finite difference approximation of the Laplace operator --relevant for solving partial differential equations-- while improving upon current error metrics. The final example deals with learning a dense, non-unitary operator that arises in the analysis of inviscid potential flow around an airfoil. These results motivate the extension of the framework to a broader class of operator-synthesis problems beyond the prototypical engineering and quantum applications considered here.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.20184) | 2026-10-21
