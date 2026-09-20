---
title: "Radical Ring-LWR: Efficient Key Encapsulation and Signatures from Structured Rounding"
date: "2026-09-18"
updated: "2026-09-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2078"
summary: "State-of-the-art lattice-based cryptography requires a power-of-two cyclotomic field that limits the attainable security levels, or a module structure for which the cost grows quadratically in the mod"
last_verified: "2026-09-20"
review_by: "2026-12-19"
stale: false
---

State-of-the-art lattice-based cryptography requires a power-of-two cyclotomic field that limits the attainable security levels, or a module structure for which the cost grows quadratically in the module rank. Radical rings were recently proposed as a solution in the context of Learning With Errors (LWE) based Key Encapsulation Mechanisms (KEMs) with heuristic hardness arguments for the Ring-LWE security and failure probability. We develop the Learning With Rounding counterpart, Radical Ring-LWR (RR-LWR). We give a proved closed-form bound on the distortion incurred from the error sampling independent of the radical ring parameters: this places RR-LWR inside the regime identified by Peikert as safe for instantiating Ring-LWE/LWR. We instantiate two schemes: Mithril, an IND-CCA KEM, and Octarine, an EF-CMA signature scheme. They are built on a single radical-ring arithmetic foundation based on powers of two (favorable for sampling, rounding and masking) and we provide security reductions in the QROM to RR-LWR and SelfTarget-RR-SIS, a radical-ring variant of SIS. We show that the KEM failure probability estimators used for power-of-two cyclotomics are insufficient and provide an exact solution tailored to the RR-LWR setting. Finally, we instantiate Mithril and Octarine with concrete parameters and benchmark optimized AVX2 and Arm Cortex-M4 implementations, showing that both are competitive with (and in some cases significantly faster than) the MLKEM and MLDSA standards.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2078) | 2026-09-18
