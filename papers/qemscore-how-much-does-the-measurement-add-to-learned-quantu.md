---
title: "QEMScore: How Much Does the Measurement Add to Learned Quantum Error Mitigation?"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.17896"
summary: "arXiv:2609.17896v1 Announce Type: new Abstract: How much does the noisy measurement add to learned quantum error mitigation? An accuracy table cannot say, because a model handed circuit structure can "
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2609.17896v1 Announce Type: new Abstract: How much does the noisy measurement add to learned quantum error mitigation? An accuracy table cannot say, because a model handed circuit structure can score well without reading the measurement at all. QEMScore adds the comparison that can. Each simulated circuit carries an exact ideal answer. The learned mitigator is scored beside a capacity-matched control, a model just as flexible that reads the same circuit description but never the measurement. Each method's measurement spend is accounted and not equalized. We run a controlled campaign on simulated circuits and reanalyze two published learned mitigators, Q-LEAR and QRAFT, from their released hardware data. Three findings stand out. First, under familiar within-family conditions (S0) evaluated across two spin-chain families and three seeds, continuous couplings identify the target, and the control that never reads the measurement matches 87.7 to 100.5 percent of the mitigator's gain over an affine fit to the circuit description. A plain polynomial in the coupling parameters, fitted after the campaign, beats the mitigator on all six evaluations, reflecting the selected learners' capacity. Second, for these selected learners, matching most of the gain is not matching the accuracy: on five of six evaluations the mitigator removes 19.5 to 74.5 percent of the error the capacity-matched control leaves, a learner-specific gap rather than a measurement requirement. Third, on released hardware data where descriptors only partially identify queries, the findings differ: flexible models of the descriptors show negligible mean gain over affine fits in Q-LEAR, and measurement inputs carry predictive gains in both Q-LEAR and QRAFT. These comparisons reflect representation- and protocol-specific behavior rather than an isolated cross-regime difference. A learned mitigator's accuracy should therefore be reported beside such controls.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.17896) | 2026-09-17
