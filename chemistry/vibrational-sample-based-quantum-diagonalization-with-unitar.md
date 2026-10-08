---
title: "Vibrational Sample-Based Quantum Diagonalization with Unitary-Cluster-Jastrow Ansatze on IBM QPUs"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.09532"
summary: "arXiv:2610.09532v1 Announce Type: new Abstract: We extend sample-based quantum diagonalization (SQD) to anharmonic vibrational spectra and use it to benchmark how vibrational ansatze scale on present-"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.09532v1 Announce Type: new Abstract: We extend sample-based quantum diagonalization (SQD) to anharmonic vibrational spectra and use it to benchmark how vibrational ansatze scale on present-day hardware under a direct one-hot encoding (up to 72 qubits). Five particle-conserving circuits are warm-started through vibrational coupled-cluster (VCC) t1, t2 amplitudes: UVCCSD, the compact heuristic circuit (CHC), and three unitary-cluster-Jastrow ansatze introduced here, VLUCJ, Vg-uCJ, and VIm-uCJ. A self-consistent configuration-recovery loop reconstructs correlated states from hardware samples in the low-retention regime where naive post-selection breaks down, enabling the calculation of ground-state energies for H_2O, CH_2O, and CH_2ClF (3-9 modes). We compare harmonic-oscillator and vibrational self-consistent-field (VSCF, "modal") reference bases. In the small-modal-basis regime relevant for near-term devices, the modal basis is typically more accurate than the harmonic-oscillator representation; empirically, it also yields substantially better-converged hardware sampling for deep circuits at these qubit counts. Across ansatze, we find a clear retention/accuracy tradeoff when scaling: the new VLUCJ circuit is the most hardware-robust, retaining the largest fraction of physically valid one-hot outcomes, whereas the more expressive uCJ variants and UVCCSD can recover more correlation when retention is sufficient. Finally, we extend the recovery protocol to excited states by targeting a chosen per-mode VSCF occupation and warm-starting it with a state-specific VCC calculation, and we demonstrate the calculation of one representative fundamental vibrational frequency per molecule on IBM QPUs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.09532) | 2026-10-08
