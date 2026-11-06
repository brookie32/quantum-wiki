---
title: "SesQ: A Surface Electrostatic Simulator for Precise Energy Participation Ratio Simulation in Superconducting Qubits"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.28524"
summary: "arXiv:2603.28524v3 Announce Type: replace Abstract: An accurate and efficient numerical electromagnetic model for superconducting qubits is essential for characterizing and minimizing design-dependent"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2603.28524v3 Announce Type: replace Abstract: An accurate and efficient numerical electromagnetic model for superconducting qubits is essential for characterizing and minimizing design-dependent dielectric losses. The energy participation ratio (EPR) is the commonly adopted metric used to evaluate these losses, but its calculation presents a severe multiscale computational challenge. Conventional finite element method (FEM) requires 3D volumetric meshing, leading to prohibitive computational costs and memory requirements when attempting to capture singular electric fields at nanometer-thin material interfaces. To address this bottleneck, we propose SesQ, a surface integral equation simulator tailored for the precise simulation of the EPR. By applying discretization on 2D surfaces, deriving a semi-analytical multilayer Green's function, and employing a dedicated non-conformal boundary mesh refinement scheme, SesQ accurately resolves singular edge fields without an explosive growth in the number of unknowns. Validations with analytically solvable models demonstrate that SesQ accelerates capacitance extraction by roughly two orders of magnitude compared to commercial FEM tools. While achieving comparable accuracy for capacitance extraction, SesQ delivers superior precision for EPR calculation. Simulations of practical transmon qubits further reveal that FEM approaches tend to significantly underestimate the EPR. Finally, the high efficiency of SesQ enables rapid iteration in the layout optimization, as demonstrated by minimizing the EPR of the qubit pattern, establishing the simulator as a powerful tool for the automated design of low-loss superconducting quantum circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.28524) | 2026-11-06
