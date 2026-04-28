---
title: "Noise-aware selection of circuit cutting strategies under hardware noise non-uniformity"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "safety"
tags: [safety, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24422"
summary: "arXiv:2604.24422v1 Announce Type: new Abstract: Noise in contemporary quantum hardware is highly non-uniform across qubits and couplers, giving rise to localized low-noise 'islands' within otherwise n"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24422v1 Announce Type: new Abstract: Noise in contemporary quantum hardware is highly non-uniform across qubits and couplers, giving rise to localized low-noise "islands" within otherwise noisy device topologies. As quantum workloads scale, executions are increasingly forced to traverse high-noise regions, degrading algorithmic fidelity. Circuit cutting provides a route to circumvent such regions by decomposing large circuits into smaller subcircuits, but its practicality is limited by exponential sampling overhead and the lack of systematic guidance on how cut strategies should align with heterogeneous hardware noise. In this work, we present a hardware-noise-aware circuit cutting framework that explicitly exploits the spatial non-uniformity of noise in quantum devices. Rather than proposing a new cut-finding algorithm, we formalize the problem of device-constraint selection under realistic hardware noise and show that this choice critically determines both execution overhead and effective noise. Using a unified gate- and wire-cutting formulation, we demonstrate that small, hardware-informed relaxations in the device constraint yield exponential reductions in execution overhead while preserving alignment with low-noise hardware regions. Across representative workloads, our method achieves an average reduction in the number of circuit executions ranging from 5-54x for 20-qubit circuits, and enables tractable circuit cutting for 50-qubit circuits and application-level benchmarks where conventional strategies incur prohibitive overhead. These results establish noise-aware device-constraint selection as a necessary ingredient for making circuit cutting resource-efficient and practically deployable on contemporary quantum hardware.



## Related
- [[quantum-circuit-cutting-complexity-and-optimization|Quantum Circuit Cutting: Complexity and Optimization]]
- [[few-shot-cross-device-transfer-for-quantum-noise-modeling-on|Few-Shot Cross-Device Transfer for Quantum Noise Modeling on Real Hardware]]
- [[architecture-aware-unitary-synthesis|Architecture-aware Unitary Synthesis]]
- [[quantum-decoherence-of-the-surface-code-a-generalized-caldei|Quantum Decoherence of the Surface Code: A Generalized Caldeira-Leggett Approach]]
- [[noise-correlations-as-a-resource-in-pauli-twirled-circuits|Noise Correlations as a Resource in Pauli-Twirled Circuits]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24422) | 2026-04-28
