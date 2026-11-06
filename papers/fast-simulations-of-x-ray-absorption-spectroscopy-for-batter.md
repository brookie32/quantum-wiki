---
title: "Fast simulations of X-ray absorption spectroscopy for battery materials on a quantum computer"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2506.15784"
summary: "arXiv:2506.15784v3 Announce Type: replace Abstract: X-ray absorption spectroscopy (XAS) is a leading technique for understanding structural changes in advanced battery materials such as lithium-excess"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2506.15784v3 Announce Type: replace Abstract: X-ray absorption spectroscopy (XAS) is a leading technique for understanding structural changes in advanced battery materials such as lithium-excess cathodes. However, extracting critical information like oxidation states from the experimental spectra requires expensive and time-consuming simulations. Building upon a recent proposal to simulate XAS using quantum computers, this work proposes a highly-optimized implementation of the time-domain algorithm for X-ray absorption. Among a host of improvements to Hamiltonian representation, circuit implementation, and measurement strategies, three optimizations are key to the efficiency of the algorithm. The first is the use of product formulas with the compressed double factorized form of the Hamiltonian. The second is recognizing that for spectroscopy applications, it is sufficient to control the error in the eigenvalues of the (approximate) Hamiltonian being implemented by the product formula, rather than the generic error on the full time evolution operator. Using perturbation theory to estimate this eigenvalue error, we find that significantly fewer Trotter steps are needed than expected from the time evolution error bound. The third is the choice of an optimized distribution of samples that takes advantage of the exponentially decaying Lorentzian kernel. Through constant factor resource estimates, we show that a challenging model Li_4Mn_2O cluster system with 18 spatial orbitals and 22 electrons in the active space can be simulated with 100 logical qubits and less than 4 imes 10^8 Toffoli gates per circuit. Finally, the algorithm is implemented on a simulator, and the reconstructed spectrum is verified against a classical computational reference. The low cost of our algorithm makes it attractive to use on fault-tolerant quantum devices to accelerate the development and commercialization of high-capacity battery cathodes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2506.15784) | 2026-11-06
