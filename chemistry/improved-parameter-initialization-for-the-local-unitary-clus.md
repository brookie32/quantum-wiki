---
title: "Improved parameter initialization for the (local) unitary cluster Jastrow ansatz"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.22476"
summary: "arXiv:2511.22476v2 Announce Type: replace Abstract: The unitary cluster Jastrow (UCJ) ansatz and its variant known as local UCJ (LUCJ) are promising choices for variational quantum algorithms for chem"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2511.22476v2 Announce Type: replace Abstract: The unitary cluster Jastrow (UCJ) ansatz and its variant known as local UCJ (LUCJ) are promising choices for variational quantum algorithms for chemistry due to their combination of physical motivation and hardware efficiency. The parameters of these ansatzes can be initialized from the output of a coupled cluster, singles and doubles (CCSD) calculation performed on a classical computer. However, truncating the number of repetitions of the ansatz, as well as discarding interactions to accommodate the connectivity constraints of near-term quantum processors, degrade the approximation to CCSD and the resulting energy accuracy. In this work, we propose two methods to improve the parameter initialization. The first method, which is applicable to both expectation value- and sample-based algorithms, uses compressed double factorization of the CCSD amplitudes to improve or recover the CCSD approximation. The second method, which is applicable to sample-based algorithms, uses approximate tensor network simulation to improve the quality of samples produced by the ansatz circuit. Both methods perform classical preprocessing to construct the initial circuit parameters and can be followed by parameter optimization using quantum measurements, although we do not perform such optimization in this work. We validate our methods using exact state vector simulation on systems of up to 52 qubits, as well as experiments on superconducting quantum processors using up to 65 qubits. Our results indicate that our methods can significantly improve the output of both expectation value- and sample-based quantum algorithms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.22476) | 2026-11-18
