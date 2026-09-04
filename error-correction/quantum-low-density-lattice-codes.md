---
title: "Quantum low-density lattice codes"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.03021"
summary: "arXiv:2609.03021v1 Announce Type: new Abstract: Gottesman-Kitaev-Preskill (GKP) codes provide a family of promising schemes for encoding discrete quantum information (qudits) into infinite-dimensional"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.03021v1 Announce Type: new Abstract: Gottesman-Kitaev-Preskill (GKP) codes provide a family of promising schemes for encoding discrete quantum information (qudits) into infinite-dimensional bosonic modes based on mathematical lattices. While such codes, when concatenated with discrete-variable codes, are relatively well studied, the construction and decoding of native GKP codes has largely remained open due to the computationally hard problems encountered. To address this challenge, we advocate a strategy of co-designing the decoder and the quantum error-correcting code itself by constructing lattices for which decoding is feasible: The requirement of efficient decoding effectively determines the quantum error-correcting code. This construction is built on classical low-density lattice codes (LDLCs), a lattice analogue of low-density parity-check codes, here lifted to families of GKP codes. Concretely, we introduce quantum versions of classical, randomly constructed LDLCs. We show that after suitable dimensionality reduction these codes have code properties comparable to or better than concatenated GKP-surface codes of equal number of modes. However, the GKP-LDLCs constructed here do not have a strictly sparse parity check matrix, which motivates our study of the performance of natively analog message-passing decoders originally developed for LDLCs when applied to concatenated GKP-LDPC codes. We show that the fully analog, linear-time decoder achieves performances close to state-of-the-art hybrid qubit-analog decoders. To facilitate future research on the structure and performance of general GKP codes, the relevant source code will be released in open-source Julia packages LatticeDecoder.jl and SymplecticGKP.jl.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.03021) | 2026-09-04
