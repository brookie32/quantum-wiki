---
title: "Optimizing Subspace Expansion in Quantum Chemistry through Operator Selection and Reference State Choice"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16362"
summary: "arXiv:2608.16362v1 Announce Type: new Abstract: The Virtual Quantum Subspace Expansion (VQSE) extends the Variational Quantum Eigensolver (VQE) by leveraging additional measurements on the reference s"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.16362v1 Announce Type: new Abstract: The Virtual Quantum Subspace Expansion (VQSE) extends the Variational Quantum Eigensolver (VQE) by leveraging additional measurements on the reference state to capture the influence of excluded virtual orbitals. This makes VQSE attractive for chemical applications where accurate energy differences along potential energy surfaces are crucial for modeling reaction rates and kinetics. In this work, we analyze VQSE performance on H_2 dissociation including references that use Hartree--Fock molecular orbitals with broken spin symmetry. We identify two mechanisms which affect accuracy: overlap of the reference state with the exact full configuration interaction (FCI) wavefunction and operator pool expressivity. We show these mechanisms are strongly co-dependent. When operators are restricted to act only from the active to the virtual space, results become highly sensitive to the reference, and enlarging the active space does not guarantee improved accuracy. In this case, prioritizing reference overlap over energy minimization is therefore essential. Adding single excitations and number operators within the active space recovers the accuracy of MR-CISD (multi-reference configuration interaction singles and doubles) regardless of the reference. In our noisy hardware experiments, we achieve chemical accuracy by adding additional operators and using strict regularization. These findings motivate careful co-design of reference fidelity, pool expressivity, and hardware constraints for practical VQSE deployment.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16362) | 2026-08-18
