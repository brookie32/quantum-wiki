---
title: "TorchSpin: Differentiable Electron Paramagnetic Resonance Simulation in PyTorch"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.18924"
summary: "arXiv:2610.18924v1 Announce Type: new Abstract: Interpreting electron paramagnetic resonance (EPR) spectra commonly requires repeated forward simulation and optimization of spin Hamiltonian parameters"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2610.18924v1 Announce Type: new Abstract: Interpreting electron paramagnetic resonance (EPR) spectra commonly requires repeated forward simulation and optimization of spin Hamiltonian parameters. Established software provides mature simulation and fitting methods, but these calculations are not generally available as differentiable components within machine-learning workflows. We present TorchSpin, an open-source PyTorch framework that ports the organization and numerical conventions of EasySpin into a tensor-based computational environment. Representative calculations spanning continuous-wave EPR, ENDOR, pulse EPR, spin dynamics, trajectory simulation, and magnetometry closely reproduced corresponding EasySpin results. In matched benchmarks, TorchSpin CPU execution was faster than EasySpin for six of nine workloads although performance depended strongly on the calculation. We therefore focused on the capabilities enabled by automatic differentiation in PyTorch. In a Cu(II) powder-spectrum demonstration, feedback propagated through TorchSpin improved the quality of a supervised convolutional neural network (CNN) without using parameter labels during refinement. Models trained from randomly initialized CNNs using only noisy spectra and TorchSpin reconstruction loss achieved median similarities of geq 0.99. CNNs trained on TorchSpin-generated libraries also transferred without adaptation to independently generated EasySpin spectra with performance comparable to EasySpin-trained controls. Once trained, the CNN produced initial parameter estimates in approximately 1 ms per spectrum while a batch of 512 was processed in approximately 1.3 ms with GPU acceleration. TorchSpin therefore provides both a tested Python implementation of established EPR calculations and a differentiable physical layer for rapid learned inference, spectral refinement, and parameter-label-free training.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.18924) | 2026-10-15
