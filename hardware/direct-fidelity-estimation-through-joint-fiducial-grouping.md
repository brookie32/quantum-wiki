---
title: "Direct fidelity estimation through joint fiducial grouping"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.18548"
summary: "arXiv:2608.18548v1 Announce Type: new Abstract: Fault-tolerant quantum computation hinges on the requirement for low physical error rates. Reaching below threshold regime requires the accounting of ci"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.18548v1 Announce Type: new Abstract: Fault-tolerant quantum computation hinges on the requirement for low physical error rates. Reaching below threshold regime requires the accounting of circuit dependent noise, that is inherent to the execution context in which a quantum gate is usually embedded. Direct fidelity estimation is a technique that offers natural context preservation as it solely requires the insertion of local Pauli preparation and measurement fiducials around the window of interest. However, each sampled input-output Pauli pair demands its own preparation and measurement setting, an overhead that grows rapidly once the target gate is no longer Clifford. We introduce joint fiducial grouping, which partitions Pauli pairs into sets with commuting input and output operators, allowing several Pauli-transfer coefficients to be estimated within the same preparation-measurement setting. We derive an unbiased grouped estimator and finite-sample guarantees showing that grouping always reduces the number of distinct input-output settings and can also reduce the required channel uses when the target weight is concentrated within compatible groups. We characterize these gains for the parametric two-qubit gate fSim(heta,arphi), and use the grouped estimator as a context-sensitive reward for reinforcement-learning-based gate calibration. Our results provide a practical route to lower-overhead, context-preserving fidelity estimation for continuously parameterized quantum gates.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.18548) | 2026-08-20
