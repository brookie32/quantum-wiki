---
title: "Biquaternion Algebra with Bilinear Multiplication: A General, Elegant, and Computationally Advantageous Framework for Relativistic Electronic Structure Calculations on CPUs and GPUs"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.02081"
summary: "arXiv:2609.02081v1 Announce Type: new Abstract: Quaternion algebra provides a natural representation of time-reversal-symmetric matrix structures in relativistic electronic-structure theory, whereas c"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02081v1 Announce Type: new Abstract: Quaternion algebra provides a natural representation of time-reversal-symmetric matrix structures in relativistic electronic-structure theory, whereas complementary time-reversal-antisymmetric structures extend this representation to complex quaternions, or biquaternions. Here, we explicitly exploit biquaternion algebra for fundamental objects, including operators, kinetically and magnetically balanced basis functions, and their expectation values, within a unified framework encompassing real, complex, and real quaternion subalgebras as special cases. To realize this framework computationally, we have developed HMATLIB, a biquaternion matrix library implemented within the ReSpect package for pure CPU and hybrid CPU/GPU execution. A key development is a bilinear algorithm for matrix-valued biquaternion multiplication that reduces the number of real matrix--matrix multiplications from 64 to 24 compared with the conventional component-wise approach, while the biquaternion representation effectively doubles the maximum accessible matrix dimension under the same 32-bit indexing constraint. Numerical benchmarks on modern CPU and GPU architectures demonstrate that the biquaternion formulation consistently outperforms its isomorphic complex-algebra counterpart. For the largest matrices reported, hybrid CPU/GPU execution accelerates bilinear matrix multiplication by approximately 5-8 times over pure CPU execution and matrix diagonalization by approximately 12 and 61 times relative to CPU oneAPI MKL and NVHPC OpenBLAS, respectively. These results establish biquaternion algebra as a general and computationally advantageous framework for modern relativistic electronic-structure calculations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.02081) | 2026-09-03
