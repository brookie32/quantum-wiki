---
title: "A systematic comparison of hard- and soft-constrained physics-informed molecular machine learning with the Clapeyron equation"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.36947"
summary: "arXiv:2609.36947v1 Announce Type: new Abstract: In molecular machine learning (ML), significant progress has been made on integrating fundamental thermodynamic relations into ML models. Such physics-i"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36947v1 Announce Type: new Abstract: In molecular machine learning (ML), significant progress has been made on integrating fundamental thermodynamic relations into ML models. Such physics-informed approaches can be categorized as hard-constrained, where the thermodynamic relations are embedded in the model architecture, and soft-constrained, where relations are included in the training loss. While both approaches have been applied to various property prediction tasks, a systematic comparison on experimental data is lacking. We herein compare hard- and soft-constrained approaches on a numerically challenging case study: the prediction of vapor pressure, saturated liquid and vapor molar volumes, and enthalpy of vaporization as functions of temperature for single-species vapor-liquid equilibrium, related by the exact Clapeyron equation. Furthermore, soft-constrained approaches in molecular ML typically balance data and physics losses with a fixed weighting factor, requiring careful tuning. To overcome this, we investigate the augmented Lagrangian method (ALM), well established in constrained optimization. We find that for the soft-constrained approach, using the ALM improves prediction performance in terms of constraint satisfaction by factor 2 and reduces training epochs compared to using a fixed penalty by 30%. Hence, in the soft-constrained approach, the use of the ALM is always recommended. The hard-constrained approach, which entails additional architectural design choices, can reach on par accuracy with the soft-constrained approach, at even higher thermodynamic consistency, reaching 12 orders of magnitude closer approximation of the Clapeyron equation. Overall, the hard-constrained approach is most promising when thermodynamic consistency is critical, yet requires tailoring the ML model architecture to the respective thermodynamic relation.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.36947) | 2026-09-30
