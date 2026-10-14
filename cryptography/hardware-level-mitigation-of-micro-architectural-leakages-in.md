---
title: "Hardware-Level Mitigation of Micro-Architectural Leakages in Embedded Processors"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2478"
summary: "Cryptographic software, with its inherent flexibility and adaptability, has become essential for meeting today’s rapidly evolving security requirements, despite offering lower performance than dedicat"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Cryptographic software, with its inherent flexibility and adaptability, has become essential for meeting today’s rapidly evolving security requirements, despite offering lower performance than dedicated hardware accelerators. However, Side-Channel Analysis (SCA) complicates its secure execution on physical hardware, making robust protection a central challenge. While the masking countermeasure offers provable security guarantees in theory, its effectiveness is often undermined by the processor’s micro-architecture. In response, formal adversary models have been adapted to account for micro-architectural leakage under generic (but over-conservative) assumptions on the hardware. Consequently, achieving security under such a generic model requires compilers to produce less performant software. To bridge this gap, secure hardware-software co-design assumes a precisely specified hardware leakage behavior, enabling the specification of constraints for secure compilation. While this approach reduces the overhead required to counteract these effects, it does not entirely remove it. This work follows a more fundamental paradigm: instead of managing leakage in software, we aim at eliminating it at its source. Conceptually, we propose architectural changes to general-purpose processors at the Register-Transfer Level (RTL) that remove the root causes of micro-architectural leakages. The application of these changes enables the secure execution of masked software without introducing micro-architectural leakage under the Robust but Relaxed (RR) d-probing model, thereby removing the need for complex, security-aware compilers and hardware-specific workarounds in the software. While our countermeasures can be applied to many micro-architectures, we formally prove the security of each countermeasure individually and integrate them into the Ibex processor, whose security we evaluate as a whole through tool-assisted leakage assessment of the full netlist and physical experiments on a Field Programmable Gate Array (FPGA).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2478) | 2026-10-14
