---
title: "Computational framework for quantum state tomography of spin ensembles"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.11868"
summary: "arXiv:2609.11868v1 Announce Type: new Abstract: We present Tomography-NMR, an open-source Python package that reconstructs quantum density matrices from spectroscopic measurement data. The package imp"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.11868v1 Announce Type: new Abstract: We present Tomography-NMR, an open-source Python package that reconstructs quantum density matrices from spectroscopic measurement data. The package implements a complete analysis pipeline for two-qubit quantum state tomography based on the product operator formalism: raw time-domain signals are Fourier-transformed into frequency-domain spectra, spectral peak intensities are mapped to expansion coefficients of the density matrix, and the full quantum state is reconstructed. Three integration methods are provided for different use cases: direct peak height measurement and fixed-parameter numerical integration require no theoretical reference and are suited to unknown states, achieving fidelities of approximately 98% on a benchmark set of known states, while a systematic parameter optimization against a known target state achieves reconstruction fidelities exceeding 99% for the same benchmark states. While the detailed theoretical framework for quantum state tomography is well established, the practical procedures for extracting density matrices from experimental spectra are often inadequately documented in the literature and obscured within proprietary software. This package addresses that gap by providing a fully transparent, reproducible implementation of every analysis step, from spectral preprocessing to density matrix visualization. The software has been validated on experimentally prepared two-qubit states measured via nuclear magnetic resonance (NMR) spectroscopy of coupled ^{31}P nuclei. Average reconstruction fidelities range from 0.975 to 0.995 across a benchmark set of 20 two-qubit states, including the computational basis states, Bell states, and the outputs of three fundamental quantum gates (CNOT, H, and T). Although developed for NMR, the modular architecture facilitates adaptation to other spectroscopic platforms and alternative measurement protocols.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.11868) | 2026-09-11
