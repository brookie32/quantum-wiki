---
title: "PolyGPT: A Decoder-Only Transformer for Polymer Electrolyte Design"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.07438"
summary: "arXiv:2611.07438v1 Announce Type: cross Abstract: Designing polymer electrolytes requires control over both material properties and chemical structure. Here, we present PolyGPT, a Transformer with 38."
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.07438v1 Announce Type: cross Abstract: Designing polymer electrolytes requires control over both material properties and chemical structure. Here, we present PolyGPT, a Transformer with 38.3 million parameters that generates polymer repeat units from optional property targets, requests to include or exclude a specified chemical feature, and an electrolyte-domain condition. Using the model selected by validation loss, we compared unconditional generation with requests for electrolyte-associated structures, a low glass-transition temperature (Tg), or both. Unconditional and electrolyte-only generation achieved structural validity of 99.46% and 99.59%, respectively. However, electrolyte conditioning increased repetition: uniqueness among valid outputs fell from 99.99% to 51.74%. At a Tg target of 246.11 K, we compared generation with and without electrolyte conditioning, and adding the electrolyte condition slightly reduced the predictor-estimated mean absolute error from 26.97 to 26.07 K, but the fraction of all attempts yielding distinct valid polymers within 50 K of the target fell from 82.35% to 32.31%. When we also required absence from the training catalog, these yields were 59.90% and 19.71%, respectively. The lower yield persisted with a tighter 25 K tolerance. Domain conditioning also weakened control of inclusion requests: the mean fraction of attempts producing valid polymers containing the requested chemical feature fell from 94.27% to 31.27%. Across nine checkpoints, earlier models sometimes produced more distinct, catalog-unseen polymers meeting the Tg target: 10,000 checkpoint model with electrolyte conditioning and 30,000 checkpoint model without it. Together, these results show why property error alone is insufficient for evaluating conditional polymer generation. It must be considered alongside repetition, training-catalog novelty, and whether combined design requests are satisfied.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.07438) | 2026-11-06
