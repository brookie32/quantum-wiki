---
title: "Breaking the cubic barrier for the inverse-free Solovay-Kitaev algorithm"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03655"
summary: "arXiv:2610.03655v1 Announce Type: new Abstract: The Solovay-Kitaev algorithm states that it is possible to efficiently compile unitaries to accuracy epsilon in ext{polylog}(1/epsilon) time using any u"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03655v1 Announce Type: new Abstract: The Solovay-Kitaev algorithm states that it is possible to efficiently compile unitaries to accuracy epsilon in ext{polylog}(1/epsilon) time using any universal gate set. While Solovay and Kitaev's initial work addressed inverse-closed gate sets, recently Bouland and Giurgica-Tiron showed it is possible to efficiently compile arbitrary gate sets without inverses. However, the exponent of their compilation algorithm is high. For example the inverse-free exponent for a qubit is over 8.62, while information theoretically it is known that an inverse-free exponent of 3 is possible in any dimension by a result of Oszmaniec, Sawicki, and Horodecki. This leads to a natural question: can one improve the exponent in Bouland and Giurgica-Tiron's algorithm? And are there any cases where the inverse-free exponent is below 3, thus surpassing existing information-theoretic arguments? To answer this question, we first show that a special case of the inverse-free compiling problem -- namely Pauli gates supplemented by an irrational rotation of a qubit - admits a highly efficient compilation algorithm with an exponent at most approx 2.138. Our algorithm fuses ideas from prior algorithms of Kuperberg and Sardharwalla, Cubitt, Harrow and Linden to construct an efficient ``Pauli golf'' compilation routine. We then extend these ideas to the general inverse-free case for a qubit, where we give a compiling algorithm with exponent at most 2.988. This result uses a novel form of approximate ``aiming'' of unitary corrections to improve the compilation efficiency. Our results give two examples of quantum compiling algorithms surpassing information-theoretic arguments, and demonstrate that there are many efficiency gains possible for inverse-free compilation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03655) | 2026-10-05
