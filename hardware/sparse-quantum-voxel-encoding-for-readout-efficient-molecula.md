---
title: "Sparse Quantum Voxel Encoding for Readout-Efficient Molecular Geometry Reconstruction on NISQ Devices"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.26925"
summary: "arXiv:2607.26925v1 Announce Type: new Abstract: We propose a sparse computational-basis encoding of voxelized molecular geometries that converts molecular reconstruction from full-state tomography int"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.26925v1 Announce Type: new Abstract: We propose a sparse computational-basis encoding of voxelized molecular geometries that converts molecular reconstruction from full-state tomography into support recovery by computational-basis sampling. To realize the encoding scheme, the molecular space is discretized into a 3D grid, and each atom's position and chemical species is mapped to a single computational basis state. This discretization introduces spatial quantization at the voxel-resolution scale. The molecule is then encoded as an equal superposition over this sparse set of occupied states, where we assume that a suitable state preparation method exists. In contrast to full state tomography, which requires on the order of O(3^n imes 10^{2ext{--}3}) measurement shots, where n is the number of qubits, our proposed encoding scheme reduces to a coupon-collector sampling problem in the computational basis. Complete recovery of an A-atom molecule requires O(Alog A) shots on noise-free hardware. On noisy hardware, the required number of shots increases. We demonstrate the method on the 156-qubit IBM Kingston device using 8-qubit circuits to reconstruct the discretized geometry of a 10-atom ethylamine molecule with high mean reconstruction recall using only O(10^2) shots despite substantial hardware noise. These results demonstrate that our proposed encoding scheme is a practical, readout-efficient representation for molecular geometries on near-term devices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.26925) | 2026-07-30
