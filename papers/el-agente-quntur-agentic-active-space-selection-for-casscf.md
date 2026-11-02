---
title: "El Agente Quntur: Agentic Active-Space Selection for CASSCF"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.38145"
summary: "arXiv:2610.38145v2 Announce Type: replace Abstract: Multireference calculations require time-consuming expert decisions about active spaces, state identity, and convergence. This study asks whether ag"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.38145v2 Announce Type: replace Abstract: Multireference calculations require time-consuming expert decisions about active spaces, state identity, and convergence. This study asks whether agents can make these decisions reliably. Using the El Agente Quntur multi-agent harness with GPT-5.6 Sol and GPT-5.6 Terra as its language models, agents study 32 fixed-geometry singlet excitations, detect missing active orbitals, compare excited states, and revise state assignments as calculations progress. Prompts specify equal-weight two-singlet state-averaged complete active space self-consistent field (CASSCF) calculations followed by strongly contracted second-order N-electron valence state perturbation theory (NEVPT2) with def2-TZVPD; agents choose and refine the active spaces. Excitation energies are evaluated against published complete active space second-order perturbation theory (CASPT2) reference values at matching geometries. Agentic execution reduces mean absolute error by 48% relative to six deterministic Active Space Finder protocols. Computational traces vary substantially across runs in selection strategies and cost, even for the same molecule. These results underscore the advantage of agentic active space selection over fixed workflows, yet leave room to improve efficiency through runtime-aware decision-making, reduced inter-agent communication overhead and redundancy, more systematic checks of state identity, and clearer stopping criteria.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.38145) | 2026-11-02
