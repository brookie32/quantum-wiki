---
title: "Turning Quantum Compiler Configuration Selection Upside Down: A Top-Down Paradigm"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.29170"
summary: "arXiv:2610.29170v1 Announce Type: new Abstract: Selecting an effective quantum compiler configuration requires coordinated decisions over both hardware targets and compiler settings, with the ultimate"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.29170v1 Announce Type: new Abstract: Selecting an effective quantum compiler configuration requires coordinated decisions over both hardware targets and compiler settings, with the ultimate goal of improving circuit execution fidelity. Existing SOTA approaches typically decompose this problem into two sequential stages: a device is chosen first, after which compiler options are tuned on that device through RL-based search. This bottom-up strategy can be fundamentally limited by its initial device decision, since a poorly matched backend may constrain the best fidelity achievable regardless of how effectively later compiler options are optimized. In contrast to classical compiler tuning, where the search space is often prohibitively large, the configuration space of quantum compilers remains manageable enough to support exhaustive search. Consequently, rather than repeatedly searching from candidate configurations, one can derive reusable configuration knowledge from offline oracle results and apply it directly to new circuits. In this paper, we introduce a top-down configuration-selection paradigm and build QuOPTBench, an exhaustively searched benchmark containing oracle configurations for 268 quantum circuits. We first study whether LLMs can directly infer suitable configurations and evaluate ten representative LLMs. The results reveal that vanilla LLMs remain far from the oracle. We then employ an LLM to extract transferable rules from sampled circuits governing configuration selection. Using these rules together with predictors trained on the enumerated configuration data of the sampled circuits, we design QuTOP, a rule-guided ML framework that performs fast configuration selection without iterative online search. Across our evaluation, the distilled rules consistently strengthen LLM-based selection, while QuTOP provides the strongest overall balance between solution quality and selection latency among the baselines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.29170) | 2026-10-22
