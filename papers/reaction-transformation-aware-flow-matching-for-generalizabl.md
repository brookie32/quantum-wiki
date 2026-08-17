---
title: "Reaction-Transformation-Aware Flow Matching for Generalizable Transition State Generation"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.14076"
summary: "arXiv:2608.14076v1 Announce Type: new Abstract: Transition-state (TS) structures define the energetic barriers and mechanistic pathways of elementary chemical reactions, yet their identification remai"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2608.14076v1 Announce Type: new Abstract: Transition-state (TS) structures define the energetic barriers and mechanistic pathways of elementary chemical reactions, yet their identification remains computationally demanding because conventional saddle-point searches require expensive quantum-mechanical calculations. Recent machine-learning approaches have accelerated TS generation by predicting structures from reaction endpoint information, but they primarily learn geometric correspondence between endpoints and TSs, leaving the structural transformations underlying elementary reactions implicitly represented. To address this limitation, we introduce TransTS, a reaction-transformation-aware framework for generalizable TS generation from atom-mapped reactant-product pairs. TransTS explicitly learns atom-level structural transformations between reaction endpoints and integrates them with a unified atom-aligned geometric representation of reactants, TSs and products, enabling reaction-aware equivariant generation of TS geometries. TransTS is designed to provide reliable TS initial guesses for subsequent quantum-chemical refinement, where generated structures are evaluated not only by geometric similarity but also by their ability to converge to validated saddle points and recover the intended reaction pathways. Across IID and zero-shot OOD benchmarks, TransTS demonstrates improved TS initialization quality, with particularly strong generalization to unseen reaction distributions. On the challenging GDB-10-rxn and GDB-17-rxn OOD benchmarks, TransTS generates TS candidates that more frequently converge to validated saddle points and recover the intended elementary reactions after refinement than existing approaches under the same training regime. Scaling reaction coverage and model capacity further improves both geometric fidelity and refinement outcomes.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.14076) | 2026-08-17
