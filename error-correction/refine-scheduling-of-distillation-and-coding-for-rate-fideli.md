---
title: "ReFINE: Scheduling of Distillation and Coding for Rate-Fidelity Tradeoff in Quantum Networks"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.21152"
summary: "arXiv:2609.21152v1 Announce Type: new Abstract: In quantum networks, nodes are connected via sharing of Einstein-Podolsky-Rosen (EPR) pairs, ideally with high fidelity and high rate. However, the fide"
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2609.21152v1 Announce Type: new Abstract: In quantum networks, nodes are connected via sharing of Einstein-Podolsky-Rosen (EPR) pairs, ideally with high fidelity and high rate. However, the fidelity of EPR pairs degrades due to imperfect generation and decoherence errors. Entanglement Distillation is a method that increases the fidelity but operates probabilistically and may destroy all involved EPR pairs upon failure. This failure reduces available EPR pairs for application use, thereby decreasing the service rate. Quantum Error Correction (QEC) is another mechanism to protect EPR pairs against error by forming what we term as Coding-Enhanced Memory (CEM). While effective, CEM requires extra time and resources to form the code, which also reduces the service rate. Existing methods often use static combinations of distillation and CEM, ignoring demand variations. This results in a low service rate without significant fidelity gain. Limited resources together with this rate-fidelity tradeoff make it essential to schedule when to run distillation, form CEM, or serve requests. We propose ReFINE, a demand-aware preemptive scheduler that based on application requirements either serves an available EPR pair immediately or preserves it in CEM. This selective use of CEM, only when needed, enables a better balance for rate-fidelity tradeoff than always using CEM. Between request arrivals, ReFINE either schedules distilling EPR pairs or forming CEM to protect distilled pairs, following one of the three priority policies: ReFINE-D (Distillation-First) first generates EPR pairs for distillation and then forms the CEM, prioritizing service rate. ReFINE-M (Memory-First) first forms the CEM, then generates the EPR pairs for distillation, prioritizing fidelity. ReFINE-C (Concurrent) performs both distillation and CEM formation concurrently, balancing between fidelity and service rate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.21152) | 2026-09-21
