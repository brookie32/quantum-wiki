---
title: "Minimizing classical resources in variational measurement-based quantum computation for generative modeling"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.11578"
summary: "arXiv:2604.11578v2 Announce Type: replace Abstract: Measurement-based quantum computation (MBQC) is a framework for quantum information processing in which a computational task is carried out through "
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2604.11578v2 Announce Type: replace Abstract: Measurement-based quantum computation (MBQC) is a framework for quantum information processing in which a computational task is carried out through one-qubit measurements on a highly entangled resource state. Due to the indeterminacy of the outcomes of a quantum measurement, the random outcomes of these operations, if not corrected, yield a variational quantum channel family. Traditionally, this randomness is corrected through classical processing in order to ensure deterministic unitary computations. Recently, variational measurement-based quantum computation (VMBQC) has been introduced to exploit this measurement-induced randomness to gain an advantage in generative modeling. A limitation of this approach is that the corresponding channel model has twice as many parameters compared to the unitary model, scaling as N imes D, where N is the number of logical qubits (width) and D is the depth of the VMBQC model. This can often make optimization more difficult and may lead to poorly trainable models. In this paper, we present a restricted VMBQC model that extends the unitary setting to a channel-based one using only a single additional trainable parameter. We show, both numerically and algebraically, that this minimal extension is sufficient to generate probability distributions that cannot be learned by the corresponding unitary model.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.11578) | 2026-11-16
