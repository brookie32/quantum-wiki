---
title: "A Coherent Memory Register for Sequential Quantum Generative Modeling, with Application to Calorimeter Showers"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.23050"
summary: "arXiv:2609.23050v1 Announce Type: new Abstract: Simulating the showers that particles deposit in a calorimeter, the detector that records their energy across many cells, is one of the largest computin"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.23050v1 Announce Type: new Abstract: Simulating the showers that particles deposit in a calorimeter, the detector that records their energy across many cells, is one of the largest computing costs in high-energy physics, and fast generative surrogates are needed. Quantum circuits have been proposed as such surrogates, but demonstrations on calorimeter data have either required a register that grows with the image, roughly one qubit per cell, or have passed the information between parts of the image through a classical channel. We remove both constraints for this problem, using a construction drawn from the sequential-generation and hidden-quantum-Markov-model literature. A shower image is generated block by block on a fixed register of six qubits. Three of them, the memory, are never measured. They hold what the circuit knows about the blocks already generated as a quantum state, so the correlations between distant parts of the image cross each block boundary as unmeasured amplitudes. The other three are measured and reset once per block, and each outcome selects the energy pattern of one block. The register size is set by the block, so adding cells to the image adds steps to the sequence, not qubits. We call the model a coherent-memory Born machine (CoMB), a Born machine being a circuit whose measurement statistics are the generated distribution. Its training loss grows only linearly with the number of blocks and never requires enumerating the image distribution, and a depth-two instance runs on an IBM superconducting processor. On a twelve-cell benchmark the model reproduces the energy distribution of every cell, the correlation matrix between cells, and the total-energy spectrum. Removing the three memory qubits, with everything else unchanged, produces independent blocks. Every correlation between blocks is carried by the unmeasured qubits and by nothing else.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.23050) | 2026-09-22
