---
title: "Quantum Krylov Learning"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "sensing"
tags: [sensing, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00537"
summary: "arXiv:2610.00537v1 Announce Type: new Abstract: The Hamiltonian of a natural quantum system is usually determined indirectly, by proposing microscopic models and comparing their predicted observables "
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00537v1 Announce Type: new Abstract: The Hamiltonian of a natural quantum system is usually determined indirectly, by proposing microscopic models and comparing their predicted observables with experiment. A more direct approach is to extract information about the Hamiltonian from measurements on the system itself. In many settings, however, direct access to the full system is unavailable and measurements can be performed only through controllable probes, as in quantum sensing and boundary spectroscopy. Existing Hamiltonian learning protocols under such restricted access typically require a special symmetry, a known parametric form, or controlled operations beyond free evolution. We introduce Quantum Krylov Learning (QKL), a restricted-access framework that avoids these requirements. QKL uses single temperature probe autocorrelators and their operator Krylov structure to extract model-independent spectral information about the unknown system. Rather than fitting a parametrized Hamiltonian, it reconstructs the operator Krylov Jacobi matrix representing the dynamical modes accessible to the probe. The method assumes that the unobserved system is at, or near, infinite temperature. Under this condition, the Jacobi matrix can be reconstructed directly from the autocorrelation of a probe observable, without oracle access to the Hamiltonian. The required operations are free evolution under the unknown H, together with probe state preparation and measurement. The learning core therefore requires no symmetry, no parametric model, and no controlled-unitary gates. We show a Lieb--Robinson bound for the operator Krylov chain and derive a data-driven criterion for the required observation window. We also establish an end-to-end sample complexity guarantee: under generic conditions on the spectral gaps and weights, the number of measurement shots required to achieve spectral precision arepsilon is polynomial in 1/arepsilon.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00537) | 2026-10-02
