---
title: "Hash-QNeRF: Multiresolution Hash Encoding for Quantum Neural Radiance Fields"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.21675"
summary: "arXiv:2607.21675v1 Announce Type: new Abstract: Neural Radiance Fields (NeRF) have revolutionized novel view synthesis, yet their classical implementations remain computationally intensive for high-fi"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.21675v1 Announce Type: new Abstract: Neural Radiance Fields (NeRF) have revolutionized novel view synthesis, yet their classical implementations remain computationally intensive for high-fidelity rendering. QNeRF recently demonstrated the feasibility of training NeRF on gate-based quantum computers by combining amplitude embedding, parameterized quantum circuits (PQCs), parity-based measurements, and volumetric rendering. However, QNeRF relies on classical sinusoidal positional encoding for spatial coordinates, which scales poorly with scene complexity and resolution. In this work, we replace the sinusoidal positional encoding for spatial coordinates with the multiresolution hash encoding from Instant-NGP while keeping the view-direction encoding, amplitude MLP, quantum circuit, parity measurement, output scaling, and volumetric rendering pipeline unchanged. This hybrid design, Hash-QNeRF, retains the quantum radiance prediction step while benefiting from the fast convergence and memory efficiency of learnable hash grids. On a synthetic Blender scene, we achieve a final training loss of 0.003534, corresponding to approximately 24.5 dB PSNR on the fitted batch. Noise resilience experiments using Qiskit FakeKyiv and FakeTorino backends yield state fidelities of 0.93 to 0.98, indicating that hash encoding does not degrade the quantum circuit's noise tolerance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.21675) | 2026-07-27
