---
title: "Analog Quantum Experiments Meet Automatic Differentiation - from Programs to Atoms"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.36167"
summary: "arXiv:2610.36167v1 Announce Type: new Abstract: Gradient-based optimization of analog quantum hardware poses a concrete programming problem: given an executable experiment P(heta) that returns only me"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.36167v1 Announce Type: new Abstract: Gradient-based optimization of analog quantum hardware poses a concrete programming problem: given an executable experiment P(heta) that returns only measurement samples, what executable experiment should the system run to obtain (d/dheta_ell)P(heta)? Conventional automatic differentiation cannot propagate through the inaccessible quantum state, while finite differences require a noise-sensitive step size and analytic gradient identities cover only parts of an experiment. We present DiffSimuQ, which shows that a broad class of open-loop analog quantum experiments is closed under automatic differentiation. A compositional transformation maps P(heta) to a derivative program D_ell[P(heta)] in the same language whose expected outcome is exactly the derivative. Only continuous evolution requires a strategy-specific rule, and we give two realizations. Our Nyquist shift rule (NSR) applies to general time-dependent evolution: we prove that the observable response to shifting the Hamiltonian along its tangent is band-limited even for non-commuting controls, enabling exact reconstruction from shifted executions. For involutory generators, a parameter-shift realization (PSR) inserts a parameter-independent operation at a sampled time. Because derivative programs remain ordinary programs, source and derivative experiments share one compiler, which reuses the source realization, lowers branches to device-ready neutral-atom controls, and selects between NSR and PSR based on estimated cost. Under device noise, the exact derivative programs differentiate the objective realized by the device, with hardware realization errors treated separately. In machine-level noisy emulation, NSR and PSR avoid the finite-difference error floor and improve closed-loop optimization; they win in complementary cost regimes, while each derivative branch at 1000 qubits add at most 0.3% to source compilation time.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.36167) | 2026-10-28
