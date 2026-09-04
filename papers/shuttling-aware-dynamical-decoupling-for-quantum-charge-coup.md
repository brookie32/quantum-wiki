---
title: "Shuttling-aware dynamical decoupling for quantum charge-coupled devices"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.03014"
summary: "arXiv:2609.03014v1 Announce Type: new Abstract: Dynamical decoupling (DD) helps maintain high-fidelity quantum computations by suppressing dephasing noise through carefully timed refocusing pulses. In"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.03014v1 Announce Type: new Abstract: Dynamical decoupling (DD) helps maintain high-fidelity quantum computations by suppressing dephasing noise through carefully timed refocusing pulses. In quantum charge-coupled device (QCCD) architectures, however, where ions are shuttled throughout the device, transport constrains when pulses can be applied and affects the phase accumulated by an ion. Conventional DD methods do not account for shuttling and may therefore schedule pulses that must be omitted or shifted after transport scheduling, weakening the protection from dephasing. We therefore introduce shuttling-aware dynamical decoupling (SADD), an offline compiler pass that jointly selects refocusing pulses and local ion rerouting while preserving logical-gate timings and the total schedule length. In benchmark simulations, SADD improves average final-state fidelity over both the original schedules and a simple nearest-feasible Hahn-echo baseline when dephasing dominates control and transport errors and varies slowly enough for DD. Rerouting enables otherwise infeasible pulse timings, while spatial information about the noise can provide further gains. These benefits disappear, however, when the added transport introduces too much error. Overall, our results show that coordinating DD with ion transport is an effective compiler strategy for reducing dephasing in QCCD processors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.03014) | 2026-09-04
