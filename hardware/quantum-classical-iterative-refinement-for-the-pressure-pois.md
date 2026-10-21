---
title: "Quantum-Classical Iterative Refinement for the Pressure-Poisson Equation on NISQ Hardware"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.24342"
summary: "arXiv:2610.24342v2 Announce Type: replace Abstract: We present a hybrid quantum-classical iterative refinement for the pressure-Poisson equation of the incompressible Navier-Stokes projection method o"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.24342v2 Announce Type: replace Abstract: We present a hybrid quantum-classical iterative refinement for the pressure-Poisson equation of the incompressible Navier-Stokes projection method on noisy quantum hardware. Rather than solving the pressure equation once per time step, we solve it repeatedly for the normalized residual and scale each quantum direction by a least-squares fit to the physical residual. As a result, the error of the quantum solve enters as a contraction factor sinheta_k of the residual rather than as an error floor. This removes the requirement of a state infidelity below 10^{-7} that was estimated for single-solve schemes. The hardware noise then sets the rate of convergence but not the attainable accuracy, and it is this change of the role of the quantum solve, not an improvement of the hardware, that allows the residual to converge. With a boundary-consistent staggered (MAC) discretization, the pressure residual equals the velocity divergence left after projection up to the factor Delta t/rho. On the IBM processor ibm_cleveland, a four-qubit (16imes16) problem reached a relative residual below 10^{-7} within eight to ten corrections in all 20 runs of a pre-registered experiment, whereas a single solve with a comparable number of shots stopped at 0.33-0.59. In a six-qubit (64imes64) pilot, all three runs reached the same tolerance in 13 corrections. On the IonQ Forte processor, a manufactured-solution benchmark reached 5.6imes10^{-8} in nine corrections. With the variational training itself carried out on ibm_cleveland, the residual fell to 5.6imes10^{-4} in seven corrections, below the pre-specified tolerance of 10^{-3}, at the rate predicted by a noise model. To the best of our knowledge, these are the first converged pressure solutions obtained on quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.24342) | 2026-10-21
